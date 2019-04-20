#include <stdio.h>
#include <cmath>

#define MAX_ERROR 0.0001

using namespace std;

int v[100000];
int n, a;

double custom_sum(double height) {
	double sum = 0;
	for (int i = 0; i < n; i++) {
		if ((double)v[i] >= height) {
			sum += (double)v[i] - height;
		}
	}
	return sum;
}

double max() {
	int max = v[0];
	for (int i = 1; i < n; i++) {
		if (v[i] > max) {
			max = v[i];
		}
	}
	return (double)max;
}

double solve_height() {
	double lower_bound = 0;
	double upper_bound = max();
	double mid;

	while (lower_bound <= upper_bound) {
		mid = (lower_bound + upper_bound) / 2.0;
		double c = custom_sum(mid);

		if (fabs(c - a) < MAX_ERROR) {
			return mid;
		}
		if (c < a) {
			upper_bound = mid;
		} else {
			lower_bound = mid;
		}
	}
	return -1;
}

int main(int argc, char const *argv[])
{
	while(1) {
		scanf("%d %d ", &n, &a);
		if (!n && !a)
			break;

		int sum = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d ", &v[i]);
			sum += v[i];
		}

		if (sum < a) {
			printf("-.-\n");
		} else if (sum == a) {
			printf(":D\n");
		} else {
			printf("%.4lf\n", solve_height());
		}
	}
	return 0;
}
