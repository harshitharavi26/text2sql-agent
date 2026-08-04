from agents.nodes.retrieve_schema import retrieve_schema_node


def test_retrieve_schema():

    state = {
        "question": "Show employees by department"
    }

    result = retrieve_schema_node(state)

    assert "schema" in result
    assert result["schema"] != ""