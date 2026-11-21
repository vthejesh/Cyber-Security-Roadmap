# Infosys SP/DSE prep — Day 1, problems 1-3
# 1. Check if Array Is Sorted  2. Find Missing Number  3. Count Even and Odd

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

def missing_number(arr, n):
    expected = n * (n + 1) // 2
    return expected - sum(arr)

def count_even_odd(arr):
    even = odd = 0
    for x in arr:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

if __name__ == "__main__":
    print(is_sorted([1, 2, 2, 5, 9]))          # True
    print(missing_number([1, 2, 4, 5], 5))     # 3
    print(count_even_odd([5, 2, 9, 1, 7, 4]))  # (2, 4)
