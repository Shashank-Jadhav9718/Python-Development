# Find the first non-repeating character in a string and return its index. If it doesn't exist, return -1.

string = input("Enter a string : ")   

def first_non_repeating_character(s):
    char_count = {}
    print("char count initialized: ", char_count)
    print("Counting characters in the string...")
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
            print(f"Character '{char}' count updated to: {char_count[char]}")   
        else:
            char_count[char] = 1
            print(f"Character '{char}' count initialized to: {char_count[char]}")

    print("Final character count: ", char_count)
            
    for index, char in enumerate(s):
        if char_count[char] == 1:
            print(f"Character '{char}' is non-repeating and at index: {index}") 
            return index
            
    return -1

result = first_non_repeating_character(string)
if result != -1:
    print(f"The first non-repeating character is at index: {result}")           
else:    
    print("There is no non-repeating character in the string.")