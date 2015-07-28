#include "stl_io.h"

double atof(const string &a) { 
  return std::atof(a.c_str()); 
}

int atoi(const string &a) { 
  return std::atoi(a.c_str()); 
}

vector<double> atof(const vector<string> &a) { 
  vector<double> lhs;
  for(auto &x:a) lhs.push_back(atof(x));
  return lhs;
}

vector<int> atoi(const vector<string> &a) { 
  vector<int> lhs;
  for(auto &x:a) lhs.push_back(atoi(x));
  return lhs;
}


// -==- -- -==- ---==- -- -==- ---==- -- -==- ---==- -- -==- ---==- -- -==- --

// Pulls out a single string from the command line arguments and warns if not present

string parse_command_line(int argc, char*argv[]) {
  const int required_cmd_line_args = 1;
  if(argc != required_cmd_line_args+1) {
    cerr << argv[0] << " expects [f_config] as single argument" << endl;
    exit(3);
  }

  string f_config(argv[1]);
  return f_config;
}
