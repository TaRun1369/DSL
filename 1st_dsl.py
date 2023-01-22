# function for intersection of two sets
def intersection(lst1,lst2):
    lst3=[]
    for val in lst1:
        if val in lst2:
            lst3.append(val)
    return lst3


# Function for union of two sets

def union(lst1,lst2):
    lst3=lst1.copy()
    for val in lst2:
        if val not in lst3:
            lst3.append(val)
    return lst3



# function for difference between two sets
def diff(lst1,lst2):
    lst3=[]
    for val in lst1:
        if val not in lst2:
            lst3.append(val)
    return lst3

#function for symm diff between two sets

def sym_diff(lst1,lst2):
    lst3=[]
    D1=diff(lst1,lst2)
    # print("Difference between Cricket and Badminton (C-B) is : ", D1)
    D2=diff(lst2,lst1)
    # print("Difference between Badminton and Cricket (B-C) is : ", D2)
    lst3=union(D1,D2)
    return lst3

c = []
n = int(input("\nno. of  cricketer : "))
print("names of ",n,"cricketers :")
for i in range(0,n):
    ele = input()
    c.append(ele)
print("list of cricketers :" +str(c))

f = []
n = int(input("\nno. of  footballer : "))
print("names of ",n,"footballer :")
for i in range(0,n):
    ele = input()
    f.append(ele)
print("list of footballer :" +str(f))

b = []
n = int(input("\nno. of  batminton player : "))
print("names of ",n,"batminton player :")
for i in range(0,n):
    ele = input()
    b.append(ele)
print("list of badminton player :" +str(b))

print("List of students who play both cricket and badminton :", intersection(c,b))
print("List of students who play either cricket or badminton but not both :", sym_diff(b,c))
l = diff(f,c)
m = diff(f,b)
print("Number of students who play neither cricket nor badminton :", len(intersection(l,m)))
k = intersection(c,f)

print("Number of students who play cricket and football but not badminton. :", len(diff(k,b)))
