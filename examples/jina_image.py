import streamlit as st
from streamlit_jina import jina
st.set_page_config(page_title="Jina Image Search",)

st.title("Jina Image Search")
st.markdown("Please run our [Pokemon Docker example](https://github.com/jina-ai/examples/tree/master/pokedex-with-bit#tldr-just-show-me-the-pokemon) to test out this search")
st.markdown("`docker run -p 34567:34567 -e \"JINA_PORT=34567\" jinaai/hub.app.bitsearch-pokedex search`")
jina.image_search(endpoint="http://3.140.167.7:34567/api/search")
