import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

linkedin_url = 'https://www.linkedin.com/in/asifmujiburrahman'
github_url = 'https://github.com/DinoDD19'
email_addr = 'asifmujibur19@gmail.com'

# Update LinkedIn social link
html = re.sub(r'href="https://linkedin\.com/in/[^"]*"', f'href="{linkedin_url}"', html)
html = re.sub(r'href="https://www\.linkedin\.com/in/[^"]*"', f'href="{linkedin_url}"', html)

# Update GitHub social link
html = re.sub(r'href="https://github\.com/[^"]*"', f'href="{github_url}"', html)

# Ensure project "View Code" buttons point to GitHub profile (if not specific repos)
html = re.sub(r'<a href="[^"]*" class="project-btn">View Code</a>', f'<a href="{github_url}" class="project-btn">View Code</a>', html)

# Update mailto email
html = re.sub(r'href="mailto:[^"]*"', f'href="mailto:{email_addr}"', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Links updated: LinkedIn, GitHub, email, and View Code buttons.')
