print("\tID- 20CS065\n NAME- KISHAN PRAJAPATI")
for i in range(int(input())):  #running loop till no. of test cases
    n = input()                #taking input
    st = len(n)                 #finding length of string
    first = n[:st//2]           #saving first half of string in first var
    if(st%2 == 0):              #if n in string is even then second half is from s/2 till the length of string
        second = n[st//2:]
    else:                      #if n is odd
        second = n[(st//2)+1:]
    if (sorted(first) == sorted(second)):    #checking if both sub half are equal
        print("YES")
    else:
        print("NO")