import streamlit as st
import streamlit.components.v1 as components
import requests
from PIL import Image
import base64
from io import BytesIO

headers = {
    "Content-Type": "application/json",
}

# Set default endpoint. Usually this would be passed to a function via a parameter
endpoint = "http://0.0.0.0:45678/api/search"

class text:
    """
    Jina text search
    """
    class process:
        """
        Process query and results
        """
        def json(query: str, top_k: int, endpoint: str) -> list:
            """
            Process Jina's JSON output and parse results
            """
            data = f'{{"top_k": {top_k}, "mode": "search", "data": ["{query}"]}}'
            response = requests.post(endpoint, headers=headers, data=data)

            content = response.json()["search"]["docs"]
            results = []
            for doc in content:
                matches = doc["matches"]  # list
                for match in matches:
                    results.append(match["text"])

            return results

    class render:
        """
        Render results
        """
        def raw(query, top_k, endpoint):
            """
            Render raw JSON
            """
            raw_results = text.process.json(query, top_k, endpoint)
            return raw_results


class image:
    """
    Jina image search
    """
    class encode:
        """
        Encode image
        """
        def img_base64(byte_string):
            """
            Encode image file to base64
            """
            output = str(base64.b64encode(byte_string))[2:-1]
            output = f'["data:image/png;base64,{output}"]'

            return output

    class render:
        """
        Render image output
        """
        def html(results: list) -> str:
            """
            Render images as list of HTML img tags
            """
            output = ""
            for doc in results:
                html = f'<img src="{doc}">'
                output += html

            return output

        def markdown(query, top_k, endpoint):
            """
            Renders images as markdown output
            """
            encoded_query = image.encode.img_base64(query.read())
            # results = image.process.json(encoded_query, top_k, endpoint)
            results = image.process.json(encoded_query, top_k, endpoint)
            output = image.render.html(results)
            return st.markdown(output, unsafe_allow_html=True)

    class process:
        def json(query: str, top_k: int, endpoint: str) -> list:
            data = (
                '{"top_k":' + str(top_k) + ', "mode": "search", "data":' + query + "}"
            )
            response = requests.post(endpoint, headers=headers, data=data)

            content = response.json()["search"]["docs"]
            results = []
            for doc in content:
                matches = doc["matches"]
                for match in matches:
                    results.append(match["uri"])

            return results


class jina:
    def text_search(endpoint="", top_k=10, output="raw", hidden=[]):
        container = st.beta_container()
        with container:
            if "endpoint" not in hidden:
                endpoint = st.text_input("Endpoint", endpoint)
            else:
                endpoint = endpoint

            query = st.text_input("Enter query")
            if "top_k" not in hidden:
                top_k = st.slider("Results", 1, top_k, int(top_k / 2))
            else:
                top_k = top_k
            button = st.button("Search")

            if button:
                st.write(text.render.raw(endpoint=endpoint, query=query, top_k=top_k))

        return container

    def image_search(endpoint="", top_k=10, hidden=[]):
        container = st.beta_container()
        with container:
            # Show input widgets
            if "endpoint" not in hidden:
                endpoint = st.text_input("Endpoint", endpoint)
            else:
                endpoint = endpoint

            query = st.file_uploader("Upload file")

            if "top_k" not in hidden:
                top_k = st.slider("Results", 1, top_k, int(top_k / 2))
            else:
                top_k = top_k
            button = st.button("Search")

            if button:
                image.render.markdown(query=query, endpoint=endpoint, top_k=top_k)

        return container
