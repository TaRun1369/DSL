s = "naman"
a = ''
t=" "
w = []
q = []
k = 0
longest = 0
print(s.count("am")) # part 5
print(s.find('am')) #part 4
print(s.count("n")) #part 2

def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

for i in range(0,len(s)):
    f = s[i]
    if (t == f):
        w.append(a)
        a = ""
    else:
        a = a + f
    if(i == (len(s) - 1)):
        w.append(a)
for j in range(0,len(w)):
    l = len(w[j])
    q.append(l)

for o in range(0,len(q)):
    if (longest < q[o]):
        longest = q[o]
        max = w[o]

    #else:
    #    print(w[o + 1])

if (s == reverse(s)):
    print("it is palindrome")
else:
    print("not a palindrome")



print(w)
print(q)
print(max)