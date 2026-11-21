# Infosys SP/DSE prep — Day 1, problems 4-7 (the counting notebook)
# 4. Count Frequencies  5. Duplicate Elements  6. First Non-Repeating  7. First Repeating

def frequencies(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq

def duplicates(arr):
    freq = frequencies(arr)
    return [x for x in freq if freq[x] > 1]

def first_non_repeating(arr):
    freq = frequencies(arr)
    for x in arr:
        if freq[x] == 1:
            return x
    return -1

def first_repeating(arr):
    seen = set()
    for x in arr:
        if x in seen:
            return x
        seen.add(x)
    return -1

if __name__ == "__main__":
    arr = [5, 2, 9, 5, 1, 2, 5]
    print(frequencies(arr))            # {5: 3, 2: 2, 9: 1, 1: 1}
    print(duplicates(arr))             # [5, 2]
    print(first_non_repeating([5, 2, 9, 5, 1, 2]))  # 9
    print(first_repeating([5, 2, 9, 5, 1, 2]))      # 5
