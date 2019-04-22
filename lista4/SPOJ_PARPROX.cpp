#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[]) {
	int n, x, y;
	array<pair<int, int>, 1000> v;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> x;
		cin >> y;
		v[i] = pair<int, int>(x, y);
	}

	double aux;
	double dist = DBL_MAX;
	for (int i = 0; i < n; i++) {
		for (int j = i+1; j < n; j++) {
			aux = sqrt(pow(v[j].first - v[i].first, 2) + pow(v[j].second - v[i].second, 2));
			if (aux < dist) {
				dist = aux;
			}
		}
	}
	printf("%.3lf", dist);
	return 0;
}
