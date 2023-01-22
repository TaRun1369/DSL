# Write a python program to store second year percentage of students in array. Write
# function for sorting array of floating-point numbers in ascending order using a)
# Insertion sort b) Shell Sort and display top five scores

class assignment5:
    def __init__(self,list1):
        self.list1=list1
    def insertion(self):
        for step in range(1, len(self.list1)):
            key = self.list1[step]
            j = step - 1


            while j >= 0 and key < self.list1[j]:
                self.list1[j + 1] = self.list1[j]
                j = j - 1

            self.list1[j + 1] = key

    def shellSort(self,n):

        interval = n // 2
        while interval > 0:
            for i in range(interval, n):
                temp = list1[i]
                j = i
                while j >= interval and self.list1[j - interval] > temp:
                    self.list1[j] = self.list1[j - interval]
                    j -= interval

                self.list1[j] = temp
            interval //= 2



list1 = [9, 5, 1, 4, 3]
y=assignment5(list1)
y.insertion()
print('Sorted Array in Ascending Order by insertion sort :')
print(list1)

size = len(list1)
y.shellSort(size)
print('Sorted Array in Ascending Order by shell sort :')
print(list1)
list2 = list1.reverse()
print('Top five scores are :')
print(list2)
