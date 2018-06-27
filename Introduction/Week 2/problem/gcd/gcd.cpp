#include <iostream>

int gcd_fast(int a, int b) 
{
        
        int temp;

        if( a < b) {
                temp = b;
                b = a;
                a = temp;
        }

        if(b == 0) {
                return a;
        } else {
                return gcd_fast(a % b, b);
        }

}

int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << gcd_fast(a, b) << std::endl;
  return 0;
}
