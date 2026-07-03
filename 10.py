#Implement a function to find the longest common prefix string among an array of strings. If there is no common prefix, return an empty string.

words = ["flower", "shashank", "flight", "flourish", "flock", "flute"]

def longest_common_prefix(words):
    if not words:
        return ""
    
    prefix = words[0]
    
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    
    return prefix


result = longest_common_prefix(words)
print("The longest common prefix is: ", result) 


