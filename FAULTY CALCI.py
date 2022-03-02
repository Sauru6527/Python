num1  = int(input("ENTER NUMBER = "))
num2  = int(input("ENTER NUMBER = "))

print("   1     =   MULTIPLICATION" )
print("   2     =   ADDITION" )
print("   3     =   SUBSTRACTION" )
print("   4     =   DIVISION" )

user  = int(input("ENTER CHOICE = "))

if(num1 == 45 and num2 == 3 and user == 1):
                                           print("ANSWER = 55")

elif(num1 == 56 and num2 == 9 and user == 2):
                                            print("ANSWER = 77")

elif(num1 == 56 and num2 == 6  and user == 4):
                                            print("ANSWER = 4 ")                                         
else:                                           
     if(user == 1):
                   print("ANSWER  =  ",num1*num2)
                   
     elif(user == 2):
                     print("ANSWER  =  ",num1+num2)
     elif(user == 3):
                     print("ANSWER  =  ",num1-num2)
     elif(user == 4):
                     print("ANSWER  =  ",num1/num2)
     else:
         print("SEE MENU DEAR")
