#include <iostream>

using namespace std;

long long fibonacci_slow(int n);

int main()
{
	int n;

	cin >> n;

	cout << fibonacci_slow(n) << endl;

}

long long fibonacci_slow(int n)
{
	
	if(n <= 1) {
		return n;
	} else {
		return ((long long) fibonacci_slow(n-1)) + fibonacci_slow(n-2);
	}

}
