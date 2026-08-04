import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from agents.graph import run_graph


st.set_page_config(
    page_title="Text-to-SQL Agent",
    page_icon="🤖",
)


st.title("🤖 Text-to-SQL Agent")


question = st.text_input(
    "Ask a question about the HR database"
)


if st.button("Generate Answer"):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Generating answer..."
        ):

            result = run_graph(question)


        # Error handling
        if result["error"]:

            st.error(
                "Unable to generate a successful answer."
            )

            st.subheader("Error")

            st.write(
                result["error"]
            )


            if result.get("sql"):

                st.subheader(
                    "Generated SQL"
                )

                st.code(
                    result["sql"],
                    language="sql"
                )


        else:

            # Natural language answer
            st.subheader("Answer")

            st.markdown(
            f"""
            <div style="
                font-size:18px;
                color:white;
                line-height:1.6;
            ">
                {result["answer"]}
            </div>
            """,
            unsafe_allow_html=True
        )


            # Generated SQL
            st.subheader(
                "Generated SQL"
            )

            st.code(
                result["sql"],
                language="sql"
            )


            # Repair information
            if result["repaired"]:

                st.info(
                    "The original SQL failed and was repaired."
                )

                with st.expander(
                    "Repair Details"
                ):

                    if "original_sql" in result:

                        st.write(
                            "Original SQL"
                        )

                        st.code(
                            result["original_sql"],
                            language="sql"
                        )


                    if "original_error" in result:

                        st.write(
                            "Original Error"
                        )

                        st.error(
                            result["original_error"]
                        )


            # Results table
            st.subheader(
                "Results"
            )


            rows = [
                dict(zip(result["columns"], row))
                for row in result["rows"]
            ]


            st.dataframe(
                rows,
                use_container_width=True
            )