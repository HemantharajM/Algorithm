#include <iostream>

int get_change(int m) {
  //write your code here
  int n = 0;
  int arr[3];
  
  arr[0] = 10;
  arr[1] = 5;
  arr[2] = 1;

  for(int i = 0; i < 3;i++) {
          n = n + int(m / arr[i]);
          m = m - (int(m / arr[i]) * arr[i]);
  } 
  return n;
}

int main() {
  int m;
  std::cin >> m;
  std::cout << get_change(m) << '\n';
}
