from analyzer import analyze_resume, extract_skills


def test_extract_skills_detects_common_skills():
    text = """
    Experienced Python developer with SQL, Pandas,
    NumPy and Machine Learning experience.
    """

    skills = extract_skills(text)

    assert "python" in skills
    assert "sql" in skills
    assert "pandas" in skills
    assert "numpy" in skills
    assert "machine learning" in skills


def test_skill_aliases_are_normalized():
    text = """
    Experience with sklearn, Postgres, NLP and ReactJS.
    """

    skills = extract_skills(text)

    assert "scikit-learn" in skills
    assert "postgresql" in skills
    assert "natural language processing" in skills
    assert "react" in skills


def test_matching_skills_are_detected():
    resume = """
    Python developer with experience in Python, SQL,
    Pandas and NumPy.
    """

    job = """
    Looking for a developer with Python, SQL, Pandas
    and NumPy experience.
    """

    result = analyze_resume(resume, job)

    assert result.skill_match_score == 100.0
    assert "python" in result.matched_skills
    assert "pandas" in result.matched_skills
    assert "numpy" in result.matched_skills
    assert "sql" in result.matched_skills


def test_missing_skills_are_detected():
    resume = """
    Python developer with experience in Python and SQL.
    """

    job = """
    Looking for a developer with Python, SQL, Docker,
    AWS and Kubernetes experience.
    """

    result = analyze_resume(resume, job)

    assert "python" in result.matched_skills
    assert "sql" in result.matched_skills

    assert "docker" in result.missing_skills
    assert "aws" in result.missing_skills
    assert "kubernetes" in result.missing_skills


def test_unrelated_job_has_no_matching_skills():
    resume = """
    Python developer experienced in Python, Pandas,
    NumPy and Machine Learning.
    """

    job = """
    Graphic designer experienced in Photoshop, Figma,
    Illustrator and Typography.
    """

    result = analyze_resume(resume, job)

    assert result.skill_match_score == 0.0
    assert result.matched_skills == []


def test_unrelated_job_has_low_overall_score():
    resume = """
    Python developer experienced in Python, Pandas,
    NumPy and Machine Learning.
    """

    job = """
    Graphic designer experienced in Photoshop, Figma,
    Illustrator and Typography.
    """

    result = analyze_resume(resume, job)

    assert result.overall_score < 30.0


def test_empty_job_description_returns_zero_skill_match():
    resume = """
    Python developer with Python and SQL experience.
    """

    result = analyze_resume(resume, "")

    assert result.skill_match_score == 0.0
    assert result.matched_skills == []
    assert result.missing_skills == []