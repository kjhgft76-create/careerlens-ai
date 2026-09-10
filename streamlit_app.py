import streamlit as st

from analyzer import analyze_resume
from pdf_parser import PDFExtractionError, extract_text_from_pdf


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CareerLens AI",
    page_icon="🎯",
    layout="wide",
)


# ============================================================
# DARK THEME
# ============================================================

st.markdown(
    """
    <style>

    /* ======================================================
       GLOBAL
       ====================================================== */

    .stApp {
        background: #0b0f14;
        color: #e7ebf2;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }


    /* ======================================================
       HEADER
       ====================================================== */

    .brand {
        font-size: 2rem;
        font-weight: 750;
        color: #f5f7fa;
        letter-spacing: -0.02em;
    }

    .brand-ai {
        color: #8b95a5;
        margin-left: 3px;
    }

    .brand-subtitle {
        color: #687385;
        font-size: 0.87rem;
        margin-top: -3px;
    }

    .version {
        text-align: right;
        color: #687385;
        font-size: 0.9rem;
        padding-top: 0.35rem;
    }


    /* ======================================================
       HERO
       ====================================================== */

    .eyebrow {
        color: #8f9aaa;
        font-size: 1.3rem;
        font-weight: 750;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-top: 2.5rem;
        margin-bottom: 0.7rem;
    }

    .hero-title {
        color: #f5f7fa;
        font-size: 4rem;
        line-height: 1.04;
        font-weight: 780;
        letter-spacing: -0.055em;
        margin-bottom: 0.9rem;
    }

    .hero-title span {
        color: #707b8c;
    }

    .hero-description {
        max-width: 700px;
        color: #8b95a5;
        font-size: 1rem;
        line-height: 1.65;
    }


    /* ======================================================
       SECTION HEADERS
       ====================================================== */

    .section-title {
        color: #e8ecf2;
        font-size: 2rem;
        font-weight: 700;
    }

    .section-description {
        color: #687385;
        font-size: 1.6rem;
        margin-top: 3px;
    }


    /* ======================================================
       NATIVE STREAMLIT CONTAINERS
       ====================================================== */

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: #11161e;
        border: 2px solid #252c37;
        border-radius: 14px;
    }


    /* ======================================================
       INPUT LABELS
       ====================================================== */

    label {
        color: #cbd2dc !important;
    }


    /* ======================================================
       JOB DESCRIPTION
       ====================================================== */

    .stTextArea {
        margin-top: 0.3rem;
    }

    .stTextArea textarea {
        background-color: #0d1219 !important;
        color: #e8ecf2 !important;

        border: 1px solid #303845 !important;
        border-radius: 10px !important;

        font-size: 1.5rem !important;
        line-height: 1.6 !important;

        padding: 13px !important;
    }

    .stTextArea textarea::placeholder {
        color: #596474 !important;
        opacity: 1 !important;
    }

    .stTextArea textarea:focus {
        background-color: #0d1219 !important;
        color: #f5f7fa !important;

        border-color: #667085 !important;

        box-shadow: 0 0 0 1px #667085 !important;
    }


    /* ======================================================
       FILE UPLOADER
       ====================================================== */

    [data-testid="stFileUploader"] {
        background: #0d1219;
        border-radius: 10px;
    }

    [data-testid="stFileUploaderDropzone"] {
        background: #0d1219 !important;

        border: 1px dashed #303845 !important;

        border-radius: 10px !important;
    }

    [data-testid="stFileUploaderDropzoneInstructions"] {
        color: #8b95a5 !important;
    }

    [data-testid="stFileUploaderDropzoneInstructions"] span {
        color: #cbd2dc !important;
    }


    /* ======================================================
       BUTTON
       ====================================================== */
    .stButton > button {
        background: #e7ebf2 !important;
        color: #0b0f14 !important;

        border: none !important;
        border-radius: 10px !important;

        min-height: 46px;

        font-size: 1rem;
        font-weight: 700;

        transition: all 0.15s ease;
    }

    .stButton > button:hover {
        background: #ffffff !important;
        color: #0b0f14 !important;
    }

    .stButton > button:active {
        background: #171c24 !important;
        color: #ffffff !important;
        transform: scale(0.99);
    }

    .stButton > button:focus {
        background: #171c24 !important;
        color: #ffffff !important;
        box-shadow: none !important;
    }
    

    /* ======================================================
       METRICS
       ====================================================== */

    [data-testid="stMetric"] {
        background: #11161e;

        border: 1px solid #252c37;

        border-radius: 14px;

        padding: 1.2rem;
    }

    [data-testid="stMetricLabel"] {
        color: #7f8998 !important;
    }

    [data-testid="stMetricValue"] {
        color: #f1f4f8 !important;
    }

    [data-testid="stMetricDelta"] {
        color: #8f99a8 !important;
    }


    /* ======================================================
       SKILL TAGS
       ====================================================== */

    .skill {
        display: inline-block;

        padding: 5px 9px;

        margin: 3px;

        border-radius: 6px;

        font-size: 0.7rem;

        font-weight: 600;
    }

    .matched-skill {
        background: #10261f;
        color: #6ed1a7;
        border: 1px solid #1d4939;
    }

    .missing-skill {
        background: #2a1c11;
        color: #e4a56d;
        border: 1px solid #53341d;
    }


    /* ======================================================
       EXPANDERS
       ====================================================== */

    [data-testid="stExpander"] {
        background: #11161e;
        border: 1px solid #252c37;
        border-radius: 10px;
    }

    [data-testid="stExpander"] summary {
        color: #cbd2dc !important;
    }


    /* ======================================================
       ALERTS
       ====================================================== */

    [data-testid="stAlert"] {
        border-radius: 9px;
    }


    /* ======================================================
       FOOTER
       ====================================================== */

    .footer {
        text-align: center;

        color: #4f5968;

        font-size: 0.9rem;

        padding-top: 2rem;

        margin-top: 3rem;

        border-top: 1px solid #202631;
    }


    /* ======================================================
       MOBILE
       ====================================================== */

    @media (max-width: 768px) {

        .hero-title {
            font-size: 2.3rem;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HELPERS
# ============================================================


def get_score_label(score: float) -> str:
    """Return a readable interpretation of the match score."""

    if score >= 80:
        return "Excellent Match"

    if score >= 60:
        return "Strong Match"

    if score >= 40:
        return "Moderate Match"

    if score >= 20:
        return "Weak Match"

    return "Poor Match"


def display_skill_tags(
    skills: list[str],
    matched: bool,
) -> None:
    """Display skills as compact tags."""

    if not skills:
        st.caption("None detected.")
        return

    class_name = (
        "matched-skill"
        if matched
        else "missing-skill"
    )

    tags = " ".join(
        f'<span class="skill {class_name}">'
        f'{skill}'
        f'</span>'
        for skill in skills
    )

    st.markdown(
        tags,
        unsafe_allow_html=True,
    )


# ============================================================
# MAIN APPLICATION
# ============================================================


def main() -> None:
    """Run CareerLens AI."""


    # ========================================================
    # HEADER
    # ========================================================

    header_left, header_right = st.columns(
        [5, 1]
    )

    with header_left:

        st.markdown(
            """
            <div class="brand">
                CareerLens
                <span class="brand-ai">AI</span>
            </div>

            <div class="brand-subtitle">
                Resume intelligence platform
            </div>
            """,
            unsafe_allow_html=True,
        )

    with header_right:

        st.markdown(
            """
            <div class="version">
                v1.0<br>
                Resume Analysis
            </div>
            """,
            unsafe_allow_html=True,
        )


    st.divider()


    # ========================================================
    # HERO
    # ========================================================

    st.markdown(
        """
        <div class="eyebrow">
            Candidate Intelligence
        </div>

        <div class="hero-title">
            Resume compatibility,<br>
            <span>without the guesswork.</span>
        </div>

        <div class="hero-description">
            Compare your resume against a target role,
            measure skill alignment, and identify the
            capabilities you may need to strengthen
            before applying.
        </div>
        """,
        unsafe_allow_html=True,
    )


    st.write("")


    # ========================================================
    # INPUT SECTION
    # ========================================================

    st.markdown(
        '<div class="section-title">Start an analysis</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="section-description">
            Upload your own resume and paste the job
            description you are targeting.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")


    resume_column, job_column = st.columns(
        2,
        gap="large",
    )


    # ========================================================
    # RESUME
    # ========================================================

    with resume_column:

        with st.container(border=True):

            st.markdown(
                '<div class="section-title">'
                'Resume'
                '</div>',
                unsafe_allow_html=True,
            )

            st.caption(
                "Upload a text-based PDF resume."
            )

            resume_file = st.file_uploader(
                "Choose your resume",
                type=["pdf"],
                help="PDF files only.",
            )


    # ========================================================
    # JOB DESCRIPTION
    # ========================================================

    with job_column:

        with st.container(border=True):

            st.markdown(
                '<div class="section-title">'
                'Target role'
                '</div>',
                unsafe_allow_html=True,
            )

            st.caption(
                "Paste the complete job description below."
            )

            job_description = st.text_area(
                "Job description",
                height=220,
                placeholder=(
                    "Paste the job description here..."
                ),
                label_visibility="collapsed",
            )


    # ========================================================
    # FILE STATUS
    # ========================================================

    if resume_file:

        st.success(
            f"Resume ready · {resume_file.name}"
        )


    # ========================================================
    # ANALYZE
    # ========================================================

    analyze_button = st.button(
        "Analyze compatibility  →",
        type="primary",
        use_container_width=True,
    )


    if not analyze_button:

        st.markdown(
            """
            <div class="footer">
                CareerLens AI · Resume–Job Compatibility Analyzer
            </div>
            """,
            unsafe_allow_html=True,
        )

        return


    # ========================================================
    # VALIDATION
    # ========================================================

    if resume_file is None:

        st.warning(
            "Please upload your resume PDF."
        )

        return


    if not job_description.strip():

        st.warning(
            "Please paste a job description."
        )

        return


    # ========================================================
    # EXTRACT RESUME
    # ========================================================

    try:

        resume_text = extract_text_from_pdf(
            resume_file
        )

    except (
        PDFExtractionError,
        ValueError,
        OSError,
    ) as exc:

        st.error(
            f"Unable to process the resume: {exc}"
        )

        return


    # ========================================================
    # ANALYZE
    # ========================================================

    with st.spinner(
        "Analyzing resume compatibility..."
    ):

        result = analyze_resume(
            resume_text,
            job_description,
        )


    # ========================================================
    # RESULTS
    # ========================================================

    st.divider()

    st.markdown(
        '<div class="section-title">'
        'Compatibility analysis'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="section-description">
            Structured comparison between your resume
            and the target role.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")


    # ========================================================
    # SCORE SUMMARY
    # ========================================================

    score_column, skill_column, similarity_column = st.columns(
        3,
        gap="medium",
    )


    with score_column:

        st.metric(
            "Overall Match",
            f"{result.overall_score}%",
            get_score_label(
                result.overall_score
            ),
        )


    with skill_column:

        st.metric(
            "Skill Alignment",
            f"{result.skill_match_score}%",
            f"{len(result.matched_skills)} matched",
        )


    with similarity_column:

        st.metric(
            "Content Similarity",
            f"{result.similarity_score}%",
            "TF-IDF comparison",
        )


    # ========================================================
    # ASSESSMENT
    # ========================================================

    st.write("")

    score_label = get_score_label(
        result.overall_score
    )

    if result.overall_score >= 80:

        st.success(
            f"**{score_label}** — "
            "Your resume aligns very well with this role."
        )

    elif result.overall_score >= 60:

        st.info(
            f"**{score_label}** — "
            "Your resume has strong alignment with this role."
        )

    elif result.overall_score >= 40:

        st.warning(
            f"**{score_label}** — "
            "There is some alignment, but several areas "
            "could be strengthened."
        )

    else:

        st.error(
            f"**{score_label}** — "
            "Your resume has limited alignment with this role."
        )


    # ========================================================
    # SKILL INTELLIGENCE
    # ========================================================

    st.write("")

    st.markdown(
        '<div class="section-title">'
        'Skill intelligence'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="section-description">
            Technical skills identified from the target role.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")


    matched_column, missing_column = st.columns(
        2,
        gap="large",
    )


    # ========================================================
    # MATCHED
    # ========================================================

    with matched_column:

        with st.container(border=True):

            st.markdown(
                "**✓ Matched skills**"
            )

            st.caption(
                f"{len(result.matched_skills)} "
                "required skills found in your resume."
            )

            display_skill_tags(
                result.matched_skills,
                matched=True,
            )


    # ========================================================
    # MISSING
    # ========================================================

    with missing_column:

        with st.container(border=True):

            st.markdown(
                "**⚠ Skills to develop**"
            )

            st.caption(
                f"{len(result.missing_skills)} "
                "required skills not detected."
            )

            display_skill_tags(
                result.missing_skills,
                matched=False,
            )


    # ========================================================
    # DETAILED INFORMATION
    # ========================================================

    st.write("")

    with st.expander(
        "View detected skills"
    ):

        resume_skills_column, job_skills_column = st.columns(
            2
        )

        with resume_skills_column:

            st.markdown(
                "**Resume skills**"
            )

            for skill in result.resume_skills:

                st.write(
                    f"• {skill}"
                )


        with job_skills_column:

            st.markdown(
                "**Job requirements**"
            )

            for skill in result.job_skills:

                st.write(
                    f"• {skill}"
                )


    # ========================================================
    # METHODOLOGY
    # ========================================================

    with st.expander(
        "How the score is calculated"
    ):

        st.markdown(
            """
            ### Scoring model

            **70% — Skill alignment**

            Measures how many technical skills required
            by the job description were detected in the
            resume.

            **30% — Content similarity**

            Uses TF-IDF vectorization and cosine similarity
            to measure lexical overlap between the resume
            and job description.

            **Overall score**

            `Overall = (Skill Match × 0.70) + `
            `(Text Similarity × 0.30)`

            CareerLens v1 does not claim semantic understanding
            or LLM-based reasoning.
            """
        )


    # ========================================================
    # FOOTER
    # ========================================================

    st.markdown(
        """
        <div class="footer">
            CareerLens AI · Resume–Job Compatibility Analyzer
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()