def all_function(num1,num2):
    return num1/num2

def div_number ():
    try :
        num1 = float(input("Enter number please :"))
        num2 = float(input("Enter number please :"))
        result = all_function(num1,num2)
        print (result)
    except ValueError:
        print ("find Error , Please Enter two number")
    except ZeroDivisionError :
        print ("Division by zero is not allowed")

div_number()