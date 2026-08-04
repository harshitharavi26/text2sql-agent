from agents.sql_agent import answer_question
from utils.sql_validator import validate_sql

def test_valid_question():

    question = "How many employees are there?"

    result = answer_question(question)

    assert result["success"] is True
    assert result["columns"] is not None
    assert result["rows"] is not None

def test_non_read_sql_rejected():

    sql = """
    DROP TABLE employees;
    """

    is_valid, error = validate_sql(sql)

    assert is_valid is False
    assert "Only SELECT and WITH queries are allowed." in error



def test_forbidden_keyword_rejected():

    sql = """
    SELECT *
    FROM employees
    WHERE name = 'DELETE';
    """

    is_valid, error = validate_sql(sql)

    assert is_valid is False
    assert "Forbidden SQL operation detected" in error

def test_empty_sql_rejected():

    is_valid, error = validate_sql("")

    assert is_valid is False
    assert error == "Generated SQL is empty."

def test_multiple_statements_rejected():

    sql = """
    SELECT * FROM employees;
    SELECT * FROM departments;
    """

    is_valid, error = validate_sql(sql)

    assert is_valid is False
    assert "Only one SQL statement is allowed" in error

def test_repair_failure(monkeypatch):

    def mock_generate_response(prompt):
        return "SELECT invalid_column FROM employees"


    monkeypatch.setattr(
        "agents.sql_agent.generate_response",
        mock_generate_response
    )

    monkeypatch.setattr(
        "agents.sql_repair.generate_response",
        mock_generate_response
    )


    result = answer_question(
        "Show employee information"
    )


    assert result["success"] is False
    assert result["repaired"] is True

def test_no_schema_retrieved(monkeypatch):

    def mock_search_schema(question):

        return {
            "documents": [[]]
        }


    monkeypatch.setattr(
        "agents.sql_agent.search_schema",
        mock_search_schema
    )


    result = answer_question(
        "Show employees"
    )


    assert result["success"] is False
    assert result["error"] == "No relevant schema found."