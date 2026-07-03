import re

def clean_paragraph(text):
    text = re.sub(r'[ \t\n]+', ' ', text).strip()
    text = re.sub(r' +([.!?,;:])', r'\1', text)
    text = re.sub(r'([.!?])([A-Za-z])', r'\1 \2', text)
    
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return ' '.join(s[0].upper() + s[1:] for s in sentences if s)


def clean_paragraph_no_regex(text):
    text = text.replace('\n', ' ').replace('\t', ' ')
    
    while '  ' in text:
        text = text.replace('  ', ' ')
    
    for p in '.!?,;:':
        text = text.replace(' ' + p, p)
    
    for i in range(len(text)):
        if text[i] in '.!?' and i + 1 < len(text) and text[i + 1].isalpha():
            text = text[:i+1] + ' ' + text[i+1:]
    
    while '  ' in text:
        text = text.replace('  ', ' ')
    
    text = text.strip()
    sentences = []
    current = ''
    
    for char in text:
        current += char
        if char in '.!?':
            sentences.append(current.strip())
            current = ''
    if current.strip():
        sentences.append(current.strip())
    
    return ' '.join(s[0].upper() + s[1:] for s in sentences if s)


messy_text = "this is a    messy  paragraph.it has  multiple   spaces.also,the punctuation is  bad!what about this?"
print(clean_paragraph(messy_text))
print(clean_paragraph_no_regex(messy_text))

