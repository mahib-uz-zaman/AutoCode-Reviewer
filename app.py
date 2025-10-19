import streamlit as st
from analyzer_local import CodeAnalyzer
from validator import CodeValidator

st.set_page_config(page_title="AutoCode Reviewer", page_icon="")

st.title("AutoCode Reviewer")
st.markdown("**Paste your Python code below:**")

user_code = st.text_area("Code Input:", height=200)
review_button = st.button("Click for Review")

if review_button and user_code.strip():
    analyzer = CodeAnalyzer()
    validator = CodeValidator()

    with st.spinner("Analyzing..."):
        review_output = analyzer.analyze_code(user_code)

        syntax_check = validator.check_syntax(user_code)
        run_check = validator.run_code(user_code)

    st.subheader("AI Review & Improved Code")
    st.write(review_output)

    st.subheader("Syntax Check")
    st.info(syntax_check)

    st.subheader("Execution Result")
    st.info(run_check)
