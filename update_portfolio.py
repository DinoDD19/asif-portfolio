import re

# Read the current HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Update Hero Section - Full name
html_content = html_content.replace(
    '<h1>Asif</h1>',
    '<h1>Asif Mujibur Rahman</h1>'
)

html_content = html_content.replace(
    '<h2>Aspiring AI Engineer</h2>',
    '<h2>AI & ML Engineer | Computer Science Student</h2>'
)

html_content = html_content.replace(
    '<p>Building intelligent, data-driven solutions with AI</p>',
    '<p>3rd Year B.E. Student at St. Joseph\'s College of Engineering | Building AI solutions for real-world problems</p>'
)

# Update About Section
old_about = r'<div class="about-content">.*?</div>\s*</section>\s*<!-- ============================================\s*SKILLS SECTION'
new_about = '''<div class="about-content">
              <p>
                  Hello! I'm <span class="highlight">Asif Mujibur Rahman</span>, a passionate Computer Science and Artificial Intelligence student     
                  currently pursuing my 3rd year B.E. in Computer Science & Engineering at <span class="highlight">St. Joseph's College of Engineering</span>, Chennai, India.
              </p>
              <p>
                  My career objective is to secure a challenging position where I can efficiently contribute my skills and abilities 
                  to the growth of the organization while building my professional career. I am eager to learn the maximum about every 
                  domain I am involved in, not just a little, and continuously expand my knowledge and experience.
              </p>
              <p>
                  I have completed multiple internships including <span class="highlight">Python Development at CODSOFT</span>, 
                  <span class="highlight">Web Development at Prodigy Infotech</span>, and <span class="highlight">Software Debugging at ES Technocorp</span>. 
                  My interests include Generative AI & NLP, Agentic AI Frameworks, Deep Learning and LLMs, and Quantum Mechanics.
              </p>
              <p>
                  Born in the Kingdom of Bahrain and fluent in Tamil, English, and Hindi, I bring a diverse perspective to my work. 
                  Beyond technical skills, I'm proficient in Microsoft Office, project management, AI tools, and possess effective communication skills.
              </p>
          </div>
      </section>

      <!-- ============================================
           SKILLS SECTION'''

html_content = re.sub(old_about, new_about, html_content, flags=re.DOTALL)

# Update Skills Section
old_skills = r'<div class="skills-grid">.*?</div>\s*</section>\s*<!-- ============================================\s*PROJECTS SECTION'
new_skills = '''<div class="skills-grid">
              <div class="skill-card">
                  <div class="skill-icon">🐍</div>
                  <h3 class="skill-name">Python</h3>
                  <p class="skill-level">Advanced</p>
                  <div class="skill-progress">
                      <div class="skill-progress-bar" data-progress="90"></div>
                  </div>
              </div>
              <div class="skill-card">
                  <div class="skill-icon">🤖</div>
                  <h3 class="skill-name">AI & ML Engineering</h3>
                  <p class="skill-level">Advanced</p>
                  <div class="skill-progress">
                      <div class="skill-progress-bar" data-progress="85"></div>
                  </div>
              </div>
              <div class="skill-card">
                  <div class="skill-icon">🗄️</div>
                  <h3 class="skill-name">Database Management</h3>
                  <p class="skill-level">Intermediate</p>
                  <div class="skill-progress">
                      <div class="skill-progress-bar" data-progress="75"></div>
                  </div>
              </div>
              <div class="skill-card">
                  <div class="skill-icon">💻</div>
                  <h3 class="skill-name">Fullstack Development</h3>
                  <p class="skill-level">Intermediate</p>
                  <div class="skill-progress">
                      <div class="skill-progress-bar" data-progress="80"></div>
                  </div>
              </div>
              <div class="skill-card">
                  <div class="skill-icon">📊</div>
                  <h3 class="skill-name">Tableau & PowerBI</h3>
                  <p class="skill-level">Intermediate</p>
                  <div class="skill-progress">
                      <div class="skill-progress-bar" data-progress="70"></div>
                  </div>
              </div>
              <div class="skill-card">
                  <div class="skill-icon">🧠</div>
                  <h3 class="skill-name">Deep Learning & LLMs</h3>
                  <p class="skill-level">Advanced</p>
                  <div class="skill-progress">
                      <div class="skill-progress-bar" data-progress="85"></div>
                  </div>
              </div>
              <div class="skill-card">
                  <div class="skill-icon">💬</div>
                  <h3 class="skill-name">NLP & Generative AI</h3>
                  <p class="skill-level">Advanced</p>
                  <div class="skill-progress">
                      <div class="skill-progress-bar" data-progress="80"></div>
                  </div>
              </div>
              <div class="skill-card">
                  <div class="skill-icon">⚛️</div>
                  <h3 class="skill-name">React</h3>
                  <p class="skill-level">Intermediate</p>
                  <div class="skill-progress">
                      <div class="skill-progress-bar" data-progress="75"></div>
                  </div>
              </div>
          </div>
      </section>

      <!-- ============================================
           PROJECTS SECTION'''

html_content = re.sub(old_skills, new_skills, html_content, flags=re.DOTALL)

# Update Projects Section with real projects
old_projects = r'<div class="projects-grid">.*?</div>\s*</section>\s*<!-- ============================================\s*CONTACT SECTION'
new_projects = '''<div class="projects-grid">
              <!-- Project 1 -->
              <div class="project-card">
                  <div class="project-image">🚨</div>
                  <div class="project-content">
                      <h3 class="project-title">Disaster Management System</h3>
                      <p class="project-description">
                          An innovative disaster management system designed to work without internet connectivity.
                          Enables emergency response coordination in areas with network disruptions.
                      </p>
                      <div class="project-tech">
                          <span class="tech-tag">Python</span>
                          <span class="tech-tag">Offline-First</span>
                          <span class="tech-tag">IoT</span>
                      </div>
                      <div class="project-links">
                          <a href="https://github.com/DinoDD19" class="project-btn">View Code</a>
                      </div>
                  </div>
              </div>

              <!-- Project 2 -->
              <div class="project-card">
                  <div class="project-image">🎓</div>
                  <div class="project-content">
                      <h3 class="project-title">Mindure</h3>
                      <p class="project-description">
                          An AI-integrated platform designed to help students with career planning and guidance.
                          Uses machine learning to provide personalized career recommendations.
                      </p>
                      <div class="project-tech">
                          <span class="tech-tag">Python</span>
                          <span class="tech-tag">AI/ML</span>
                          <span class="tech-tag">Web Development</span>
                      </div>
                      <div class="project-links">
                          <a href="https://github.com/DinoDD19" class="project-btn">View Code</a>
                      </div>
                  </div>
              </div>

              <!-- Project 3 -->
              <div class="project-card">
                  <div class="project-image">🌱</div>
                  <div class="project-content">
                      <h3 class="project-title">PlantDoc</h3>
                      <p class="project-description">
                          A machine learning-based prediction model and platform for plant disease diagnosis.
                          Helps farmers identify plant diseases early and take preventive measures.
                      </p>
                      <div class="project-tech">
                          <span class="tech-tag">Python</span>
                          <span class="tech-tag">Machine Learning</span>
                          <span class="tech-tag">Computer Vision</span>
                      </div>
                      <div class="project-links">
                          <a href="https://github.com/DinoDD19" class="project-btn">View Code</a>
                      </div>
                  </div>
              </div>

              <!-- Project 4 -->
              <div class="project-card">
                  <div class="project-image">🏥</div>
                  <div class="project-content">
                      <h3 class="project-title">DocAI</h3>
                      <p class="project-description">
                          An AI-based appointment reservation system for hospitals that streamlines
                          patient scheduling and optimizes doctor availability.
                      </p>
                      <div class="project-tech">
                          <span class="tech-tag">Python</span>
                          <span class="tech-tag">AI</span>
                          <span class="tech-tag">Healthcare Tech</span>
                      </div>
                      <div class="project-links">
                          <a href="https://github.com/DinoDD19" class="project-btn">View Code</a>
                      </div>
                  </div>
              </div>
          </div>
      </section>

      <!-- ============================================
           CONTACT SECTION'''

html_content = re.sub(old_projects, new_projects, html_content, flags=re.DOTALL)

# Update Contact Section
html_content = re.sub(
    r'<p>Feel free to reach out for collaborations or just a friendly chat!</p>',
    '<p>Feel free to reach out for collaborations, opportunities, or just a friendly chat!</p>',
    html_content
)

# Update GitHub link
html_content = html_content.replace(
    'href="#"',
    'href="https://github.com/DinoDD19"',
    1  # Only first occurrence in social links
)

# Update LinkedIn
html_content = re.sub(
    r'<a href="#" class="social-link" aria-label="LinkedIn">',
    '<a href="https://www.linkedin.com/in/asif-mujibur-rahman" class="social-link" aria-label="LinkedIn">',
    html_content
)

# Update email placeholder in form
html_content = re.sub(
    r'placeholder="your\.email@example\.com"',
    'placeholder="asifmujibur19@gmail.com"',
    html_content
)

# Add Work Experience section after Skills and before Projects
experience_section = '''
      <!-- ============================================
           WORK EXPERIENCE SECTION
      ============================================ -->
      <section id="experience" class="reveal" style="padding: 5rem 2rem; background: var(--bg-secondary);">
          <h2 class="section-title">Work Experience & Internships</h2>
          <p class="section-subtitle">Professional journey and hands-on experience</p>
          <div style="max-width: 1000px; margin: 0 auto;">
              <!-- Experience Timeline -->
              <div style="display: grid; gap: 2rem; margin-top: 3rem;">
                  <!-- Experience 1 -->
                  <div class="skill-card" style="text-align: left; padding: 2rem;">
                      <h3 style="color: var(--accent-primary); margin-bottom: 0.5rem;">Software Debugging Intern</h3>
                      <p style="color: var(--text-secondary); margin-bottom: 0.5rem;">ES Technocorp W.L.L | Riffa, Manama</p>
                      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem;">June 2025 - July 2025</p>
                      <p>Created small projects using React and learned software debugging and testing methodologies at company scale.</p>
                  </div>
                  
                  <!-- Experience 2 -->
                  <div class="skill-card" style="text-align: left; padding: 2rem;">
                      <h3 style="color: var(--accent-primary); margin-bottom: 0.5rem;">Web Development Intern</h3>
                      <p style="color: var(--text-secondary); margin-bottom: 0.5rem;">Prodigy Infotech W.L.L | Mumbai, India (Remote)</p>
                      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem;">September 2024 - October 2024</p>
                      <p>Created small projects and learned to use web development at company level, gaining practical experience in full-stack development.</p>
                  </div>
                  
                  <!-- Experience 3 -->
                  <div class="skill-card" style="text-align: left; padding: 2rem;">
                      <h3 style="color: var(--accent-primary); margin-bottom: 0.5rem;">Python Development Intern</h3>
                      <p style="color: var(--text-secondary); margin-bottom: 0.5rem;">CODSOFT W.L.L | Kolkata, India (Remote)</p>
                      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem;">August 2024 - September 2024</p>
                      <p>Created small projects and learned to use Python at company scale, developing practical programming skills.</p>
                  </div>
                  
                  <!-- Experience 4 -->
                  <div class="skill-card" style="text-align: left; padding: 2rem;">
                      <h3 style="color: var(--accent-primary); margin-bottom: 0.5rem;">Accounts Assistant</h3>
                      <p style="color: var(--text-secondary); margin-bottom: 0.5rem;">Food City W.L.L | Kingdom of Bahrain</p>
                      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem;">March 2023 - April 2023</p>
                      <p>Assisted in improving financial efficiency and accounts outcomes during school break.</p>
                  </div>
                  
                  <!-- Experience 5 -->
                  <div class="skill-card" style="text-align: left; padding: 2rem;">
                      <h3 style="color: var(--accent-primary); margin-bottom: 0.5rem;">CNC Operator</h3>
                      <p style="color: var(--text-secondary); margin-bottom: 0.5rem;">Fluid Tech W.L.L | Riffa, Kingdom of Bahrain</p>
                      <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem;">July 2021 - August 2021</p>
                      <p>Learned how to make hydraulic and pneumatic seals and operate CNC machinery during school break.</p>
                  </div>
              </div>
          </div>
      </section>

'''

# Insert experience section before projects
html_content = html_content.replace(
    '<!-- ============================================\n           PROJECTS SECTION\n      ============================================ -->',
    experience_section + '      <!-- ============================================\n           PROJECTS SECTION\n      ============================================ -->'
)

# Update navigation to include Experience
html_content = html_content.replace(
    '<li><a href="#skills">Skills</a></li>\n                  <li><a href="#projects">Projects</a></li>',
    '<li><a href="#skills">Skills</a></li>\n                  <li><a href="#experience">Experience</a></li>\n                  <li><a href="#projects">Projects</a></li>'
)

# Write the updated HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Portfolio updated successfully with CV information!")
print("Updated sections:")
print("  ✓ Hero section with full name")
print("  ✓ About section with education and career objective")
print("  ✓ Skills section with real technical skills")
print("  ✓ Projects section with actual projects")
print("  ✓ Added Work Experience section with all internships")
print("  ✓ Updated contact links (GitHub, LinkedIn)")
