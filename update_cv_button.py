import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

cv_href = 'assets/Asif_Mujibur_Rahman_CV.pdf'
cv_button = f'\n                  <a href="{cv_href}" class="btn btn-secondary" target="_blank" rel="noopener" download>Download CV</a>'

# Insert button into hero CTA buttons
html = re.sub(r'(\<div class=\"cta-buttons\"\>\s*.*?)(\</div\>)', lambda m: m.group(1) + cv_button + '\n' + m.group(2), html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Added Download CV button in hero section.')
