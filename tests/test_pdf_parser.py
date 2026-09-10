import pymupdf
import pytest

from pdf_parser import (
    PDFExtractionError,
    extract_text_from_pdf,
)


def test_extract_text_from_pdf(tmp_path):
    pdf_path = tmp_path / "resume.pdf"

    document = pymupdf.open()

    page = document.new_page()
    page.insert_text(
        (72, 72),
        "Python Developer with SQL and Pandas experience.",
    )

    document.save(pdf_path)
    document.close()

    text = extract_text_from_pdf(pdf_path)

    assert "Python Developer" in text
    assert "SQL" in text
    assert "Pandas" in text


def test_missing_pdf_raises_file_not_found():
    with pytest.raises(FileNotFoundError):
        extract_text_from_pdf(
            "does_not_exist.pdf"
        )


def test_non_pdf_file_raises_value_error(tmp_path):
    text_file = tmp_path / "resume.txt"
    text_file.write_text(
        "This is not a PDF."
    )

    with pytest.raises(ValueError):
        extract_text_from_pdf(text_file)


def test_empty_pdf_raises_extraction_error(tmp_path):
    pdf_path = tmp_path / "empty.pdf"

    document = pymupdf.open()
    document.new_page()
    document.save(pdf_path)
    document.close()

    with pytest.raises(PDFExtractionError):
        extract_text_from_pdf(pdf_path)