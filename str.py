# return a string where each digit is repeated a number of times equals to its value. 
str = input("Enter your Number :")
def explode(str):
    newstr= ""
    for i in str:
        for j in range(int(i)):
            newstr+=i
    print("The New string is {}".format(newstr))

explode(str)
