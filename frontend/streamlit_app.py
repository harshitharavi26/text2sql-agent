import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from agents.sql_agent import answer_question


st.set_page_config(
    page_title="Text-to-SQL Agent",
    page_icon="🤖",
)

st.title("Text-to-SQL Agent")

question = st.text_input(
    "Ask a question about the HR database"
)

if st.button("Generate Answer"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:
        with st.spinner("Generating SQL and retrieving results..."):
            result = answer_question(question)

        st.subheader("Generated SQL")
        st.code(result["sql"], language="sql")

        if not result["success"]:
            st.error(result["error"])

        else:
            if result["repaired"]:
                st.info(
                    "The original SQL failed and was repaired."
                )

            st.subheader("Results")

            rows = [
                dict(zip(result["columns"], row))
                for row in result["rows"]
            ]

            st.dataframe(
                rows,
                use_container_width=True,
            )