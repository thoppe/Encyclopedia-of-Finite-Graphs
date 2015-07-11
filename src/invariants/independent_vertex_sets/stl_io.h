#ifndef STL_IO_H
#define STL_IO_H

#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <deque>

#include <random>

using std::cout;
using std::cerr;
using std::endl;

using std::string;
using std::vector;
using std::set;
using std::list;
using std::map;
using std::deque;

using std::ostream;

// Pulls out a single string from the command line arguments and warns if not present
string parse_command_line(int argc, char*argv[]);


// Useful string functions
double atof(const string &a);
int    atoi(const string &a);

vector<double> atof(const vector<string> &a);
vector<int> atoi(const vector<string> &a);

template<typename Iter, typename RandomGenerator>
Iter random_element(Iter start, Iter end, RandomGenerator& g) {
  std::uniform_int_distribution<> dis(0, std::distance(start, end) - 1);
  std::advance(start, dis(g));
  return start;
}

template<typename Iter>
Iter random_element(Iter start, Iter end) {
    static std::random_device rd;
    static std::mt19937 gen(rd());
    return random_element(start, end, gen);
}

template <typename T>
vector<vector<T> > reshape(const vector<T> &A, int nx, int ny) {
  vector<vector<T> > lhs;
  typename vector<T>::const_iterator a = A.begin();

  for(int i=0;i<nx;i++) {
    lhs.push_back({});
  
    for(int j=0;j<ny;j++) {
      T val = *a;
      lhs[i].push_back(val);
      ++a;
    }
  }
  return lhs;
}


template <class T1, class T2>
ostream& operator<<(ostream& s, const map<T1, T2> &A){
  if(A.empty()) { s << "{ }"; return s; }

  typename map<T1,T2>::const_iterator itr     = A.begin();
  typename map<T1,T2>::const_iterator itr_end = --A.end();

  s << "{";
  for(itr=A.begin();itr!=A.end();++itr) {  
    s << (*itr).first << ":" << (*itr).second;
    if(itr != itr_end) { s << ","; }
  }
  s << "}";

  return s;
}


template <class T>
ostream& operator<<(ostream& s, const list<T> &A){
  if(A.empty()) return s << "[]";

  s << "[";
  for(unsigned int i=0;i<A.size()-1;++i) s << A[i] << ',';
  s << A[A.size()-1] << "]";
  return s;
}

template <class T1, class T2>
  ostream& operator<<(ostream& s, const std::pair<T1,T2> &A){
  s << "{" << A.first << "," << A.second << "}"; 
  return s;
}

template <class T>
ostream& operator<<(ostream& s, const deque<T> &A){
  if(A.empty()) 
    return s << "[]";

  s << "[";
  typename deque<T>::const_iterator itr_penultimate = --A.end();
  typename deque<T>::const_iterator itr = A.begin();

  while(itr != itr_penultimate) {
    s << *itr << ", ";
    itr++;
  }
  return s << *itr << "]";
}

template <class T>
ostream& operator<<(ostream& s, const vector<T> &A){
  if(A.empty()) 
    return s << "[]";

  s << "[";
  typename vector<T>::const_iterator itr_penultimate = --A.end();
  typename vector<T>::const_iterator itr = A.begin();

  while(itr != itr_penultimate) {
    s << *itr << ", ";
    itr++;
  }
  return s << *itr << "]";
}

template <class T>
ostream& operator<<(ostream& s, const vector<vector<T> > &A){
  if(A.empty()) return s << "[]";

  s << "[";
  for(int i=0;i<A.size()-1;++i) s << A[i] << ',';
  s << A[A.size()-1] << "]";
  return s;
}

template <class T>
ostream& operator<<(ostream& s, const set<T> &A){
  if(A.empty()) return s << "{ }";

  s << "{";
  typename set<T>::const_iterator it;
  typename set<T>::const_iterator eit = --A.end();
  for(it=A.begin();it!=eit;++it) s << (*it) << ',';
  return s << (*eit) << "}";
}

template <class T>
ostream& operator<<(ostream& s, const set<vector<T> > &A){
  if(A.empty()) return s << "{ }";

  s << "{";
  typename set<vector<T> >::const_iterator it;
  typename set<vector<T> >::const_iterator eit = --A.end();
  for(it=A.begin();it!=eit;++it) s << (*it) << ',';
  return s << (*eit) << "}";
}

#endif
