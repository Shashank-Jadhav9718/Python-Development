#Write a script that reads a text file line-by-line and outputs the total count of words, unique words, and lines to the terminal.

file_name = "sample.txt"

total_lines = 0
total_words = 0
unique_words = set()

with open(file_name , 'r') as file:
    for line in file:
        total_lines += 1
        words = line.split()
        total_words += len(words)
        for word in words:
            unique_words.add(word.lower())
        
print(f"Total lines : {total_lines}")
print(f"Total words : {total_words}")
print(f"Uniques Words: {unique_words}")