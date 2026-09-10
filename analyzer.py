import re
from dataclasses import dataclass

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Common technical and professional skills found in job descriptions.
# Each key is the canonical skill name used in analysis.
SKILL_ALIASES = {
    # Programming
    "python": ["python"],
    "java": ["java"],
    "javascript": ["javascript", "js"],
    "typescript": ["typescript", "ts"],
    "c++": ["c++"],
    "c#": ["c#", "c sharp"],

    # Web development
    "html": ["html", "html5"],
    "css": ["css", "css3"],
    "react": ["react", "react.js", "reactjs"],
    "node.js": ["node.js", "nodejs", "node"],
    "django": ["django"],
    "flask": ["flask"],
    "fastapi": ["fastapi"],
    "streamlit": ["streamlit"],

    # Data
    "sql": ["sql"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "excel": ["excel", "microsoft excel"],
    "power bi": ["power bi", "powerbi"],
    "tableau": ["tableau"],
    "data analysis": ["data analysis", "data analytics"],
    "data science": ["data science"],

    # AI / Machine Learning
    "machine learning": ["machine learning", "ml"],
    "deep learning": ["deep learning"],
    "natural language processing": [
        "natural language processing",
        "nlp",
    ],
    "computer vision": ["computer vision"],
    "tensorflow": ["tensorflow"],
    "pytorch": ["pytorch"],
    "scikit-learn": [
        "scikit-learn",
        "sklearn",
        "scikit learn",
    ],

    # Databases
    "mysql": ["mysql"],
    "postgresql": [
        "postgresql",
        "postgres",
        "postgres db",
    ],
    "mongodb": ["mongodb", "mongo db"],
    "redis": ["redis"],

    # APIs
    "rest api": [
        "rest api",
        "restful api",
        "rest apis",
    ],
    "graphql": ["graphql"],
    "api": ["api", "apis"],

    # Cloud / DevOps
    "aws": ["aws", "amazon web services"],
    "azure": ["azure", "microsoft azure"],
    "gcp": [
        "gcp",
        "google cloud",
        "google cloud platform",
    ],
    "docker": ["docker"],
    "kubernetes": ["kubernetes", "k8s"],
    "linux": ["linux"],

    # Version control
    "git": ["git"],
    "github": ["github", "git hub"],

    # Design
    "figma": ["figma"],
    "photoshop": [
        "photoshop",
        "adobe photoshop",
    ],
    "illustrator": [
        "illustrator",
        "adobe illustrator",
    ],
    "ui design": [
        "ui design",
        "user interface design",
    ],
    "ux design": [
        "ux design",
        "user experience design",
    ],
    "graphic design": [
        "graphic design",
        "graphic designer",
    ],
    "typography": ["typography"],
    "branding": ["branding"],
    "logo design": [
        "logo design",
        "logo designing"
    ],
    "visual design": ["visual design"],
}


@dataclass
class AnalysisResult:
    """Contains the results of comparing a resume with a job description."""

    overall_score: float
    skill_match_score: float
    similarity_score: float
    resume_skills: list[str]
    job_skills: list[str]
    matched_skills: list[str]
    missing_skills: list[str]


def extract_skills(text: str) -> list[str]:
    """
    Identify known skills mentioned in a piece of text.

    Skill aliases are normalized to their canonical names so that
    equivalent terms such as "sklearn" and "scikit-learn" are treated
    as the same skill.
    """
    normalized_text = _normalize_text(text)

    found_skills = set()

    for canonical_skill, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            if _skill_is_present(alias, normalized_text):
                found_skills.add(canonical_skill)
                break

    return sorted(found_skills)


def analyze_resume(
    resume_text: str,
    job_description: str,
) -> AnalysisResult:
    """
    Compare a resume against a job description.

    The analysis combines:
    - TF-IDF lexical similarity
    - technical skill extraction
    - matched skill identification
    - missing skill identification
    - weighted compatibility scoring
    """
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched_skills = sorted(
        set(resume_skills) & set(job_skills)
    )

    missing_skills = sorted(
        set(job_skills) - set(resume_skills)
    )

    similarity_score = _calculate_similarity(
        resume_text,
        job_description,
    )

    skill_match_score = _calculate_skill_match(
        job_skills,
        matched_skills,
    )

    overall_score = _calculate_overall_score(
        skill_match_score,
        similarity_score,
    )

    return AnalysisResult(
        overall_score=overall_score,
        skill_match_score=skill_match_score,
        similarity_score=similarity_score,
        resume_skills=resume_skills,
        job_skills=job_skills,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
    )


def _calculate_similarity(
    text_a: str,
    text_b: str,
) -> float:
    """Calculate lexical similarity using TF-IDF and cosine similarity."""
    if not text_a.strip() or not text_b.strip():
        return 0.0

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
    )

    try:
        vectors = vectorizer.fit_transform(
            [text_a, text_b]
        )
    except ValueError:
        return 0.0

    score = cosine_similarity(
        vectors[0:1],
        vectors[1:2],
    )[0][0]

    return round(score * 100, 1)


def _calculate_skill_match(
    job_skills: list[str],
    matched_skills: list[str],
) -> float:
    """Calculate the percentage of job skills found in the resume."""
    if not job_skills:
        return 0.0

    score = (
        len(matched_skills)
        / len(job_skills)
        * 100
    )

    return round(score, 1)


def _calculate_overall_score(
    skill_match_score: float,
    similarity_score: float,
) -> float:
    """Calculate the weighted resume-to-job compatibility score."""
    overall_score = (
        skill_match_score * 0.70
        + similarity_score * 0.30
    )

    return round(overall_score, 1)


def _skill_is_present(
    skill: str,
    text: str,
) -> bool:
    """Check whether a skill appears as a meaningful term in the text."""
    escaped_skill = re.escape(skill)

    pattern = rf"(?<!\w){escaped_skill}(?!\w)"

    return bool(re.search(pattern, text))


def _normalize_text(text: str) -> str:
    """Normalize text for consistent skill matching."""
    return re.sub(
        r"\s+",
        " ",
        text.lower(),
    ).strip()