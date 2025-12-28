import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

achievements_section = '''
      <!-- ============================================
           ACHIEVEMENTS SECTION
      ============================================ -->
      <section id="achievements" class="reveal" style="padding: 5rem 2rem;">
          <h2 class="section-title">Achievements</h2>
          <p class="section-subtitle">Highlights and awards</p>
          <div class="skills-grid" style="margin-top: 2rem;">
              <div class="skill-card">
                  <div class="skill-icon">🏆</div>
                  <h3 class="skill-name">Toastmasters</h3>
                  <p class="skill-level">Winner</p>
                  <p style="color: var(--text-secondary); margin-top: 0.5rem; font-size: 0.9rem;">Participated and won in Toastmasters competition</p>
              </div>
              <div class="skill-card">
                  <div class="skill-icon">⭐</div>
                  <h3 class="skill-name">Derek'O Brien Quiz</h3>
                  <p class="skill-level">National Level</p>
                  <p style="color: var(--text-secondary); margin-top: 0.5rem; font-size: 0.9rem;">Participated in National Level Quiz Competition</p>
              </div>
              <div class="skill-card">
                  <div class="skill-icon">🏅</div>
                  <h3 class="skill-name">Sastra Pratibha Contest</h3>
                  <p class="skill-level">Participant</p>
                  <p style="color: var(--text-secondary); margin-top: 0.5rem; font-size: 0.9rem;">Participated in Sastra Pratibha Contest</p>
              </div>
              <div class="skill-card">
                  <div class="skill-icon">🎖️</div>
                  <h3 class="skill-name">AskItians Quiz</h3>
                  <p class="skill-level">Participant</p>
                  <p style="color: var(--text-secondary); margin-top: 0.5rem; font-size: 0.9rem;">Participated in AskItians Quiz Competition</p>
              </div>
          </div>
      </section>

'''

certifications_section = '''
      <!-- ============================================
           CERTIFICATIONS SECTION
      ============================================ -->
      <section id="certifications" class="reveal" style="padding: 5rem 2rem; background: var(--bg-secondary);">
          <h2 class="section-title">Certifications</h2>
          <p class="section-subtitle">Courses and credentials</p>
          <div class="skills-grid" style="margin-top: 2rem;">
              <div class="skill-card">
                  <div class="skill-icon">🎓</div>
                  <h3 class="skill-name">Internet of Things</h3>
                  <p class="skill-level">NPTEL — Elite Silver</p>
              </div>
              <div class="skill-card">
                  <div class="skill-icon">🎓</div>
                  <h3 class="skill-name">Python for Data Science</h3>
                  <p class="skill-level">NPTEL — Elite</p>
              </div>
              <div class="skill-card">
                  <div class="skill-icon">🎓</div>
                  <h3 class="skill-name">Cloud Computing</h3>
                  <p class="skill-level">NPTEL — Elite</p>
              </div>
              <div class="skill-card">
                  <div class="skill-icon">📜</div>
                  <h3 class="skill-name">Digital 101</h3>
                  <p class="skill-level">futureskills-prime</p>
              </div>
              <div class="skill-card">
                  <div class="skill-icon">📜</div>
                  <h3 class="skill-name">Data Analyst</h3>
                  <p class="skill-level">Coursera</p>
              </div>
          </div>
      </section>

'''

# Insert before CONTACT SECTION marker
contact_marker = '<!-- ============================================\n           CONTACT SECTION\n      ============================================ -->'
if contact_marker in html:
    html = html.replace(contact_marker, achievements_section + certifications_section + '      ' + contact_marker)

# Update navbar if not already present
if '#achievements' not in html:
    html = html.replace(
        '<li><a href="#projects">Projects</a></li>\n                  <li><a href="#contact">Contact</a></li>',
        '<li><a href="#projects">Projects</a></li>\n                  <li><a href="#achievements">Achievements</a></li>\n                  <li><a href="#certifications">Certifications</a></li>\n                  <li><a href="#contact">Contact</a></li>'
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Added Achievements and Certifications sections.')
