import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove all instances of literal \1 including with surrounding whitespace
content = content.replace('\\1', '')
content = re.sub(r'\s+\\1\s+', ' ', content)
content = re.sub(r'\\1\s+', '', content)
content = re.sub(r'\s+\\1', '', content)

# Clean up any double spaces that might result
content = re.sub(r'  +', ' ', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Removed all instances of \\1')
