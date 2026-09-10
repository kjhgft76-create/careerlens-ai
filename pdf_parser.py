from pathlib import Path
from typing import BinaryIO

import pymupdf


class PDFExtractionError(Exception):
    """Raised when resume text cannot be extracted from a PDF."""


def extract_text_from_pdf(
    file_source: str | Path | BinaryIO,
) -> str:
    """
    Extract readable text from a PDF file or uploaded file.

    Parameters
    ----------
    file_source:
        Either a filesystem path or a binary file-like object.

    Returns
    -------
    str
        Extracted and normalized document text.

    Raises
    ------
    FileNotFoundError
        If the supplied filesystem path does not exist.
    ValueError
        If the supplied file is not a PDF.
    PDFExtractionError
        If the PDF cannot be opened or contains no readable text.
    """

    if isinstance(file_source, (str, Path)):
        return _extract_from_path(file_source)

    return _extract_from_uploaded_file(file_source)


def _extract_from_path(
    file_path: str | Path,
) -> str:
    """Extract text from a PDF stored on the filesystem."""

    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(
            f"PDF file not found: {path}"
        )

    if path.suffix.lower() != ".pdf":
        raise ValueError(
            "The supplied file must be a PDF."
        )

    try:
        document = pymupdf.open(path)
    except (pymupdf.FileDataError, OSError) as exc:
        raise PDFExtractionError(
            f"Unable to open PDF document: {path.name}"
        ) from exc

    return _extract_document_text(document)


def _extract_from_uploaded_file(
    file_source: BinaryIO,
) -> str:
    """Extract text from a Streamlit-style uploaded file."""

    file_name = getattr(
        file_source,
        "name",
        "uploaded document",
    )

    if not str(file_name).lower().endswith(".pdf"):
        raise ValueError(
            "The supplied file must be a PDF."
        )

    try:
        file_source.seek(0)
        file_bytes = file_source.read()

        document = pymupdf.open(
            stream=file_bytes,
            filetype="pdf",
        )
    except (pymupdf.FileDataError, OSError, TypeError) as exc:
        raise PDFExtractionError(
            f"Unable to open PDF document: {file_name}"
        ) from exc

    return _extract_document_text(document)


def _extract_document_text(
    document: pymupdf.Document,
) -> str:
    """Extract and normalize text from an opened PDF document."""

    try:
        pages = [
            page.get_text("text")
            for page in document
        ]
    finally:
        document.close()

    text = "\n".join(pages)
    text = _normalize_text(text)

    if not text:
        raise PDFExtractionError(
            "No readable text was found in the PDF. "
            "The document may contain scanned images "
            "instead of selectable text."
        )

    return text


def _normalize_text(text: str) -> str:
    """Normalize whitespace while preserving paragraph boundaries."""

    lines = [
        line.strip()
        for line in text.splitlines()
    ]

    cleaned_lines = []
    previous_blank = False

    for line in lines:
        if not line:
            if not previous_blank:
                cleaned_lines.append("")

            previous_blank = True
            continue

        cleaned_lines.append(line)
        previous_blank = False

    return "\n".join(cleaned_lines).strip()