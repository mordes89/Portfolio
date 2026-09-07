from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
out=Path('output/pdf/Mike-Schnall-Resume.pdf')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='NameX',fontName='Helvetica-Bold',fontSize=21,leading=23,textColor=HexColor('#122b30'),spaceAfter=3))
styles.add(ParagraphStyle(name='SubX',fontName='Helvetica',fontSize=10.5,leading=13,textColor=HexColor('#333333'),spaceAfter=3))
styles.add(ParagraphStyle(name='BodyX',fontName='Helvetica',fontSize=10.5,leading=13,spaceAfter=4))
styles.add(ParagraphStyle(name='HeadX',fontName='Helvetica-Bold',fontSize=13,leading=18,textColor=HexColor('#a64d79'),spaceBefore=8,spaceAfter=7,keepWithNext=True))
styles.add(ParagraphStyle(name='RoleX',fontName='Helvetica-Bold',fontSize=10.7,leading=14,spaceBefore=5,spaceAfter=2,keepWithNext=True))
styles.add(ParagraphStyle(name='MetaX',fontName='Helvetica',fontSize=9.5,leading=13,textColor=HexColor('#556267'),spaceAfter=5,keepWithNext=True))
styles.add(ParagraphStyle(name='BulletX',parent=styles['BodyX'],leftIndent=12,firstLineIndent=-10,spaceAfter=4))
class SectionHeading(Paragraph):
 def draw(self):
  super().draw()
  self.canv.saveState()
  self.canv.setStrokeColor(HexColor('#a64d79'))
  self.canv.setLineWidth(0.8)
  self.canv.line(0,-2,self.width,-2)
  self.canv.restoreState()
story=[]
def p(t,sty='BodyX'): story.append((SectionHeading if sty=='HeadX' else Paragraph)(t,styles[sty]))
def bullet(t): p('&#8226; '+t,'BulletX')
def role(t,meta): p(t,'RoleX');p(meta,'MetaX')
p('<font color="#a64d79">Mike</font> <font color="#e69138">Schnall</font>','NameX')
p('Senior Solutions Engineer | Software Engineer','SubX')
p('New York City, NY | 682-365-1263 | <link href="mailto:MMSchnall@gmail.com" color="#1155cc"><u>MMSchnall@gmail.com</u></link>','MetaX')
p('<link href="https://www.linkedin.com/in/mike-mordechai-schnall/" color="#1155cc"><u>LinkedIn</u></link> &#8226; <link href="https://github.com/mordes89" color="#1155cc"><u>GitHub</u></link> &#8226; <link href="https://mordes89.github.io/Mike-Schnall-portfolio/" color="#1155cc"><u>Portfolio</u></link>','MetaX')
p('Senior Solutions Engineer connecting enterprise clients to machine learning verification products through API integrations, data analysis, and technical onboarding.')
p('Experience','HeadX')
role('Informed.IQ | Senior Solutions Engineer','Apr 2022 - Present')
for t in [
'Lead enterprise onboarding and integrations, translating client requirements into implementation plans.',
'Diagnose complex integration issues, identify root causes, and explain technical concepts to technical and nontechnical stakeholders.',
'Develop utility scripts and analyze client and system activity to identify integration gaps and optimize partner APIs.',
'Architect and implement methodologies that eliminate more than 300,000 lines of legacy code.',
'Partner with engineering, product, and customer success to bring client feedback into product planning.',
'Create documentation and training materials to support client adoption.'
]: bullet(t)
role('Get PEYD, LLC | Database Manager and Bookkeeper','May 2015 - Jun 2021 | Inwood, NY')
for t in ['Built the company database and automated data collection and financial reporting, reducing manual labor by more than 40%.','Created custom reports and collected data for marketing campaigns.','Trained and supervised the onboarding of new hires, incorporating them into team workflows.']:bullet(t)
role('Hapoel Jerusalem Basketball Club | Sports Equipment Manager','Aug 2010 - Jul 2011 | Jerusalem, Israel')
p('Managed inventory and international travel logistics, reducing equipment misplacement and theft by more than 70%.')
role('Israel Defense Forces | Infantry Soldier','Jul 2007 - Jul 2010 | Israel')
p('Led teams in military operations. Awarded Exemplary Infantryman in advanced training; highest rank held was Staff Sergeant.')
p('Skills','HeadX')
p('<b>Engineering:</b> Python, JavaScript, Ruby on Rails, React, Redux, Node.js, Express.js, HTML, CSS, Sass, Git, Webpack, jQuery.')
p('<b>Data and cloud:</b> AWS, SQL, PostgreSQL, SQLite, MongoDB, Mongoose, API integrations, data analysis, automation.')
p('Education and Languages','HeadX')
p('<b>App Academy</b> | Full Stack Web Development Bootcamp | Jun - Oct 2021')
p('<b>Queens College, CUNY</b> | BA, Economics | 2020<br/>Magna cum laude, GPA 3.878; National Society of Collegiate Scholars member.')
p('<b>Languages:</b> English and Hebrew (fluent).')
SimpleDocTemplate(str(out),pagesize=A4,rightMargin=32,leftMargin=32,topMargin=24,bottomMargin=28,title='Mike Schnall Resume',author='Mike Schnall').build(story)
print(out.resolve())

