from langgraph.graph import StateGraph, START, END

from agents.state import SQLAgentState


from agents.nodes.retrieve_schema import (
    retrieve_schema_node
)

from agents.nodes.generate_sql import (
    generate_sql_node
)

from agents.nodes.validate_sql import (
    validate_sql_node
)

from agents.nodes.execute_sql import (
    execute_sql_node
)

from agents.nodes.repair_sql import (
    repair_sql_node
)

from agents.nodes.generate_answer import (
    generate_answer_node
)

workflow = StateGraph(SQLAgentState)

workflow.add_node(
    "retrieve_schema",
    retrieve_schema_node
)


workflow.add_node(
    "generate_sql",
    generate_sql_node
)


workflow.add_node(
    "validate_sql",
    validate_sql_node
)


workflow.add_node(
    "execute_sql",
    execute_sql_node
)


workflow.add_node(
    "repair_sql",
    repair_sql_node
)


workflow.add_node(
    "generate_answer",
    generate_answer_node
)

workflow.add_edge(
    START,
    "retrieve_schema"
)


workflow.add_edge(
    "retrieve_schema",
    "generate_sql"
)


workflow.add_edge(
    "generate_sql",
    "validate_sql"
)

def sql_validation_router(
    state: SQLAgentState
):
    """
    Decide whether SQL needs repair.
    """

    if state["error"]:
        return "repair_sql"

    return "execute_sql"

def execution_router(
    state: SQLAgentState
):

    if state["error"]:
        return "repair_sql"

    return "generate_answer"


workflow.add_conditional_edges(
    "validate_sql",
    sql_validation_router,
)

workflow.add_conditional_edges(
    "execute_sql",
    execution_router,
)

workflow.add_edge(
    "repair_sql",
    "execute_sql"
)

workflow.add_edge(
    "generate_answer",
    END
)

graph = workflow.compile()


def run_graph(question: str):

    initial_state = {

        "question": question,

        "schema": "",

        "sql": "",

        "original_sql": "",

        "repaired_sql": "",

        "columns": [],

        "rows": [],

        "answer": "",

        "error": "",

        "repaired": False,
    }


    return graph.invoke(initial_state)