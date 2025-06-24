# Exception Handling. An exception is an error that occurs during the execution of a program.
# Example: Dividing by zero or trying to open file that doesn't exist.
# Instead of letting the program crash, We can handle the situation using try, except, else, finally.

# Basic syntax:
# try:                      #Code that might throw an error
# except ErrorType:         #Code to run if that error occurs
# else:                     #code to run if no error occurs
# finally:                  #code that always runs

# Example

try:
    a =int(input("Enter a number: "))
    print(10/a)
except ZeroDivisionError:                       #Exception
    print("You can't divide by zero!")
except ValueError:                              #2nd Exception(Multiple Exception)
    print("That's not a valid number")
else:
    print("No Error!")
finally:
    print("Exception handling function completed!")


