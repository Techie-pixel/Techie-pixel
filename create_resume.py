"""Generate a professional resume PDF for Aditya Bokde."""
from fpdf import FPDF
import textwrap

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=20)
pdf.add_page()

# Colors
DARK = (15, 12, 41)
ACCENT = (6, 182, 212)
BLACK = (30, 30, 30)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)

# Header background
pdf.set_fill_color(*DARK)
pdf.rect(0, 0, 210, 45, 'F')

# Name
pdf.set_font('Helvetica', 'B', 26)
pdf.set_text_color(*WHITE)
pdf.set_y(8)
pdf.cell(0, 12, 'ADITYA BOKDE', align='C', new_x="LMARGIN", new_y="NEXT")

# Tagline
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*ACCENT)
pdf.cell(0, 6, 'Full-Stack Developer | Android Developer | Data Science Enthusiast', align='C', new_x="LMARGIN", new_y="NEXT")

# Contact
pdf.set_font('Helvetica', '', 8)
pdf.set_text_color(180, 180, 180)
pdf.cell(0, 5, 'bokdeaditya77@gmail.com | github.com/Techie-pixel | techie-pixel.vercel.app | India', align='C', new_x="LMARGIN", new_y="NEXT")

pdf.set_y(53)

def section(title):
    pdf.set_font('Helvetica', 'B', 12)
    pdf.set_text_color(*DARK)
    pdf.cell(0, 7, title.upper(), new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(*ACCENT)
    pdf.set_line_width(0.6)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.set_y(pdf.get_y() + 3)

def text(t):
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(*BLACK)
    lines = textwrap.wrap(t, width=100)
    for line in lines:
        pdf.cell(0, 5, line, new_x="LMARGIN", new_y="NEXT")

def item(t):
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(*BLACK)
    lines = textwrap.wrap(t, width=95)
    pdf.cell(5, 5, '>')
    pdf.cell(0, 5, lines[0], new_x="LMARGIN", new_y="NEXT")
    for line in lines[1:]:
        pdf.set_x(25)
        pdf.cell(0, 5, line, new_x="LMARGIN", new_y="NEXT")

def skill_row(label, value):
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(*ACCENT)
    pdf.cell(35, 5, label + ':')
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(*BLACK)
    # The value shouldn't wrap based on content length
    pdf.cell(0, 5, value, new_x="LMARGIN", new_y="NEXT")

# About
section('About Me')
text('Final Year Polytechnic Student specializing in Web and Mobile Application Development. Experienced in building responsive websites, backend systems, and Android applications with Firebase. Passionate about solving real-world problems through clean, maintainable code.')
pdf.set_y(pdf.get_y() + 3)

# Skills
section('Technical Skills')
skills = [
    ('Languages', 'Python, Java, JavaScript, HTML5, CSS3, C'),
    ('Mobile', 'Android (Java), Android Studio, Gradle'),
    ('Web', 'React, Next.js, Vite, Vercel, REST APIs'),
    ('Backend', 'Firebase (Auth, Firestore, Realtime DB), MySQL, Apache'),
    ('Tools', 'Git/GitHub, VS Code, Android Studio, Figma, Postman'),
    ('Learning', 'Data Science, Machine Learning, Python (Pandas, NumPy)'),
]
for label, value in skills:
    skill_row(label, value)
pdf.set_y(pdf.get_y() + 3)

# Projects
section('Projects')

pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(*DARK)
pdf.cell(0, 6, 'SmartConnect - School Management App', new_x="LMARGIN", new_y="NEXT")
pdf.set_font('Helvetica', 'I', 9)
pdf.set_text_color(*GRAY)
pdf.cell(0, 4, 'Android (Java) | Firebase | Real-time Database', new_x="LMARGIN", new_y="NEXT")
item('Comprehensive Android app with 5 role-based dashboards')
item('Real-time attendance tracking, fee management, and live chat')
item('Role-based authentication with secure access control')
pdf.set_y(pdf.get_y() + 2)

pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(*DARK)
pdf.cell(0, 6, 'Skill Gap Analyzer - AI Career Tool', new_x="LMARGIN", new_y="NEXT")
pdf.set_font('Helvetica', 'I', 9)
pdf.set_text_color(*GRAY)
pdf.cell(0, 4, 'React | Next.js | Firebase | Groq AI | Vercel', new_x="LMARGIN", new_y="NEXT")
item('Full-stack web app analyzing skills against job market using AI')
item('Integrated Groq AI for personalized learning roadmap generation')
item('Google and GitHub OAuth authentication with Firebase')
pdf.set_y(pdf.get_y() + 2)

pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(*DARK)
pdf.cell(0, 6, 'Portfolio Website - Personal Brand', new_x="LMARGIN", new_y="NEXT")
pdf.set_font('Helvetica', 'I', 9)
pdf.set_text_color(*GRAY)
pdf.cell(0, 4, 'React | Vite | CSS3 | Vercel', new_x="LMARGIN", new_y="NEXT")
item('Cinematic portfolio with scroll-linked hero animation')
item('Responsive design with premium dark theme and animations')
item('Deployed on Vercel: techie-pixel.vercel.app')
pdf.set_y(pdf.get_y() + 3)

# Education
section('Education')
pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(*DARK)
pdf.cell(0, 6, 'Diploma in Computer Engineering', new_x="LMARGIN", new_y="NEXT")
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*GRAY)
pdf.cell(0, 5, 'Final Year | Polytechnic | India', new_x="LMARGIN", new_y="NEXT")
pdf.set_y(pdf.get_y() + 3)

# Links
section('Links')
links = [
    ('GitHub', 'github.com/Techie-pixel'),
    ('Portfolio', 'techie-pixel.vercel.app'),
    ('LinkedIn', 'linkedin.com/in/aditya-bokde-b87a703b8'),
    ('Email', 'bokdeaditya77@gmail.com'),
]
for label, url in links:
    skill_row(label, url)

pdf.output('assets/Aditya_Bokde_Resume.pdf')
print("Resume generated successfully!")
