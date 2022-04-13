print("\tID- 20CS065\n NAME- KISHAN PRAJAPATI")
test = int(input())
newDict = {}  #creting a dictionary for counter

for i in range(test):    #iterating through test cases
    word = input()       #taking word input
    if word in newDict:          #check if word is present in dictionary
        newDict[word] += 1       #increment if word is present
    else:
        newDict[word] = 1

print(len(newDict))            #print length of dictionary
print(' '.join([str(newDict[word]) for word in newDict]))  #converting to string and dsiplaying output