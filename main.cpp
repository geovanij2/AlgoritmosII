#include <bits/stdc++.h>

int mod(std::string num, int a)
{
    // Initialize result
    int res = 0;

    // One by one process all digits of 'num'
    for (int i = 0; i < num.length(); i++)
         res = (res*10 + (int)num[i] - '0') %a;

    return res;
}

int main(int argc, char const *argv[])
{
	using namespace std;
	int t;
	string n;
	int memo[1500];
	memo[0] = 0;
	memo[1] = 1;
	for (int i = 2; i < 1500; i++) {
		memo[i] = (memo[i-1] + memo[i-2]) % 1000;
	}
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n;
		cout << setfill('0') << setw(3) << memo[mod(n, 1500)] << endl;
	}
	return 0;
}
