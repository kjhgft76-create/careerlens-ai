# CareerLens AI 🎯

CareerLens AI is a resume–job compatibility analyzer that compares a candidate's resume with a job description and identifies how well they match.

The application extracts technical skills, detects missing skills, and calculates an overall compatibility score using skill matching and TF-IDF text similarity.

## Features

- Upload a resume in PDF format
- Extract text from the resume automatically
- Detect technical skills from resume and job description
- Normalize common skill aliases such as `sklearn` → `scikit-learn`
- Identify matched and missing skills
- Calculate skill match percentage
- Calculate text similarity using TF-IDF
- Generate an overall compatibility score
- Simple Streamlit web interface
- Automated tests for core functionality and PDF extraction
- Users upload their own resume for analysis
- No personal resume data is included in the repository


## Privacy

CareerLens AI does not require a preloaded resume.

Users provide their own resume through the application when performing an analysis. No personal resume is included in this repository.

## How It Works

CareerLens AI uses two signals to calculate the compatibility score:

### 1. Skill Match — 70%

The system identifies technical skills mentioned in the job description and checks which of them are present in the resume.

```text
Skill Match = Matched Job Skills / Total Job Skills × 100

##2. Text Similarity — 30%

TF-IDF vectorization and cosine similarity are used to measure lexical similarity between the resume and job description.

Text Similarity = Cosine Similarity × 100
Overall Compatibility Score
Overall Score =
    (Skill Match × 0.70) +
    (Text Similarity × 0.30)

The weighting prioritizes actual skill alignment while still considering the overall content similarity.

Tech Stack
Python
Streamlit
PyMuPDF
scikit-learn
pytest


Project Structure

careerlens-ai/
│
├── app.py
├── streamlit_app.py
├── analyzer.py
├── pdf_parser.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── tests/
      ├── test_analyzer.py
      └── test_pdf_parser.py

Installation

Clone the repository:

git clone <https://github.com/kjhgft76-create/careerlens-ai.git>
cd careerlens-ai

Create a virtual environment:

python -m venv .venv

Activate the virtual environment on Windows:

.venv\Scripts\activate

Install the required dependencies:

python -m pip install -r requirements.txt
Run the Application

Start the Streamlit application:

python -m streamlit run streamlit_app.py

The application will open in your browser.

Run Tests

Run the automated test suite:

python -m pytest

The tests cover skill extraction, skill matching, missing skill detection, PDF extraction, input validation, and other core functionality.

Example

For a Python/data-oriented job description, CareerLens AI can identify skills such as:

Python
SQL
Pandas
NumPy
Machine Learning
Data Analysis
GitHub
Excel

The application then provides:

Overall compatibility score
Skill match percentage
Text similarity score
Matched skills
Missing skills
Current Limitations

The current version uses a predefined technical skill catalog and lexical TF-IDF similarity.

It does not yet fully understand the semantic meaning of different phrases.

For example, two sentences can have similar meanings while using different wording and may therefore receive a lower similarity score.

The current approach is intentionally lightweight, transparent, and easy to understand.

Future Improvements
Semantic similarity using embeddings
LLM-powered resume recommendations
Job-specific resume improvement suggestions
Experience and education matching
Downloadable analysis reports
Expanded skill taxonomy
OCR support for scanned resumes
Public cloud deployment
Testing

The project includes automated tests covering:

Skill extraction
Skill alias normalization
Matching skills
Missing skills
Unrelated job detection
Score calculation
Empty input handling
PDF text extraction
Invalid PDF input
Missing files
License

This project is licensed under the MIT License.


### One important thing

Where you see:

git clone <https://github.com/kjhgft76-create/careerlens-ai.git>
