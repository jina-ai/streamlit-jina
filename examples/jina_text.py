import streamlit as st
from streamlit_jina import jina
st.set_page_config(page_title="Jina Text Search",)

endpoint = "http://0.0.0.0:45678/api/search"

st.title("Jina Text Search")
st.markdown("You can run our [Wikipedia search example](https://github.com/jina-ai/examples/tree/master/wikipedia-sentences) to test out this search")

jina.text_search(endpoint=endpoint)
