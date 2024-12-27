import streamlit as st
import requests
import os

PAGE_TITLE = os.getenv("PAGE_TITLE", "Query Interface")

st.set_page_config(
    page_title="PAGE_TITLE",
    page_icon="🤖",
    layout="wide"
)

st.title(f"🤖 {PAGE_TITLE}")

API_URL = os.getenv("API_URL", "http://localhost:8000/answer")
URL_PARAM = os.getenv("URL_PARAM", "query")

st.header("📝 Ask a Question")

query = st.text_input("Enter your query:", placeholder="Type something...")


if st.button("Submit Query"):
    if query:
        with st.spinner("Processing your query..."):
            try:
                response = requests.get(
                    f"{API_URL}",
                    params={f"{URL_PARAM}": query}
                )
                if response.status_code == 200:
                    result = response.text
                    st.success("Query Processed Successfully!")
                    st.write("### 🎯 Result:")
                    st.markdown(result)
                else:
                    st.error(f"Failed with status code {response.status_code}")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a query before submitting.")

st.markdown("---")
