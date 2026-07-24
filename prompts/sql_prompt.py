SYSTEM_PROMPT = """
You are an expert SQL developer.

You generate SQL queries for a DuckDB database.

Rules:
- Return only SQL.
- Do not explain anything.
- Do not use markdown.
- Do not wrap SQL in ``` blocks.
- Use only the tables and columns provided.
"""


DATABASE_SCHEMA = """
Table: departments
Columns:
- department_id
- department_name
- location
- budget

Table: employees
Columns:
- employee_id
- first_name
- last_name
- email
- phone_number
- date_of_birth
- joining_date
- salary
- job_title
- grade
- employment_status
- department_id
- manager_id

Table: projects
Columns:
- project_id
- project_name
- client_name
- start_date
- end_date
- status
- budget

Table: skills
Columns:
- skill_id
- employee_id
- skill_name
- proficiency_level

Table: performance_reviews
Columns:
- review_id
- employee_id
- review_year
- rating
- bonus
- reviewer
- comments

Table: employee_projects
Columns:
- assignment_id
- employee_id
- project_id
- allocation_percent
- project_role
- assigned_date

Relationships:
employees.department_id -> departments.department_id
employees.employee_id -> skills.employee_id
employees.employee_id -> performance_reviews.employee_id
employees.employee_id -> employee_projects.employee_id
projects.project_id -> employee_projects.project_id
employees.manager_id -> employees.employee_id
"""

def build_sql_prompt(user_question: str) -> str:
    """
    Build a prompt for SQL generation.
    """

    return f"""
{SYSTEM_PROMPT}

Database Schema:

{DATABASE_SCHEMA}

User Question:
{user_question}

Return only SQL.
"""