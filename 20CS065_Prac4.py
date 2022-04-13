print("ID- 20CS065\n NAME- KISHAN PRAJAPATI")
n = int(input())     #number of input
b = input()         #taking input elements
a = list(b)         #converting b to list
maxNum = max(a)      #getting max number from list
while max(a) == maxNum:      #removing every max number present in list
    a.remove(maxNum)

print(max(a))                 #printing the new maximum number
