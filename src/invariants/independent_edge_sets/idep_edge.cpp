#include <iostream>
#include <vector>
#include <bitset>
#include <cmath>
#include "stl_io.h"

#include <boost/dynamic_bitset.hpp>
using namespace std;

template <class T>
bool is_in(const T &b, const set<T> &A) {
  return std::find(A.begin(), A.end(), b) != A.end();
};

bool check_edge_set(const boost::dynamic_bitset<> &edge_set,
                      const vector< pair<int, int> > &E) {

  const int n = edge_set.size();


  for(int i=0;i<n;i++) {
    for(int j=i+1;j<n;j++) {
      if(edge_set[i] && edge_set[j]) {
        int va0 = E[i].first;
        int va1 = E[i].second;

        int vb0 = E[j].first;
        int vb1 = E[j].second;
       
        if( va0==vb0 || va0==vb1 || va1==vb0 || va1==vb1 ) 
          return false;

      }
      
    }
  }

  return true;
}

void display_mask(vector< pair<int, int> > &E,
                  boost::dynamic_bitset<> &used_edges) {

  vector< pair<int, int> > E2;
  for(int i=0;i<E.size();i++) {
    if(used_edges[i]) E2.push_back(E[i]);
  }
  cout << E2 << ' ' <<   check_edge_set(used_edges,E) << endl;
}

void report_edge_set(boost::dynamic_bitset<> &edge_set) {
  cout << edge_set.to_ulong() << endl;
}


bool edge_itr(vector< pair<int, int> > &E,
             boost::dynamic_bitset<> &used_edges,
             int current_idx) {

  // This does not report the empty set, do this manually
  if(current_idx==0) { report_edge_set(used_edges);  }

  if(current_idx < E.size()) {

    auto trial_set = used_edges; 
    trial_set[current_idx] = 1;
    bool condition = check_edge_set(trial_set,E);

    if(condition) {
      report_edge_set(trial_set);

      // Recurse using this new valid set
      edge_itr(E, trial_set, current_idx+1);
    }

      // Recurse without flipping
    edge_itr(E, used_edges, current_idx+1);
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
  vector< pair<int, int> > E;
  for(int i=0, b_idx=edge_n-1;i<n;i++) {
    for(int j=i;j<n;j++,b_idx--) {
      if(adj_b[b_idx]) {
        E.push_back( {i,j} );
      }
    }
  }


  unsigned int edge_count = E.size();
  unsigned long max_edges = pow(2,edge_count);

  
  boost::dynamic_bitset<> edge_set(edge_count,0);
  edge_itr(E, edge_set, 0);
  

  // Iterate throught the edge combinations
  // find those that form indepdent edge sets
  /*
  for(unsigned long k=0;k<max_edges;k++) {
    boost::dynamic_bitset<> edge_set(edge_count,k);

    if( check_edge_set(edge_set, E) ) {
      report_edge_set(edge_set);
    }
  }
  */
  return 0;
}

