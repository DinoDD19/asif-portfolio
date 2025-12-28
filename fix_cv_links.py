import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1) Remove any stray literal \1 near contact area
html = re.sub(r'(<!--\s*Social\s*Links\s*-->)([^<]*)\\1([^<]*)', r'\1', html)  # guard in case of duplicated markers
html = re.sub(r'\s*\\1\s*', '', html)  # remove any visible \1

# 2) Normalize Contact CV link: remove target, set download filename
html = re.sub(
    r'<a\s+href="assets/Asif_Mujibur_Rahman_CV\.pdf"[^>]*class="social-link"[^>]*>',
    '<a href="assets/Asif_Mujibur_Rahman_CV.pdf" class="social-link" download="Asif_Mujibur_Rahman_CV.pdf">',
    html
)

# 3) Normalize Hero CV button: remove target/rel and set download filename
html = re.sub(
    r'<a\s+href="assets/Asif_Mujibur_Rahman_CV\.pdf"[^>]*class="btn btn-secondary"[^>]*>(\s*Download CV\s*)</a>',
    '<a href="assets/Asif_Mujibur_Rahman_CV.pdf" class="btn btn-secondary" download="Asif_Mujibur_Rahman_CV.pdf">Download CV</a>',
    html,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Cleaned up stray \\1 and enforced proper CV download attributes.')
