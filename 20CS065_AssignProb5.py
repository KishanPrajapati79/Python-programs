print("20CS065 kISHAN Prajapati")
try:
    a = 10/0
    print (a)
except ArithmeticError:
        print ("Divide by zero.")
else:
    print ("Success.")
