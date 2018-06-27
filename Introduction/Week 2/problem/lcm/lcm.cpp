#include <iostream>

long long gcd_fast(long long a, long long b) 
{
        long long temp = 0;

        if( a < b) {
                temp = b;
                b = a;
                a = temp;
        }

        if( b == 0) {
                return a;
        } else {
                return gcd_fast(a % b, b);
        }

}

long long lcm_fast(long long  a, long long b) 
{
        int multiple = 0;

        multiple = gcd_fast(a, b);

        return ((long long)(a * b)) / multiple ;
}

int main() {
  long long a, b;
  std::cin >> a >> b;
  std::cout << lcm_fast(a, b) << std::endl;
  return 0;
}
