total = int(input())


def merge(arr, temp, l, m, r):
    count = 0
    i, j, k = l, m, l
    while i <= m - 1 and j <= r:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            temp[k] = arr[j]
            j += 1
            k += 1
            count += (m - i)

    while i <= m - 1:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= r:
        temp[k] = arr[j]
        k += 1
        j += 1

    for i in range(l, r + 1):
        arr[i] = temp[i]

    return count



def _merge(arr, temp, l, r):
    count = 0
    if r > l:
        m = (l + r) // 2
        count += _merge(arr, temp, l, m)
        count += _merge(arr, temp, m + 1, r)
        count += merge(arr, temp, l, m + 1, r)
    return count

def merge_count(arr):
    temp = [0 for _ in arr]
    return _merge(arr, temp, 0, len(arr) - 1)


for _ in range(total):
    n_cars = int(input())
    train = [int(i) for i in input().split()]

    count = merge_count(train)
    print('Optimal train swapping takes %d swaps.' % count)
