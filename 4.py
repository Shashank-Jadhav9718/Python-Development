# Write a function to check if a string is a palindrome, ignoring spaces, punctuation, and capitalization.
import string

string = input("Enter a string to check if it's a palindrome: ")
string = string.lower().replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "")
print("Processed string for palindrome check: ", string)
def is_palindrome(s):
    if s[::-1] == s:
        return True
    else:
        return False

if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


