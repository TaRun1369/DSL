# a) Write a python program to store roll numbers of student in array who attended training
# program in random order. Write function for searching whether particular student attended
# training program or not, using Linear search and Sentinel search.
# b) Write a python program to store roll numbers of student array who attended training
# program in sorted order. Write function for searching whether particular student attended
# training program or not, using Binary search and Fibonacci search+
# self.key   self.list1
# self.FibonacciGenerator(self,n)

def FibonacciGenerator(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return FibonacciGenerator(n - 1) + FibonacciGenerator(n - 2)

def linear_Search(list1, n, key):
    for i in range(0, n):
        if (list1[i] == key):
            return i
    return -1

def sentinel(list1, key):
    size = len(list1)
    list1.append(key)
    i = 0
    while(list1[i] != key):
        i += 1
    if(i == size):
        return -1
    else:
        return i


def binary_search(list1, key):
    low = 0
    high = len(list1) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if list1[mid] < key:
            low = mid + 1

        # If x is smaller, ignore right half
        elif list1[mid] > key:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1
#
# def fib_search(list1, key):
#     # ffinding the length of given list
#     length = len(list1)
#     first = -1
#     x0 = 0
#     x1 = 1
#     x2 = 1
#     while(x2 < length):
#         x0 = x1
#         x1 = x2
#         x2 = x1 + x0
#     while(x2 > 1):
#         eleIndex = min(first + x0, length - 1)
#         if list1[eleIndex] < key:
#             x2, x1 = x1, x0
#             x0 = x2 - x1
#             start = eleIndex
#         elif list1[eleIndex] > key:
#             x2 = x0
#             x1 = x1 - x0
#             x0 = x2 - x1
#         else:
#             return eleIndex
#     if (x1) and (list1[length - 1] == key):
#         return length - 1
#     return None

def FibonacciSearch(list1, key):
    m = 0
    while FibonacciGenerator(m) < len(list1): #
        m = m + 1
    offset = -1
    while (FibonacciGenerator(m) > 1):
        i = min( offset + FibonacciGenerator(m - 2) , len(list1) - 1)
        # print('Current Element : ',list1[i])
        if (key > list1[i]):
            m = m - 1
            offset = i
        elif (key < list1[i]):
            m = m - 2
        else:
            return i
    if(FibonacciGenerator(m - 1) and list1[offset + 1] == key):
        return offset + 1
    return -1



list1 = [1, 3, 5, 4, 7, 9]
key = 7


n = len(list1)
res = linear_Search(list1, n, key)
if (res == -1):
    print("Element not found")
else:
    print("Element found in linear at index: ", res)
    linear_Search(list1,n,key)

res1 = sentinel(list1,key)
if (res1 == -1):
    print("Element not found")
else:
    print("Element found in sentinel at index: ", res1)
    sentinel(list1,key)



res2 = binary_search(list1,key)
if (res2 == -1):
    print("Element not found")
else:
    print("Element found in binary search at index: ", res2)
    binary_search(list1,key)

list1.sort()

# print("Element found in Fibonacci Search at index: ", FibonacciSearch(list1, key))

res3 = FibonacciSearch(list1,key)
if (res3 == -1):
    print("Element not found")
else:
    print("Element found in fibonnaci search at index: ", res3)
    # FibonacciSearch(list1,key)
