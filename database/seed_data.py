from faker import Faker
import random
import duckdb


fake = Faker()

SEED = 42

random.seed(SEED)
Faker.seed(SEED)

DATABASE_PATH = "data/hr_database.duckdb"

DEPARTMENTS = [
    "Engineering",
    "Data & AI",
    "Finance",
    "Human Resources",
    "Marketing",
    "Sales",
    "Operations",
    "Legal",
    "Customer Success",
    "IT Infrastructure"
]

JOB_TITLES = [
    "Software Engineer",
    "Senior Software Engineer",
    "Data Engineer",
    "Senior Data Engineer",
    "Data Scientist",
    "Machine Learning Engineer",
    "Analytics Engineer",
    "Product Manager",
    "Engineering Manager",
    "HR Manager",
    "Financial Analyst",
    "Marketing Manager",
    "Sales Executive",
    "DevOps Engineer",
    "Cloud Engineer"
]

SKILLS = [
    "Python",
    "SQL",
    "Spark",
    "Airflow",
    "Docker",
    "Kubernetes",
    "AWS",
    "Azure",
    "GCP",
    "Power BI",
    "Tableau",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "PyTorch",
    "LangChain",
    "LlamaIndex",
    "Git",
    "Linux",
    "Java"
]

PROJECTS = [
    "Project Phoenix",
    "Project Atlas",
    "Project Orion",
    "Project Nova",
    "Project Titan",
    "Project Horizon",
    "Project Eclipse",
    "Project Quantum",
    "Project Neptune",
    "Project Everest"
]

EMPLOYMENT_STATUS = [
    "Active",
    "On Leave",
    "Resigned"
]

GRADES = [
    "L1",
    "L2",
    "L3",
    "L4",
    "L5",
    "M1",
    "M2"
]

LOCATIONS = [
    "Bangalore",
    "Hyderabad",
    "Chennai",
    "Pune",
    "Seattle",
    "Austin",
    "New York",
    "London",
    "Singapore",
    "Toronto"
]

CLIENTS = [
    "Microsoft",
    "Google",
    "Amazon",
    "Meta",
    "Apple",
    "Netflix",
    "Adobe",
    "NVIDIA",
    "Tesla",
    "Salesforce",
    "Spotify",
    "Uber",
    "Intel",
    "Cisco",
    "Oracle"
]

REVIEW_YEARS = [2023, 2024, 2025]

REVIEWERS = [
    "John Smith",
    "Sarah Johnson",
    "Michael Brown",
    "Emily Davis",
    "David Wilson",
    "Jessica Taylor",
    "Robert Miller",
    "Jennifer Anderson"
]

REVIEW_COMMENTS = [
    "Outstanding performance throughout the year.",
    "Exceeded expectations on key projects.",
    "Consistently delivered high-quality work.",
    "Strong technical skills and teamwork.",
    "Excellent problem-solving abilities.",
    "Needs improvement in communication.",
    "Demonstrates leadership potential.",
    "Highly dependable and proactive.",
    "Met all performance expectations.",
    "Great collaboration with cross-functional teams."
]

PROJECT_ROLES = [
    "Developer",
    "Tech Lead",
    "Architect",
    "QA Engineer",
    "Data Engineer",
    "ML Engineer",
    "Business Analyst",
    "Project Manager"
]

JOB_TITLE_TO_DEPARTMENT = {
    "Software Engineer": "Engineering",
    "Senior Software Engineer": "Engineering",
    "Data Engineer": "Data & AI",
    "Senior Data Engineer": "Data & AI",
    "Data Scientist": "Data & AI",
    "Machine Learning Engineer": "Data & AI",
    "Analytics Engineer": "Data & AI",
    "Engineering Manager": "Engineering",
    "DevOps Engineer": "IT Infrastructure",
    "Cloud Engineer": "IT Infrastructure",
    "HR Manager": "Human Resources",
    "Financial Analyst": "Finance",
    "Marketing Manager": "Marketing",
    "Sales Executive": "Sales",
    "Product Manager": "Engineering",
}

SALARY_RANGES = {
    "Software Engineer": (85000, 110000),
    "Senior Software Engineer": (120000, 150000),
    "Data Engineer": (95000, 125000),
    "Senior Data Engineer": (130000, 165000),
    "Data Scientist": (100000, 135000),
    "Machine Learning Engineer": (120000, 170000),
    "Analytics Engineer": (95000, 120000),
    "Engineering Manager": (170000, 220000),
    "HR Manager": (90000, 130000),
    "Financial Analyst": (80000, 110000),
    "Marketing Manager": (90000, 125000),
    "Sales Executive": (70000, 140000),
    "DevOps Engineer": (100000, 140000),
    "Cloud Engineer": (110000, 150000),
    "Product Manager": (130000, 170000),
}

JOB_TITLE_TO_GRADE = {
    "Software Engineer": "L2",
    "Senior Software Engineer": "L4",
    "Data Engineer": "L3",
    "Senior Data Engineer": "L5",
    "Data Scientist": "L3",
    "Machine Learning Engineer": "L4",
    "Analytics Engineer": "L3",
    "Engineering Manager": "M1",
    "HR Manager": "M1",
    "Financial Analyst": "L3",
    "Marketing Manager": "M1",
    "Sales Executive": "L2",
    "DevOps Engineer": "L3",
    "Cloud Engineer": "L4",
    "Product Manager": "M1",
}

JOB_TITLE_WEIGHTS = {
    "Software Engineer": 18,
    "Senior Software Engineer": 10,
    "Data Engineer": 12,
    "Senior Data Engineer": 7,
    "Data Scientist": 8,
    "Machine Learning Engineer": 5,
    "Analytics Engineer": 5,
    "Product Manager": 5,
    "Engineering Manager": 4,
    "HR Manager": 3,
    "Financial Analyst": 4,
    "Marketing Manager": 3,
    "Sales Executive": 4,
    "DevOps Engineer": 7,
    "Cloud Engineer": 5,
}

DEPARTMENT_BUDGET_RANGES = {
    "Engineering": (15_000_000, 20_000_000),
    "Data & AI": (12_000_000, 18_000_000),
    "IT Infrastructure": (10_000_000, 15_000_000),
    "Sales": (8_000_000, 12_000_000),
    "Marketing": (5_000_000, 10_000_000),
    "Finance": (4_000_000, 8_000_000),
    "Human Resources": (2_000_000, 5_000_000),
    "Operations": (5_000_000, 9_000_000),
    "Legal": (2_000_000, 4_000_000),
    "Customer Success": (4_000_000, 7_000_000),
}

ROLE_TO_SKILLS = {
    "Software Engineer": [
        "Python",
        "Java",
        "Git",
        "Docker",
        "Linux",
        "SQL"
    ],

    "Senior Software Engineer": [
        "Python",
        "Java",
        "Git",
        "Docker",
        "Kubernetes",
        "Linux",
        "SQL",
        "AWS"
    ],

    "Data Engineer": [
        "Python",
        "SQL",
        "Spark",
        "Airflow",
        "Docker",
        "Azure",
        "GCP",
        "Git"
    ],

    "Senior Data Engineer": [
        "Python",
        "SQL",
        "Spark",
        "Airflow",
        "Docker",
        "Azure",
        "GCP",
        "Kubernetes",
        "Git"
    ],

    "Data Scientist": [
        "Python",
        "SQL",
        "Machine Learning",
        "TensorFlow",
        "PyTorch",
        "Deep Learning",
        "Git"
    ],

    "Machine Learning Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "Docker",
        "Kubernetes",
        "Git"
    ],

    "Analytics Engineer": [
        "SQL",
        "Python",
        "Power BI",
        "Tableau",
        "Git",
        "Azure"
    ],

    "Product Manager": [
        "SQL",
        "Power BI",
        "Tableau",
        "Git"
    ],

    "Engineering Manager": [
        "Python",
        "SQL",
        "Git",
        "Docker",
        "AWS"
    ],

    "HR Manager": [
        "Power BI",
        "SQL",
        "Git"
    ],

    "Financial Analyst": [
        "SQL",
        "Power BI",
        "Tableau",
        "Python"
    ],

    "Marketing Manager": [
        "Power BI",
        "Tableau",
        "SQL"
    ],

    "Sales Executive": [
        "Power BI",
        "SQL"
    ],

    "DevOps Engineer": [
        "Docker",
        "Kubernetes",
        "AWS",
        "Azure",
        "Linux",
        "Python",
        "Git"
    ],

    "Cloud Engineer": [
        "AWS",
        "Azure",
        "GCP",
        "Docker",
        "Kubernetes",
        "Linux",
        "Python"
    ]
}

PROJECT_STATUS = {
    "Active": 70,
    "Completed": 20,
    "On Hold": 10
}

NUM_PROJECTS = 50

RATING_WEIGHTS = {
    1.0: 2,
    2.0: 8,
    3.0: 30,
    4.0: 40,
    5.0: 20
}

def clear_tables(connection):
    """Delete existing data before seeding."""

    connection.execute("DELETE FROM employee_projects")
    connection.execute("DELETE FROM skills")
    connection.execute("DELETE FROM performance_reviews")
    connection.execute("DELETE FROM employees")
    connection.execute("DELETE FROM projects")
    connection.execute("DELETE FROM departments")


DEPARTMENT_IDS = {name: idx + 1 for idx, name in enumerate(DEPARTMENTS)}
def seed_departments(connection):
        '''Seed the departments table with predefined department names.'''
        try:
            print("Seeding departments...")
            departments = []
            for department_id, department_name in enumerate(DEPARTMENTS,start=1):
                  location = random.choice(LOCATIONS)
                  budget = random.randint(*DEPARTMENT_BUDGET_RANGES[department_name])
                  departments.append((department_id, department_name, location, budget))
            
            connection.executemany(
            """
                INSERT INTO departments (
                department_id,
                department_name,
                location,
                budget
            )
                VALUES (?, ?, ?, ?)
            """,
            departments,
        )
            print(f"Seeded {len(departments)} departments.")
        
        except Exception as e:
            print(f"Error seeding departments: {e}")

def seed_employees(connection, num_employees = 500):
      '''Seed the employees table with random employee data.'''
      
      try:
            print(f"Seeding {num_employees} employees...")
            employees = []
            job_titles = list(JOB_TITLE_WEIGHTS.keys())
            job_weights = list(JOB_TITLE_WEIGHTS.values())
            for employee_id in range(1,num_employees+1):
                  if employee_id <= 10:
                    manager_id = None
                  else:
                    manager_id = random.randint(1, 10)
                  first_name = fake.first_name()
                  last_name = fake.last_name()
                  email = fake.unique.email()
                  phone_number = fake.phone_number()
                  job_title = random.choices(
                    job_titles,
                    job_weights,
                    k=1 )[0]
                  department = JOB_TITLE_TO_DEPARTMENT[job_title]
                  department_id = DEPARTMENT_IDS[department]
                  salary = random.randint(*SALARY_RANGES[job_title])
                  grade = JOB_TITLE_TO_GRADE[job_title]
                  date_of_birth = fake.date_of_birth(
                        minimum_age=22,
                        maximum_age=60
                    )
                  joining_date = fake.date_between(
                    start_date="-10y",
                    end_date="today"
                )
                  employment_status = random.choices(
                    EMPLOYMENT_STATUS,
                    weights=[90, 5, 5],
                    k=1
                )[0]
    
                  employees.append(
                    (
                        employee_id,
                        first_name,
                        last_name,
                        email,
                        phone_number,
                        date_of_birth,
                        joining_date,
                        salary,
                        job_title,
                        grade,
                        employment_status,
                        department_id,
                        manager_id
                    )
                )
                  
            connection.executemany(
                  """
                  INSERT INTO employees (
                        employee_id,
                        first_name,
                        last_name,
                        email,
                        phone_number,
                        date_of_birth,
                        joining_date,
                        salary,
                        job_title,
                        grade,
                        employment_status,
                        department_id,
                        manager_id
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                     
                     """
             , employees)
            
            print(f"Seeded {len(employees)} employees.")
      except Exception as e:
            print(f"Error seeding employees: {e}")  

def seed_skills(connection):
    """Seed the skills table with predefined skills."""
    employees = connection.execute(
         '''
         SELECT employee_id, job_title FROM employees
         '''
    ).fetchall()
    skills = []
    skill_id = 1
    for employee_id, job_title in employees:
         available_skills = ROLE_TO_SKILLS[job_title]
         selected_skills = random.sample(available_skills,k=random.randint(
                min(3, len(available_skills)),
                min(6, len(available_skills))
            )
        )
         for skill in selected_skills:
            proficiency_level = random.choice(["Beginner", "Intermediate", "Advanced"])
            skills.append((skill_id, employee_id, skill, proficiency_level))
         
            skill_id += 1
    connection.executemany(
         """
         INSERT INTO skills(skill_id, employee_id, skill_name, proficiency_level)
            VALUES(?, ?, ?, ?)
         """,
         skills
    )
    print(f"Seeded {len(skills)} skills.")

def seed_projects(connection):
    """Seed the projects table."""

    try:
        print(f"Seeding {NUM_PROJECTS} projects...")

        projects = []

        for project_id in range(1, NUM_PROJECTS + 1):

            project_name = f"{random.choice(PROJECTS)} {project_id}"

            client_name = random.choice(CLIENTS)

            start_date = fake.date_between(
                start_date="-5y",
                end_date="-30d"
            )

            status = random.choices(
                population=list(PROJECT_STATUS.keys()),
                weights=list(PROJECT_STATUS.values()),
                k=1
            )[0]

            if status == "Completed":
                end_date = fake.date_between(
                    start_date=start_date,
                    end_date="today"
                )
            else:
                end_date = None

            budget = random.randint(
                500_000,
                10_000_000
            )

            projects.append(
                (
                    project_id,
                    project_name,
                    client_name,
                    start_date,
                    end_date,
                    status,
                    budget
                )
            )

        connection.executemany(
            """
            INSERT INTO projects (
                project_id,
                project_name,
                client_name,
                start_date,
                end_date,
                status,
                budget
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            projects
        )

        print(f"Seeded {len(projects)} projects.")

    except Exception as e:
        print(f"Error seeding projects: {e}")

def seed_employee_projects(connection):
    """Assign employees to projects."""

    try:
        print("Assigning employees to projects...")

        employees = connection.execute(
            """
            SELECT employee_id
            FROM employees
            """
        ).fetchall()

        projects = connection.execute(
            """
            SELECT project_id
            FROM projects
            """
        ).fetchall()

        project_ids = [project[0] for project in projects]

        assignments = []

        assignment_id = 1

        for employee_id, in employees:

            assigned_projects = random.sample(
                project_ids,
                k=random.randint(1, 3)
            )

            for project_id in assigned_projects:

                allocation_percent = random.choice(
                    [25, 50, 75, 100]
                )

                project_role = random.choice(PROJECT_ROLES)

                assigned_date = fake.date_between(
                    start_date="-3y",
                    end_date="today"
                )

                assignments.append(
                    (
                        assignment_id,
                        employee_id,
                        project_id,
                        allocation_percent,
                        project_role,
                        assigned_date
                    )
                )

                assignment_id += 1

        connection.executemany(
            """
            INSERT INTO employee_projects (
                assignment_id,
                employee_id,
                project_id,
                allocation_percent,
                project_role,
                assigned_date
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            assignments
        )

        print(f"Seeded {len(assignments)} employee-project assignments.")

    except Exception as e:
        print(f"Error seeding employee projects: {e}")


def seed_performance_reviews(connection):
    """Seed the performance_reviews table."""

    try:
        print("Seeding performance reviews...")

        employees = connection.execute(
            """
            SELECT employee_id
            FROM employees
            """
        ).fetchall()

        reviews = []

        review_id = 1

        for (employee_id,) in employees:

            years = random.sample(
                REVIEW_YEARS,
                k=random.randint(1, len(REVIEW_YEARS))
            )

            for year in years:

                rating = random.choices(
                    population=list(RATING_WEIGHTS.keys()),
                    weights=list(RATING_WEIGHTS.values()),
                    k=1
                )[0]

                bonus = 0

                if rating >= 4:
                    bonus = random.randint(3000, 15000)
                elif rating == 3:
                    bonus = random.randint(1000, 5000)

                reviewer = random.choice(REVIEWERS)

                comments = random.choice(REVIEW_COMMENTS)

                reviews.append(
                    (
                        review_id,
                        employee_id,
                        year,
                        rating,
                        bonus,
                        reviewer,
                        comments
                    )
                )

                review_id += 1

        connection.executemany(
            """
            INSERT INTO performance_reviews (
                review_id,
                employee_id,
                review_year,
                rating,
                bonus,
                reviewer,
                comments
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            reviews
        )

        print(f"Seeded {len(reviews)} performance reviews.")

    except Exception as e:
        print(f"Error seeding performance reviews: {e}")


def main():
    with duckdb.connect(DATABASE_PATH) as connection:
        seed_departments(connection)
        seed_employees(connection)
        seed_skills(connection)
        seed_projects(connection)
        seed_employee_projects(connection)
        seed_performance_reviews(connection)

if __name__ == "__main__":
    main()
