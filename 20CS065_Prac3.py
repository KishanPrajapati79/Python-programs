print("ID- 20CS065\n NAME- KISHAN PRAJAPATI")
k = int(input()) #taking input for total number of people per group
rooms = (int(x) for x in input().split(' '))  #input for rooms
x = {}   #empty dict

for i in rooms:             #iteration through each room
    if not i in x:           #is element is not present in x then add 1 else increasing the count
        x[i] = 1
    else:
        x[i] += 1

for key, val in x.items():   #checking key,value pair of dictionary
    if val != k:             #if any value not equal to 5 then print it
        print(key)