-- ============================
-- Departments
-- ============================

CREATE TABLE IF NOT EXISTS departments (
    department_id INTEGER PRIMARY KEY,
    department_name VARCHAR NOT NULL UNIQUE,
    location VARCHAR,
    budget DOUBLE
);

-- ============================
-- Employees
-- ============================

CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    email VARCHAR NOT NULL UNIQUE,
    phone_number VARCHAR,
    date_of_birth DATE,
    joining_date DATE NOT NULL,
    salary DOUBLE NOT NULL,
    job_title VARCHAR NOT NULL,
    grade VARCHAR,
    employment_status VARCHAR DEFAULT 'Active'
        CHECK (employment_status IN ('Active', 'On Leave', 'Resigned')),
    department_id INTEGER NOT NULL,
    manager_id INTEGER,

    FOREIGN KEY (department_id)
        REFERENCES departments(department_id),

    FOREIGN KEY (manager_id)
        REFERENCES employees(employee_id)
);

-- ============================
-- Projects
-- ============================

CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY,
    project_name VARCHAR NOT NULL,
    client_name VARCHAR,
    start_date DATE,
    end_date DATE,
    status VARCHAR DEFAULT 'Active'
        CHECK (status IN ('Active', 'Completed', 'On Hold')),
    budget DOUBLE
);

-- ============================
-- Performance Reviews
-- ============================

CREATE TABLE IF NOT EXISTS performance_reviews (
    review_id INTEGER PRIMARY KEY,
    employee_id INTEGER NOT NULL,
    review_year INTEGER NOT NULL,
    rating DOUBLE
        CHECK (rating >= 1 AND rating <= 5),
    bonus DOUBLE DEFAULT 0,
    reviewer VARCHAR,
    comments VARCHAR,

    FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id)
);

-- ============================
-- Skills
-- ============================

CREATE TABLE IF NOT EXISTS skills (
    skill_id INTEGER PRIMARY KEY,
    employee_id INTEGER NOT NULL,
    skill_name VARCHAR NOT NULL,
    proficiency_level VARCHAR
        CHECK (proficiency_level IN ('Beginner', 'Intermediate', 'Advanced', 'Expert')),

    FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id)
);

-- ============================
-- Employee Projects
-- ============================

CREATE TABLE IF NOT EXISTS employee_projects (
    assignment_id INTEGER PRIMARY KEY,
    employee_id INTEGER NOT NULL,
    project_id INTEGER NOT NULL,
    allocation_percent DOUBLE
        CHECK (allocation_percent >= 0 AND allocation_percent <= 100),
    project_role VARCHAR,
    assigned_date DATE,

    FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id),

    FOREIGN KEY (project_id)
        REFERENCES projects(project_id)
);