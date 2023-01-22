class string_operation:
    def __init__(self,s):
        self.s = s

    def reverse(self,s):
        str = ""
        for i in s:
            str = i + str
        return str
    def count_of_character(self,a):
        print(self.s.count(a))
        #part 2
    def find_index(self,d):
        print(self.s.find(d))
        #part 4

    def longestword(self):
        w = []
        q = []
        a = ''
        t = " "
        longest = 0
        print("Longest word is : ")

        for i in range(0, len(self.s)):
            f = self.s[i]

            if (t == f):
                w.append(a)
                a = ""
            else:
                a = a + f
            if (i == (len(self.s) - 1)):
                w.append(a)
        for j in range(0, len(w)):

            l = len(w[j])
            q.append(l)


        for o in range(0, len(q)):
            if (longest < q[o]):
                longest = q[o]
                max = w[o]
        print(max)
s = input("Enter string : ")
z = string_operation(s)
z.longestword()
if(s == z.reverse(s)):
    print("It is a palindrome")
else:
    print("It is not a palindrome")

a = input("Enter char whose frequency of occurrence is to find: ")
z.count_of_character(a)
d = input("Enter substring whose index of first appearance of the substring is displayed : ")
z.find_index(d)
e = input("Enter word whose count the occurrences is to find in a given string  : ")
z.count_of_character(e)