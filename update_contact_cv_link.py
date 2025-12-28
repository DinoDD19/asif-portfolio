import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

cv_anchor = (
    '                <a href="assets/Asif_Mujibur_Rahman_CV.pdf" target="_blank" class="social-link" download>\n'
    '                    <span class="social-icon">📄</span>\n'
    '                    <span>Download CV</span>\n'
    '                </a>\n'
)

# Insert CV link inside the social-links div (after opening tag)
html = re.sub(r'(\<div class=\"social-links\"\>\s*)', r"\\1" + cv_anchor, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Contact section updated with CV download link.')
