def char_frequency(s1):
    dict = {}
    for n in s1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print("20CS065 Kishan Prajapati")
str = input("Enter a string: ")
print(char_frequency(str))
