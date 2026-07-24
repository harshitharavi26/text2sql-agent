from models.llm import generate_response
from prompts.sql_prompt import build_sql_prompt

def main():
    question = "Show the average salary by department."

    prompt = build_sql_prompt(question)

    sql = generate_response(prompt)

    print("\nGenerated SQL:\n")
    print(sql)

if __name__ =="__main__":
    main()