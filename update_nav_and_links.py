with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update navbar
old_nav = '''<ul class="nav-links" id="navLinks">
                  <li><a href="#home">Home</a></li>
                  <li><a href="#about">About</a></li>
                  <li><a href="#skills">Skills</a></li>
                  <li><a href="#projects">Projects</a></li>
                  <li><a href="#contact">Contact</a></li>
              </ul>'''

new_nav = '''<ul class="nav-links" id="navLinks">
                  <li><a href="#home">Home</a></li>
                  <li><a href="#about">About</a></li>
                  <li><a href="#skills">Skills</a></li>
                  <li><a href="#projects">Projects</a></li>
                  <li><a href="#achievements">Achievements</a></li>
                  <li><a href="#certifications">Certifications</a></li>
                  <li><a href="#contact">Contact</a></li>
              </ul>'''

html = html.replace(old_nav, new_nav)

# 2. Add links to each achievement card
achievements_with_links = {
    'Toastmasters': 'https://www.toastmasters.org/',
    "Derek'O Brien Quiz": 'https://www.derekobrien.com/',
    'Sastra Pratibha Contest': '#',
    'AskItians Quiz': 'https://www.askiitians.com/'
}

for name, link in achievements_with_links.items():
    # Find each achievement and add a link button
    pattern = f'<h3 class="skill-name">{name}</h3>'
    if pattern in html:
        # Add button after the description
        old = f'''<h3 class="skill-name">{name}</h3>
 <p class="skill-level">'''
        new = f'''<h3 class="skill-name">{name}</h3>
 <a href="{link}" target="_blank" class="project-btn" style="display: inline-block; margin-top: 1rem; padding: 0.5rem 1rem; font-size: 0.85rem;">View Details</a>
 <p class="skill-level" style="margin-top: 0.5rem;">'''
        html = html.replace(old, new)

# 3. Add links to certifications
cert_links = {
    'Internet of Things': 'https://nptel.ac.in/courses/106105166',
    'Python for Data Science': 'https://nptel.ac.in/courses/106106145',
    'Cloud Computing': 'https://nptel.ac.in/courses/106105167',
    'Digital 101': 'https://futureskillsprime.in/',
    'Data Analyst': 'https://www.coursera.org/professional-certificates/google-data-analytics'
}

for name, link in cert_links.items():
    pattern = f'<h3 class="skill-name">{name}</h3>'
    if pattern in html:
        old = f'''<h3 class="skill-name">{name}</h3>
 <p class="skill-level">'''
        new = f'''<h3 class="skill-name">{name}</h3>
 <a href="{link}" target="_blank" class="project-btn" style="display: inline-block; margin-top: 1rem; padding: 0.5rem 1rem; font-size: 0.85rem;">View Certificate</a>
 <p class="skill-level" style="margin-top: 0.5rem;">'''
        html = html.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('✅ Updated navbar and added links to achievements and certifications')
