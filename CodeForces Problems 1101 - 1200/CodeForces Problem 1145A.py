def thanos_sort(array):
    n = len(array)
    if array == sorted(array):
        return n
    else:
        return max(thanos_sort(array[:n // 2]), thanos_sort(array[n // 2:]))

n = int(input())
array = [int(i) for i in input().split()]
print(thanos_sort(array))
