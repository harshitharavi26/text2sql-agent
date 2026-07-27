SCHEMA_DOCUMENTS = [
    {
        "id": "employees",
        "document": """
        Table: employees

        Columns:
        employee_id
        first_name
        last_name
        email
        phone_number
        date_of_birth
        joining_date
        salary
        job_title
        grade
        employment_status
        department_id
        manager_id
        """,
        "metadata": {"table": "employees"},
    },
    {
        "id": "departments",
        "document": """
        Table: departments

        Columns:
        department_id
        department_name
        location
        budget
        """,
        "metadata": {"table": "departments"},
    },
    {
        "id": "projects",
        "document": """
        Table: projects

        Columns:
        project_id
        project_name
        client_name
        start_date
        end_date
        status
        budget
        """,
        "metadata": {"table": "projects"},
    },
    {
        "id": "skills",
        "document": """
        Table: skills

        Columns:
        skill_id
        employee_id
        skill_name
        proficiency_level
        """,
        "metadata": {"table": "skills"},
    },
    {
        "id": "employee_projects",
        "document": """
        Table: employee_projects

        Columns:
        assignment_id
        employee_id
        project_id
        allocation_percent
        project_role
        assigned_date
        """,
        "metadata": {"table": "employee_projects"},
    },
    {
        "id": "performance_reviews",
        "document": """
        Table: performance_reviews

        Columns:
        review_id
        employee_id
        review_year
        rating
        bonus
        reviewer
        comments
        """,
        "metadata": {"table": "performance_reviews"},
    },
]