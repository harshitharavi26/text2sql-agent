from agents.graph import run_graph


def test_full_graph():

    result = run_graph(
        "Show average salary by department"
    )


    assert result["sql"] != ""

    assert result["rows"]

    assert result["answer"] != ""