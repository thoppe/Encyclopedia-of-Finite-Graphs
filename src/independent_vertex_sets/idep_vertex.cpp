#include <iostream>
#include <set>
#include <bitset>
#include <cmath>
#include "stl_io.h"

#include <boost/dynamic_bitset.hpp>
using namespace std;

template <class T>
bool is_in(const T &b, const set<T> &A) {
  return std::find(A.begin(), A.end(), b) != A.end();
};

bool check_vertex_set(const boost::dynamic_bitset<> &verts,
                      const set< pair<int, int> > &E) {

  const int n = verts.size();

  for(int i=0;i<n;i++) {
    for(int j=i+1;j<n;j++) {
      if(verts[i] && verts[j]) {
        if(is_in({i,j},E)) return false;
      }
    }
  }
  return true;

}

int main (int argc, char *argv[]) {

  // Load the command line options
  if(argc<3) {
    cerr << argv[0] << " [N] [simple_graph_relation]" << endl;
    exit(2);
  }
  int n = atoi(argv[1]);
  unsigned long adj = stoull(argv[2]);

  // Find the binary representation
  int edge_n = (n*(n+1))/2;
  boost::dynamic_bitset<> adj_b(edge_n, adj);


  // Get the edge set
  set< pair<int, int> > E; 
  for(int i=0, b_idx=edge_n-1;i<n;i++) {
    for(int j=i;j<n;j++,b_idx--) {
      if(adj_b[b_idx]) {
        E.insert( {i,j} );
      }
    }
  }


  // Iterate throught the vert combinations
  // find those that form indepdent vertex sets
  unsigned long max_verts = pow(2,n);
  for(unsigned long k=0;k<max_verts;k++) {
    boost::dynamic_bitset<> verts(n,k);

    if( check_vertex_set(verts, E) ) {
      //cout << verts << ' ' << verts.to_ulong() <<  endl;
      cout << verts <<  endl;
    }
  }

  return 0;
}

