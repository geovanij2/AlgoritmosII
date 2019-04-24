#include <bits/stdc++.h>

using namespace std;

unordered_map<int, int> complements;

int find_num_pairs_that_add_to_sum(const array<int, 100000>& arr, int size, int sum) {
	complements.clear();
	int counter = 0;
	for (int i = 0; i < size; i++) {
		// achou par
		if (complements[arr[i]] > 0) {
			counter++;
			complements[arr[i]]--;
		} else {
			complements[sum - arr[i]]++;
		}
	}
	return counter;
}

int main(int argc, char const *argv[]) {
	array<int, 100000> v;
	int t, n, m;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n >> m;
		for (int j = 0; j < n; j++) {
			cin >> v[j];
		}
		cout << find_num_pairs_that_add_to_sum(v, n, m) << endl;
	}
	return 0;
}

static const auto s = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    return nullptr;
}();
