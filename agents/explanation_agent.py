from models.llm import generate_response
from prompts.explanation_prompt import build_explanation_prompt
from utils.text_formatter import clean_answer


def generate_answer(question, columns, rows):

    prompt = build_explanation_prompt(
        question,
        columns,
        rows
    )

    response = generate_response(prompt)

    return clean_answer(response)