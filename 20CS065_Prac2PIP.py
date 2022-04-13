"""
ID- 20CS065
NAME - KISHAN PRAJAPATI
GIT lnk - https://github.com/KishanPrajapati15/20CS065_KishanPrajapati/blob/main/20CS065_Prac2PIP.py
"""
print("\n ID- 20CS065 \n NAME- KISHAN PRAJAPATI")

print('\n---DICTIONARY---')

"[A] Write a Python script to check whether a given key already exists in a dictionary."
# Creating dictionary
dic = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
a = 2
# Checking if key a is present or not
if a in dic:
    print(a, " is present")
else:
    print(a, " is not present")

"[B] Write a Python script to merge two Python dictionaries."
# Creating dictionaries
dic1 = {1: 'a', 2: 'b', 3: 'c'}
dic2 = {4: 'd', 5: 'e'}
# Merging 2 dictionaries
dic3 = {**dic1, **dic2}
print(dic3)

"[C] Write a Python program to sum all the items in a dictionary."
#Creating dictionary
dic4 = {'a': 1, 'b': 2, 'c': 3}
#finding sum by for loop
sum = 0
for i in dic4.values():
    sum = sum + i
print(sum)

"[D] Write a Python script to add a key to a dictionary."
# Creating dictionary
dic5 = {1: 'a', 2: 'b', 3: 'c'}
# Adding new value
dic5.update({4: 'd'})
print(dic5)

"[E] Write a Python script to concatenate following dictionaries to create a new one."
#Creating dictionaries
dic6 = {1: 10, 2: 20}
dic7 = {3: 30, 4: 40}
dic8 = {5: 50, 6: 60}
# Merging given dictionaries
dic9 = {**dic6, **dic7, **dic8}
print(dic9)


print('\n\n---TUPLE---')

"[A] Write a Python program to create a tuple with different data types."
#Adding string,float,boolean,int in tupple
t1 = ('Hello', 1.11, True, 65)
print(t1)

"[B] Write a Python program to create a tuple with numbers and print one item."
# Creating tuple with numbers
t2 = 1, 2, 3, 4
# printing one element
print(t2[3])

"[C] Write a Python program to add an item in a tuple."
# Creating a tuple
t3 = 1, 2, 3
#Adding new item to tupple
t4 = t3 + (65,)
print(t4)

"[D] Write a Python program to convert a tuple to a string."
t5 = ('A', 'B', 'C')
stringT5 = ''.join(t5)
print('Tupple to String: ', stringT5)

"[E] Write a Python program to find the length of a tuple."
t6 = (1, 2, 3, 4, 5)
print(len(t6))

print('\n\n---SET---')

"[A] Write a Python program to add member(s) in a set and clear a set"
# Creating set
s1 = {'a', 'b', 'c'}
# Adding element to set
s1.add('d')
print(s1)
# Clearing the set
s1.clear()
print(s1)

"[B] Write a Python program to remove an item from a set if it is present in the set."
s2 = {'a', 'b', 'c', 'd'}
s2.remove('b')
print(s2)

"[C] Write a Python program to create an intersection, Union, difference of sets."
s3 = {1, 2, 3}
s4 = {3, 5, 6}
print('Intersection is : ', s3.intersection(s4))
print('Union is: ', s3 | s4)
print('Difference is: ', s3 - s4)

"[D] Write a Python program to find maximum and the minimum value in a set."
s5 = {2, 1, 3, 4,}
print('Max: ', max(s5))
print('Min: ', min(s5))

"[E] Write a Python program to find the most common elements and their counts from list, tuple, dictionary."
List = [1, 2, 3, 4, 1, 2, 1, 5]
Tuple = (1, 2, 3, 2, 4, 5)
def find(a):
    #finding max by converting to set
    c = max(set(a), key=a.count)
    # Printing most common element with its count
    print('Most common element is: ', c, 'with count: ', a.count(c))


#Function call
find(List)
find(Tuple)





