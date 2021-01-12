import streamlit as st
from streamlit_jina import jina
st.set_page_config(page_title="Jina Text Search",)

endpoint = "http://0.0.0.0:65481/api/search"

st.title("Jina Text Search")
st.markdown("Please run our [Wikipedia search example](https://github.com/alexcg1/jina-wikipedia-sentences) to test out this search")
st.markdown("`docker run -p 65481:65481 jinahub/app.app.jina-wikipedia-sentences-30k:0.2.3-0.9.5`")

jina.text_search()
