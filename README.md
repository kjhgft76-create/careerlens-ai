# 🎯 CareerLens AI

### NLP-Based Resume–Job Compatibility Analyzer

CareerLens AI is a web-based application that analyzes a candidate's resume against a target job description and provides an interpretable compatibility score.

The application extracts technical skills from the resume and job description, identifies matched and missing skills, and calculates text similarity using TF-IDF and Cosine Similarity.

---

## 🚀 Live Demo

🔗 **Live Application:**  
https://careerlens-ai01.streamlit.app/

🔗 **GitHub Repository:**  
https://github.com/kjhgft76-create/careerlens-ai

---

## 📌 Project Overview

Matching a resume with a job description manually can be time-consuming, especially when a job description contains many technical requirements.

CareerLens AI simplifies this process by automatically comparing the resume with the target job description and presenting the results in an easy-to-understand format.

The system focuses on two major factors:

- Technical skill alignment
- Textual similarity between the resume and job description

The final result is presented through an interactive Streamlit interface.

---

## ✨ Features

- 📄 Upload resumes in PDF format
- 🔍 Extract text from PDF resumes using PyMuPDF
- 🧠 Detect technical skills from resume and job description
- 🔄 Normalize common skill aliases
- ✅ Identify matched skills
- ❌ Identify missing skills
- 📊 Calculate skill-match percentage
- 📝 Calculate resume–job text similarity
- 📐 TF-IDF based text vectorization
- 📏 Cosine Similarity based comparison
- 🎯 Calculate an overall compatibility score
- 💻 Interactive Streamlit interface
- 🧪 Automated tests using pytest
- ☁️ Deployed as a web application

---

## 🔄 How It Works

The application follows this processing pipeline:

```text
Resume PDF
     │
     ▼
PDF Text Extraction
     │
     ▼
Text Normalization
     │
     ▼
Technical Skill Extraction
     │
     ├───────────────┐
     ▼               ▼
Resume Skills    Job Skills
     │               │
     └───────┬───────┘
             ▼
       Skill Matching
             │
             ▼
     Matched / Missing Skills
             
Resume Text + Job Description
             │
             ▼
      TF-IDF Vectorization
             │
             ▼
      Cosine Similarity
             │
             ▼
       Text Similarity
             │
             ▼
      Weighted Scoring
             │
             ▼
    Compatibility Report
🏗️ System Architecture

CareerLens AI is organized into separate components for the user interface, document processing, and analysis logic.

1. Presentation Layer

Streamlit

Responsible for:

Resume upload
Job description input
Analysis button
Displaying compatibility score
Displaying matched skills
Displaying missing skills
Displaying resume and job skills
Presenting analysis results
2. Document Processing Layer

PyMuPDF

Responsible for:

Opening PDF documents
Extracting text from each page
Combining extracted text
Normalizing unnecessary whitespace
Handling PDF extraction errors
3. Analysis Layer

Python + scikit-learn

Responsible for:

Skill extraction
Skill alias normalization
Skill matching
TF-IDF vectorization
Cosine similarity calculation
Compatibility score calculation
🧠 Analysis Methodology

CareerLens AI uses two major components to calculate the final compatibility score.

Skill Alignment — 70%

The system extracts technical skills from both the resume and job description.

It then identifies:

Matched skills
Missing skills
Resume skills
Job-required skills

The skill-match score is calculated as:

Skill Match =
(Matched Job Skills / Total Job Skills) × 100
Text Similarity — 30%

The application uses TF-IDF (Term Frequency–Inverse Document Frequency) to convert the resume and job description into numerical representations.

Cosine Similarity is then used to measure the similarity between these representations.

Text Similarity =
Cosine Similarity between Resume and Job Description

The similarity value is converted into a percentage.

🎯 Overall Compatibility Score

The final compatibility score is calculated using a weighted combination of skill alignment and text similarity.

Overall Score =
(Skill Match × 0.70) + (Text Similarity × 0.30)

This gives greater importance to technical skill alignment while still considering the overall textual similarity between the resume and job description.

🔍 Skill Detection

CareerLens AI uses a predefined skill taxonomy containing technical skills and their commonly used aliases.

For example:

Python
python3

JavaScript
JS

React
ReactJS
React.js

Scikit-learn
sklearn

PostgreSQL
Postgres

These aliases are normalized to a common canonical skill name before comparison.

This helps prevent the same technology from being treated as different skills simply because it is written differently.

🛠️ Technology Stack
Technology	Purpose
Python	Core programming language
Streamlit	Web application interface
PyMuPDF	PDF text extraction
scikit-learn	NLP/ML processing
TF-IDF	Text vectorization
Cosine Similarity	Text similarity measurement
pytest	Automated testing
Git & GitHub	Version control and source management
Streamlit Community Cloud	Deployment
📂 Project Structure
careerlens-ai/
│
├── analyzer.py
│   └── Skill extraction, matching, TF-IDF,
│       cosine similarity and scoring logic
│
├── pdf_parser.py
│   └── PDF text extraction and normalization
│
├── streamlit_app.py
│   └── Streamlit user interface and application flow
│
├── tests/
│   ├── test_analyzer.py
│   │   └── Analyzer and scoring tests
│   │
│   └── test_pdf_parser.py
│       └── PDF extraction tests
│
├── README.md
│
├── requirements.txt
│
└── .gitignore
⚙️ Installation

Follow these steps to run CareerLens AI locally.

1. Clone the repository
git clone https://github.com/kjhgft76-create/careerlens-ai.git
2. Navigate to the project directory
cd careerlens-ai
3. Create a virtual environment

Windows:

python -m venv .venv

Activate it:

.venv\Scripts\activate

For macOS/Linux:

source .venv/bin/activate
4. Install dependencies
pip install -r requirements.txt
▶️ Run the Application

Start the Streamlit application using:

python -m streamlit run streamlit_app.py

The application will open in your browser.

🧪 Running Tests

The project includes automated tests for both the analysis and PDF processing modules.

Run:

python -m pytest

The test suite covers areas such as:

Skill extraction
Skill alias normalization
Skill matching
Missing skill detection
Compatibility scoring
PDF text extraction
Invalid PDF handling
Empty PDF handling
🖥️ Application Usage
Step 1 — Upload Resume

Upload a resume in PDF format.

Step 2 — Enter Job Description

Paste the target job description into the provided input area.

Step 3 — Analyze

Click:

Analyze Compatibility →
Step 4 — View Results

The application displays:

Overall compatibility score
Skill-match score
Text similarity score
Matched skills
Missing skills
Detected resume skills
Detected job skills
📸 Application Preview

Add screenshots of your application here.

Example:

### Resume and Job Description Input

![CareerLens AI Input](screenshots/input.png)

### Compatibility Analysis

![CareerLens AI Results](screenshots/results.png)

If you create a screenshots folder in the repository, you can place your screenshots there.

☁️ Deployment

CareerLens AI is deployed as a Streamlit web application.

Live Application

https://careerlens-ai01.streamlit.app/

The application can be accessed directly through a web browser without requiring a local Python setup.

🔐 Privacy

CareerLens AI is designed to process resumes submitted by the user for the purpose of analysis.

No personal resume files are included in the project repository.

Users should avoid uploading sensitive information that they do not want processed by a third-party deployment environment.

⚠️ Current Limitations

The current version of CareerLens AI has some limitations.

1. Predefined Skill Taxonomy

Skill detection currently depends on a predefined list of technical skills and their aliases.

Skills that are not included in the taxonomy may not be detected.

2. Lexical Similarity

TF-IDF and Cosine Similarity primarily measure textual/lexical similarity.

They do not provide deep semantic understanding of the content.

3. Scanned PDFs

The current PDF parser works with selectable/readable PDF text.

Scanned or image-only PDFs may not produce readable text because OCR is not currently implemented.

4. Equal Skill Importance

The current skill-matching system does not distinguish between critical and less-important skills.

5. Limited Candidate Evaluation

The current version focuses primarily on technical skills and text similarity.

It does not perform a complete evaluation of:

Professional experience
Education
Project complexity
Certifications
Required vs. preferred qualifications
Seniority level
🔮 Future Improvements

Possible improvements for future versions include:

Semantic similarity using text embeddings
Expanded technical skill taxonomy
OCR support for scanned resumes
Experience extraction
Education extraction
Certification detection
Required vs. preferred skill classification
Skill importance weighting
More detailed compatibility explanations
Resume improvement recommendations
Job-specific resume suggestions
Improved skill recognition
Downloadable analysis reports
Advanced analytics and visualizations
📚 Key Concepts Used

This project helped implement and understand several practical concepts:

Natural Language Processing

Processing and analyzing unstructured text from resumes and job descriptions.

TF-IDF

A statistical technique used to represent the importance of words within documents.

Cosine Similarity

A similarity measurement used to compare the direction of numerical text vectors.

Regular Expressions

Used for controlled technical skill detection and matching.

Data Structures

Python sets and dictionaries are used for skill storage, alias mapping, and comparison.

Object-Oriented Concepts

The project uses Python's dataclass to structure analysis results.

Software Testing

pytest is used to validate important application and business logic.

Application Deployment

The Streamlit application is deployed as an accessible web application.

🎓 Learning Outcomes

Through this project, I worked with:

Python application development
PDF document processing
Natural Language Processing concepts
Text preprocessing
Technical skill extraction
Skill alias normalization
TF-IDF vectorization
Cosine similarity
Algorithmic scoring
Regular expressions
Modular Python project structure
Automated testing with pytest
Streamlit application development
Git and GitHub
Web application deployment
📈 Project Development Approach

The project was developed with a focus on keeping the analysis logic modular and understandable.

The main responsibilities are separated into:

PDF Processing
      ↓
Text Analysis
      ↓
Skill Extraction
      ↓
Skill Matching
      ↓
Similarity Calculation
      ↓
Score Generation
      ↓
Streamlit Presentation

This structure makes individual components easier to test, maintain, and improve.

🧩 Example Analysis

A simplified example:

Resume Skills:
Python
SQL
Pandas
Machine Learning

Job Skills:
Python
SQL
Pandas
Docker
AWS

Matched Skills:
Python
SQL
Pandas

Missing Skills:
Docker
AWS

The application combines the resulting skill alignment with the TF-IDF-based text similarity to produce the final compatibility score.

📌 Project Status

Current Version: 1.0

CareerLens AI is an actively deployable NLP-based resume–job compatibility analyzer.

The current implementation focuses on explainable skill matching and lexical text similarity, with semantic analysis and advanced recommendations planned for future versions.

👨‍💻 Author

Vivek Yadav

B.Tech — Computer Science & Engineering

📄 License

This project is licensed under the MIT License.

⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

🔗 Project Links

GitHub:
https://github.com/kjhgft76-create/careerlens-ai

Live Demo:
https://careerlens-ai01.streamlit.app/
