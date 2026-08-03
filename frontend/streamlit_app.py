import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
import pandas as pd

from agents.sql_agent import answer_question


st.set_page_config(
    page_title="Text-to-SQL Agent",
    page_icon="🤖",
)


st.title("🤖 Text-to-SQL Agent")

st.caption(
    "Ask questions about the HR database using natural language."
)


question = st.text_input(
    "Your question"
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

            result = answer_question(question)


        # Failure response
        if not result["success"]:

            st.error(
                "Unable to generate a successful answer."
            )

            with st.expander(
                "Error Details"
            ):

                st.write(
                    result["error"]
                )

                if "sql" in result:

                    st.subheader(
                        "Generated SQL"
                    )

                    st.code(
                        result["sql"],
                        language="sql"
                    )


        # Successful response
        else:

            # Answer section
            st.subheader(
                "💡 Answer"
            )

            st.text(
                result["answer"]
            )


            # Metadata
            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Rows Returned",
                    len(result["rows"])
                )

            with col2:

                if result["repaired"]:

                    st.metric(
                        "SQL Repair",
                        "Required"
                    )

                else:

                    st.metric(
                        "SQL Repair",
                        "Not Required"
                    )


            # SQL section
            with st.expander(
                "📄 View Generated SQL"
            ):

                st.code(
                    result["sql"],
                    language="sql"
                )


            # Repair details
            if result["repaired"]:

                st.warning(
                    "The original SQL failed and was repaired."
                )

                with st.expander(
                    "🔧 Repair Details"
                ):

                    st.subheader(
                        "Original SQL"
                    )

                    st.code(
                        result["original_sql"],
                        language="sql"
                    )


                    st.subheader(
                        "Original Error"
                    )

                    st.error(
                        result["original_error"]
                    )


            # Results table
            st.subheader(
                "📊 Results"
            )

            df = pd.DataFrame(
                result["rows"],
                columns=result["columns"]
            )

            st.dataframe(
                df,
                use_container_width=True
            )