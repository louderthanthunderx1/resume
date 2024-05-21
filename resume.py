from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Theeraphan Sukchok', 0, 1, 'C')
        # self.set_font('Arial', 'I', 10)
        # self.cell(0, 10, 'Data Scientist', 0, 1, 'C')
        self.set_font('Arial', '', 10)
        self.cell(0, 10, 'Phone: 082-107-6614 | Email: Theeraphan.sukchok@gmail.com | LinkedIn: Theeraphan-Sukchok', 0, 1, 'C')
        self.ln(2)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 11)
        self.cell(0, 7, title, 0, 1, 'L')
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(2)

    def chapter_body(self, body):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 5, body)
        self.ln(2)

    def add_experience(self, title, company, dates, details):
        self.set_font('Arial', 'B', 10)
        self.cell(0, 6, title, 0, 1)
        self.set_font('Arial', 'I', 10)
        self.cell(0, 6, company, 0, 0)
        self.cell(0, 6, dates, 0, 1, 'R')
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 5, details)
        self.ln(2)

    def add_education(self, institution, dates, degree):
        self.set_font('Arial', 'B', 10)
        self.cell(0, 6, institution, 0, 0)
        self.set_font('Arial', 'I', 10)
        self.cell(0, 6, dates, 0, 1, 'R')
        self.set_font('Arial', '', 10)
        self.cell(0, 6, degree, 0, 1)
        self.ln(2)


    def add_skills(self, technical_skills):
        self.set_font('Arial', 'B', 11)
        self.cell(0, 7, 'SKILLS', 0, 1, 'L')
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(2)
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 5, technical_skills)
        self.ln(2)

    def add_certifications(self, certifications):
        self.set_font('Arial', 'B', 11)
        self.cell(0, 7, 'CERTIFICATIONS', 0, 1, 'L')
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(2)
        self.set_font('Arial', '', 10)
        self.multi_cell(200, 5, certifications)
        self.ln(2)

    def add_languages(self, languages):
        # Adjust the X and Y position to align with the certification title
        self.set_font('Arial', 'B', 11)
        self.cell(0, 7, 'LANGUAGES', 0, 1, 'L')
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(2)
        self.set_font('Arial', '', 10)
        self.multi_cell(85, 5, languages)
        self.ln(2)

    


def create_resume():
    pdf = PDF()
    pdf.add_page()

    # Professional Experience
    pdf.chapter_title('PROFESSIONAL EXPERIENCE')
    pdf.add_experience(
        'Data Scientist',
        'TSPACE Digital, Bangkok, Thailand',
        'July 2022 - Present',
        ('- Led computer vision project with 90% accuracy using CNN and PyTorch, enhancing product detection.\n'
         '- Developed and deployed AI models, improving efficiency by using MLOps\n   (Flask, Docker, Grafana, DVC, MLflow, Vector Database(Milvus)).\n'
         '- Optimized AI models for mobile apps, improving inference speed by 50% and real-time detection.\n'
         '- Streamlined data collection processes for fieldwork, reducing data collection time by 4x.\n'
         '- Enhanced data-driven decision-making through Python algorithms and SQL, increasing business performance.'
        )
    )
    pdf.add_experience(
        'Administrative Officer',
        'T-Power Up Fitness, Rayong, Thailand',
        'January 2021 - January 2022',
        ('- Managed training plans, boosting operational efficiency.\n'
         '- Led digital marketing campaigns, increasing client engagement.')
    )
    pdf.add_experience(
        'Production Operator',
        'Suruga (Thailand) Co., Ltd, Rayong, Thailand',
        'May 2014 - January 2021',
        ('- Improved production processes, reducing defects and increasing quality control.')
    )

    # Education
    pdf.chapter_title('EDUCATION')
    # pdf.add_education(
    #     'University of Illinois Urbana-Champaign',
    #     '2024 - Present',
    #     'Master\'s Degree Computer Science in Data Science'
    # )
    pdf.add_education(
        'Rajamangala University of Technology Tawan-ok',
        '2020 - 2022',
        'Bachelor\'s Degree in Engineering (Mechatronic and Robotics Engineer) GPA: 3.25/4.00'
    )
    pdf.add_education(
        'Rayong Technical College',
        '2012 - 2014',
        'Higher Diploma in Industrial Electronics'
    )

    # Skills
    technical_skills = (
        'General Skills:\n'
        '- Strong analytical and problem-solving abilities.\n'
        '- Effective in team collaboration and project management.\n'
        'Technical Skills:\n'
        '- Programming Languages: Python, SQL\n'
        '- AI/ML: Scikit-Learn, PyTorch, TensorFlow, Keras, HuggingFace, LLMs(GPT4/llama2), RAG, Transformer Models\n'
        '- Data Visualization: Power BI, Matplotlib, Seaborn\n'
        '- Databases: PostgreSQL, SQL Server\n'
        '- Other Tools: Git, GitHub, Postman, VScode, DBeaver, Excel, Power Point\n'
    )
    pdf.add_skills(technical_skills)

    # Certifications
    pdf.add_certifications(
        'Coursera: Deep Learning Specialization (2023)\n'
        'Udemy: PyTorch for Deep Learning (2023)\n'
        'Udemy: Complete Machine Learning & Data Science (2022)\n'
        'Udemy: Data Science A-Z: Real-Life Data Science (2021)\n'
    )

    # Languages
    pdf.add_languages(
        'Thai (Native)\n'
        'English (Intermediate)\n'
    )

    pdf.output('Theeraphan_Sukchok_Resume.pdf')

if __name__ == "__main__":
    create_resume()
