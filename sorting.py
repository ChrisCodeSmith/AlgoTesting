import time
import random


def insertion_sort(a: list):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i -= 1
        a[i+1] = key


list_a = random.sample(range(0, 100000), 10000)
print(f"Unsorted List: {list_a}")
start = time.time()
insertion_sort(list_a)
end = time.time()
print(f"Sorted List: {list_a}\nIn time: {end-start}")
