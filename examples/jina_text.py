import streamlit as st
from streamlit_jina import jina
st.set_page_config(page_title="Jina Text Search",)

st.title("Jina Text Search")
st.markdown("Please run our [South Park Docker example](https://github.com/jina-ai/examples/tree/master/southpark-search#try-out-this-demo-by-yourself) to test out this search")
st.markdown("`docker run -p 45678:45678 jinaai/hub.app.distilbert-southpark:latest`")

jina.text_search(endpoint="http://0.0.0.0:45678/api/search")
