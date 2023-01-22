# Write a python program to store first year percentage of students in array. Write function for
# sorting array of floating point numbers in ascending order using quick sort and display top
# five scores.Write a python program to store first year percentage of students in array.

print("Quick Sort Algorithm ")
A1 = []
n = int(input("Enter the number of students : "))
j = 1
for i in range(0, n):
    print("Enter percentage of student", i + 1, ":")
    elem = int(input())
    A1.append(elem)
    j = j + 1
lb = A1[0]
ub = A1[n - 1]


class order:
    def __init__(self, a, lb, ub):
        self.a = a
        self.lb = lb
        self.ub = ub

    def partition(self, a, lb, ub):
        pivot = a[lb]
        i = lb
        j = ub
        while i < j:
            while a[i] <= pivot and i < n - 1:
                i = i + 1
            while a[j] > pivot:
                j = j - 1
            if i < j:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
        temp = a[lb]
        a[lb] = a[j]
        a[j] = temp
        return j

    def quicksort(self, a, lb, ub):
        if lb < ub:
            loc = self.partition(a, lb, ub)
            self.quicksort(a, lb, loc - 1)
            self.quicksort(a, loc + 1, ub)

        # (quicksort(A1, 0, (len(A1) - 1)))
        return a


o1 = order(A1, lb, ub)
print("sorted list using quick sort is: ")
o1.quicksort(A1, 0, (len(A1) - 1))
print(A1)
