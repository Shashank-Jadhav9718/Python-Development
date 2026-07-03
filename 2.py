# Reverse a string manually without using slicing ([::-1]) or the built-in reversed() function.

def ReverseStringManually(string):
    return string[::-1]

def ReverseStringUsingBuiltIn(string):
    return list(reversed(string))

def ReverseStringUsingLoop(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string


String = input("Enter a string to reverse : ")
print("Reversed string using slicing : ", ReverseStringManually(String))
print("Reversed string using built-in function : ", ReverseStringUsingBuiltIn(String)) 

print("Reversed string using loop : ", ReverseStringUsingLoop(String))
