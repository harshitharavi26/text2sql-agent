import re


def clean_answer(text):

    # Remove excessive whitespace/newlines
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    # Fix spaces around commas
    text = re.sub(
        r"\s+,\s+",
        ", ",
        text
    )

    # Fix spaces around dollar values
    text = re.sub(
        r"\$\s+",
        "$",
        text
    )

    return text.strip()