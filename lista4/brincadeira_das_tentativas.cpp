#include <bits/stdc++.h>

using namespace std;

void print_array(array<int,8>& a, int size) {
	for (int i = 0; i < size-1; i++) {
		cout << a[i] << " ";
	}
	cout << a[size-1]<< endl;
}

// This function finds the index of the smallest element
// which is greater than 'first' and is present in str[l..h]
int findCeil (array<int, 8> a, int first, int l, int h)
{
    // initialize index of ceiling element
    int ceilIndex = l;

    // Now iterate through rest of the elements and find
    // the smallest element greater than 'first'
    for (int i = l+1; i < h; i++)
      if (a[i] > first && a[i] < a[ceilIndex])
            ceilIndex = i;

    return ceilIndex;
}

void permute_ordered(array<int, 8>& a, int size) {
	sort(a.begin(), a.begin()+size);

	while (true) {
		print_array(a, size);

		// Find the rightmost element which is smaller than its next.
        // Let us call it 'first elem'
        int i;
        for (i = size - 2; i >= 0; --i) {
           if (a[i] < a[i+1])
              break;
		}

		// If there is no such elem, all are sorted in decreasing order,
        // means we just printed the last permutation and we are done.
        if ( i == -1 ) {
            break;
		} else {
            // Find the ceil of 'first elem' in right of first elem.
            // Ceil of a elem is the smallest elem greater than it
            int ceilIndex = findCeil(a, a[i], i+1, size);

            // Swap first and second elements
            swap(a[i],a[ceilIndex] );

            // Sort the array on right of 'first elem'
            sort(a.begin()+i+1, a.begin()+size);
        }
	}
}

int main(int argc, char const *argv[]) {
	int n;
	bool first = true;
	array<int, 8> v;
	while(true) {
		cin >> n;
		if (!n) break;
		if (!first) {
			cout << endl;
		} else {
			first = false;
		}
		for (int i = 0; i < n; i++) {
			cin >> v[i];
		}
		permute_ordered(v, n);
	}
	return 0;
}

static const auto s = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    return nullptr;
}();
