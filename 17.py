# Given a raw text file containing email addresses scattered throughout regular text, write a function to parse the text and extract all valid email patterns into a clean list without using external parsing frameworks.

import re 

source_file = 'sample.txt'
pattern = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    
def parse_email(source_file):
    valid_email = []
    with open(source_file , 'r') as reader:
        for line in reader:
            match = re.findall(pattern , line)
            valid_email.append(match)
            
    print(valid_email)
    
if __name__ == '__main__':
    parse_email(source_file)
        
                