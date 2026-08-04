# Agentic Text-to-SQL Assistant using LangGraph & RAG

An agentic AI-powered Text-to-SQL system that enables users to query a relational HR database using natural language.

The system converts natural language questions into SQL queries, retrieves relevant database schema using RAG, validates generated SQL for safety, executes queries, repairs failed SQL when required, and generates concise natural-language explanations.

---

# Overview

Traditional database systems require users to understand SQL syntax and database schemas before querying data.

This project provides a natural language interface over a relational HR database.

Example:

### User Input

```
Show average salary by department
```

### Generated SQL

```sql
SELECT
    d.department_name,
    AVG(e.salary) AS average_salary
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
GROUP BY d.department_name;
```

### Generated Answer

```
The table shows the average salary for employees in each department.
IT Infrastructure has the highest average salary at $126,232,
while Finance has the lowest at $94,685.
```

---

# Key Features

## Agentic Text-to-SQL Workflow

The system uses LangGraph to orchestrate a multi-step SQL generation workflow:

```
User Question
      |
      v
Retrieve Relevant Schema
      |
      v
Generate SQL
      |
      v
Validate SQL
      |
      +----------------+
      |                |
      v                v
 Execute Query     Repair SQL
      |                |
      +----------------+
              |
              v
     Generate Explanation
              |
              v
        Final Response
```

Workflow components:

- Schema Retrieval
- SQL Generation
- SQL Validation
- SQL Execution
- SQL Repair
- Natural Language Explanation


---

# Retrieval-Augmented Generation (RAG)

The system uses ChromaDB-based vector search to retrieve relevant database schema information before SQL generation.

Benefits:

- Reduces incorrect table selection
- Provides schema context to the LLM
- Enables schema-aware SQL generation
- Improves SQL accuracy


Pipeline:

```
User Question
      |
      v
Embedding Generation
      |
      v
ChromaDB Similarity Search
      |
      v
Relevant Schema Context
      |
      v
SQL Generation
```

---

# SQL Safety Validation

Generated SQL queries are validated before execution.

Implemented protections:

### Allowed Queries

Only read-only queries are accepted:

```
SELECT
WITH
```

### Blocked Operations

The validator rejects:

```
DROP
DELETE
UPDATE
INSERT
ALTER
TRUNCATE
CREATE
REPLACE
COPY
INSTALL
LOAD
```

Additional protections:

- Rejects empty LLM responses
- Removes Markdown SQL formatting
- Prevents multiple SQL statements
- Blocks unsafe database operations


---

# Automatic SQL Repair

If generated SQL fails:

1. Database error is captured
2. Failed SQL is sent to the repair workflow
3. The LLM generates corrected SQL
4. The repaired query is validated
5. The query is retried once

This prevents infinite correction loops while improving query reliability.


---

# Natural Language Answers

After successful execution, the system converts query results into concise explanations.

Example:

```
The table shows average salary by department.
IT Infrastructure has the highest average salary at $126,232,
while Finance has the lowest at $94,685.
```

The explanation layer avoids exposing SQL details and provides user-friendly responses.


---

# Architecture

```
                         User Question
                              |
                              v
                 +-------------------------+
                 | Schema Retrieval Node   |
                 |       ChromaDB RAG      |
                 +-------------------------+
                              |
                              v
                 +-------------------------+
                 | SQL Generation Node     |
                 |     Ollama LLM          |
                 +-------------------------+
                              |
                              v
                 +-------------------------+
                 | SQL Validation Node     |
                 +-------------------------+
                              |
              +---------------+---------------+
              |                               |
              v                               v
       Valid SQL                         Invalid SQL
              |                               |
              v                               v
     Execute Query                     Repair SQL
              |                               |
              +---------------+---------------+
                              |
                              v
                 +-------------------------+
                 | Explanation Generation |
                 +-------------------------+
                              |
                              v
                         Final Response
```

---

# LangGraph Workflow

The workflow is implemented using a shared state object:

```
SQLAgentState
```

Each node receives the current state, performs an operation, and updates the state.

Workflow:

```
retrieve_schema
        |
        v
generate_sql
        |
        v
validate_sql
        |
        +----------------+
        |                |
        v                v
 execute_sql       repair_sql
        |                |
        +----------------+
                |
                v
       generate_answer
                |
                v
               END
```

---

# Tech Stack

## AI / LLM

- LangGraph
- LangChain
- Ollama
- Qwen 2.5 / Llama models

## Retrieval

- ChromaDB
- Embeddings
- Retrieval-Augmented Generation (RAG)

## Database

- DuckDB
- SQL execution engine

## Application

- Streamlit

## Testing

- Pytest


---

# Project Structure

```
text2sql-agent/

├── agents/
│   ├── graph.py
│   ├── state.py
│   └── nodes/
│       ├── retrieve_schema.py
│       ├── generate_sql.py
│       ├── validate_sql.py
│       ├── execute_sql.py
│       ├── repair_sql.py
│       └── generate_answer.py
│
├── rag/
│   ├── vector_store.py
│   ├── embeddings.py
│   └── schema_loader.py
│
├── database/
│   ├── schema.sql
│   ├── seed_data.py
│   ├── create_database.py
│   └── query_executor.py
│
├── models/
│   └── llm.py
│
├── prompts/
│   ├── sql_prompt.py
│   ├── fix_sql_prompt.py
│   └── explanation_prompt.py
│
├── frontend/
│   └── streamlit_app.py
│
├── tests/
│
├── requirements.txt
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/harshitharavi26/text2sql-agent.git

cd text2sql-agent
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

### macOS/Linux

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Ollama Setup

Install Ollama:

https://ollama.com


Pull the required model:

```bash
ollama pull qwen2.5:7b
```

Verify:

```bash
ollama list
```

---

# Database Initialization

Create the DuckDB database:

```bash
python database/create_database.py
```

Generate sample HR data:

```bash
python database/seed_data.py
```

Database contains:

- Departments
- Employees
- Projects
- Skills
- Employee Projects
- Performance Reviews


---

# Build Schema Vector Store

Load schema documents into ChromaDB:

```bash
python rag/vector_store.py
```

This creates the RAG retrieval layer used during SQL generation.


---

# Running the Application

Start Streamlit:

```bash
streamlit run frontend/streamlit_app.py
```

The application provides:

- Natural language input
- Generated SQL
- Query results
- Natural language explanations
- SQL repair details when required


---

# Example Questions

Try asking:

```
Show average salary by department
```

```
Which department has the highest average salary?
```

```
List employees working in Engineering
```

```
Show projects and assigned employees
```

```
Find the number of employees in each department
```

---

# Testing

Run all tests:

```bash
python -m pytest
```

Individual tests:

```bash
python -m pytest tests/test_graph.py
```

```bash
python -m pytest tests/test_failure_cases.py
```

Test coverage includes:

- SQL generation
- Schema retrieval
- Query execution
- SQL repair
- Unsafe SQL rejection
- LangGraph workflow


---

# Safety Considerations

The system includes multiple safety layers.

## SQL Validation

Only read-only queries are executed.

Accepted:

```
SELECT
WITH
```

Rejected:

```
DROP
DELETE
UPDATE
INSERT
ALTER
```

## Repair Protection

SQL repair is limited to one retry to prevent endless correction cycles.


---

# Limitations

Current limitations:

- Designed for the provided HR database schema
- SQL quality depends on schema retrieval accuracy
- Requires local Ollama model execution
- Not optimized for extremely large enterprise databases
- No authentication layer currently implemented


---

# Future Improvements

Potential enhancements:

- Deploy as a cloud API
- Add authentication and authorization
- Support multiple databases
- Add conversational memory
- Add query history
- Add user feedback loop
- Integrate hosted LLM providers
- Add monitoring and observability


---

# Screenshots

(Add Streamlit screenshots here)

---

# Author

**Harshitha Ravishankar**

Built as an exploration of:

- Agentic AI Systems
- Retrieval-Augmented Generation
- Natural Language Database Interfaces
- LangGraph Orchestration