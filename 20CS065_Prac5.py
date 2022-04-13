print("\tID- 20CS065\n NAME- KISHAN PRAJAPATI")
a = ("Hello World")
print(a.swapcase())  #swap case by inbuilt method

s = input()             #taking string input
s1 = ""                 #creating an empty string
for i in range(len(s)):    #iteration till length of string
    if s[i].isupper():       #if any letter is in uppercase then converting it to lower and adding to s1
        s1 += s[i].lower()
    elif s[i].islower():     #if any letter is in lowercase then converting it to upper and adding to s1
        s1 += s[i].upper()
    else:                    #adding rest all elements to s1 as it is.
        s1 += s[i]
print(s1)                       #printing string