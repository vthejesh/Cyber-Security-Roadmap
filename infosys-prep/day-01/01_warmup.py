# Infosys SP/DSE prep — Day 1 warm-up (from memory, Lesson 1)
# Find Largest, Find Second Largest, Reverse an Array

def find_largest(arr):
    largest = arr[0]
    for x in arr:
        if x > largest:
            largest = x
    return largest

def find_second_largest(arr):
    largest = second = None
    for x in arr:
        if largest is None or x > largest:
            second = largest
            largest = x
        elif x != largest and (second is None or x > second):
            second = x
    return second

def reverse_array(arr):
    return arr[::-1]

if __name__ == "__main__":
    print(find_largest([5, 2, 9, 1]))          # 9
    print(find_second_largest([5, 2, 9, 1]))   # 5
    print(reverse_array([10, 20, 30]))         # [30, 20, 10]
