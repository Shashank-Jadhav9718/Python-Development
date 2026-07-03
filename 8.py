#Implement a function that checks if two strings are anagrams of each other (contain the exact same characters in a different order).

string1 = str(input("Enter the first string1: ")).lower().strip()
string2 = str(input("Enter the second string2: ")).lower().strip()

def are_anagrams(string1, string2):
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False    

if are_anagrams(string1, string2):
    print("The two strings are anagrams of each other.")        
else:
    print("The two strings are not anagrams of each other.")

