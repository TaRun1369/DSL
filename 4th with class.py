# a) Write a python program to store roll numbers of student in array who attended training
# program in random order. Write function for searching whether particular student attended
# training program or not, using Linear search and Sentinel search.
# b) Write a python program to store roll numbers of student array who attended training
# program in sorted order. Write function for searching whether particular student attended
# training program or not, using Binary search and Fibonacci search+

class search1:
    def __init__(self, list1, key):
        self.list1 = list1
        self.key = key

    def FibonacciGen(self, n):
        if n < 1:
            return 0
        elif n == 1:
            return 1
        else:
            return self.FibonacciGen(n - 1) + self.FibonacciGen(n - 2)

    # def linear_search(self):
    #     for i in range(0, len(self.list1)):
    #         if (self.list1[i] == self.key):
    #             return i
    #     return -1
    # def sentinel_search(self):
    #     size = len(self.list1)
    #     self.list1.append(self.key)
    #     i = 0
    #     while (self.list1[i] != self.key):
    #         i += 1
    #     if (i == size):
    #         return -1
    #     else:
    #         return i
    #
    # def binary_search(self):
    #     low = 0
    #     high = len(self.list1) - 1
    #     mid = 0
    #
    #     while low <= high:
    #
    #         mid = (high + low) // 2
    #
    #         # If x is greater, ignore left half
    #         if self.list1[mid] < self.key:
    #             low = mid + 1
    #
    #         # If x is smaller, ignore right half
    #         elif self.list1[mid] > self.key:
    #             high = mid - 1
    #
    #         # means x is present at mid
    #         else:
    #             return mid
    #
    #     # If we reach here, then the element was not present
    #     return -1

    def FibonacciSearch(self):
        n = 0
        while self.FibonacciGen(n) < len(self.list1):
            offset = -1
        while (self.FibonacciGen(n) > 1):
            i = min(offset + self.FibonacciGen(n - 2), (len(self.list1) - 1))
            # print('Current Element : ',list1[i])
            if (self.key > self.list1[i]):
                n = n - 1
                offset = i
            elif (self.key < self.list1[i]):
                n = n - 2
            else:
                return i
        if (self.FibonacciGen(n - 1) and self.list1[offset + 1] == self.key):
            return offset + 1
        return -1


list1 = [1, 3, 5, 4, 7, 9]
key = 4

z = search1(list1, key)

# res = z.linear_search()
# if (res == -1):
#     print("Element not found")
# else:
#     print("Student is at this position has attennted the session")
#     z.linear_search()
#
# res1 = z.sentinel_search()
# if (res1 == -1):
#     print("Element not found")
# else:
#     print("Element found in sentinel at index: ", res1)
#     z.sentinel_search()
#
#
#
# res2 = z.binary_search()
# if (res2 == -1):
#     print("Element not found")
# else:
#     print("Element found in binary search at index: ", res2)
#     z.binary_search()
#
list1.sort()

print("Element found in fibonnaci search at index: ", z.FibonacciSearch())

res3 = z.FibonacciSearch()
if (res3 == -1):
    print("Element not found")
else:
    print("Element found in fibonnaci search at index: ", res3)

