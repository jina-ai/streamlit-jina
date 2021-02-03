import streamlit as st
from streamlit_jina import jina
st.set_page_config(page_title="Jina Image Search",)

endpoint = "http://0.0.0.0:45678/api/search"

st.title("Jina Image Search")
st.markdown("You can run Jina's [Pokemon Docker example](https://github.com/jina-ai/examples/tree/master/pokedex-with-bit#tldr-just-show-me-the-pokemon) to test out this search")

jina.image_search(endpoint=endpoint)
