import streamlit as st
import streamlit.components.v1 as components
import requests
from PIL import Image
import base64
from io import BytesIO

headers = {
    "Content-Type": "application/json",
}

endpoint = 'http://0.0.0.0:65481/api/search'

class Encoder:
    def img_base64(byte_string):
        output = str(base64.b64encode(byte_string))[2:-1]
        output = f'["data:image/png;base64,{output}"]'

        return output

    def canvas_to_base64(data):
        if data is not None:
            if data.image_data is not None:
                img_data = data.image_data
                im = Image.fromarray(img_data.astype("uint8"), mode="RGBA")
                buffered = BytesIO()
                im.save(buffered, format="PNG")
                img_str = base64.b64encode(buffered.getvalue())
                output = str(img_str)[2:-1]
                encoded_query = f'["data:image/png;base64,{output}"]'

        return encoded_query


class Getter:
    def images(query: str, top_k: int, endpoint: str) -> list:
        data = '{"top_k":' + str(top_k) + ', "mode": "search", "data":' + query + "}"
        response = requests.post(endpoint, headers=headers, data=data)

        content = response.json()["search"]["docs"][0]["topkResults"]
        results = []
        for doc in content:
            img = doc["matchDoc"]["uri"]
            results.append(img)

        return results

    def text(query: str, top_k: int, endpoint: str) -> list:
        data = f'{{"top_k": {top_k}, "mode": "search", "data": ["text:{query}"]}}'
        response = requests.post(endpoint, headers=headers, data=data)

        content = response.json()["search"]["docs"]
        results = []
        for doc in content:
            matches = doc["matches"] #list
            for match in matches:
                results.append(match["text"])


        return results


class Renderer:
    def images(results: list) -> str:
        output = ""
        for doc in results:
            html = f'<img src="{doc}">'
            output += html

        return output

    def text(results: list) -> str:
        header = """
        | Name | Line |
        | ---  | ---  |
        """
        output = header
        for text in results:
            character, words = text.split("[SEP]")
            result_text = f"| **{character}** | {words} |\n"
            output += result_text

        return output

class text:
    class results:
        def markdown(query, top_k, endpoint):
            raw_results = Getter.text(query, top_k, endpoint)
            output = Renderer.text(raw_results)
            return st.markdown(output)

        def raw(query, top_k, endpoint):
            raw_results = Getter.text(query, top_k, endpoint)
            return raw_results

class image:
    class results:
        def render(query, top_k, endpoint):
            encoded_query = Encoder.img_base64(query.read())
            results = Getter.images(encoded_query, top_k, endpoint)
            output = Renderer.images(results)
            return st.markdown(output, unsafe_allow_html=True)

# class canvas:
    # def encoder(data):
        # if data is not None:
            # if data.image_data is not None:
                # img_data = data.image_data
                # im = Image.fromarray(img_data.astype("uint8"), mode="RGBA")
                # buffered = BytesIO()
                # im.save(buffered, format="PNG")
                # img_str = base64.b64encode(buffered.getvalue())
                # output = str(img_str)[2:-1]
                # encoded_query = f'["data:image/png;base64,{output}"]'
                # output = Renderer.images(encoded_query)

        # return encoded_query


class jina:
    def text_search(endpoint="", top_k=10, output="raw", hidden=[]):
        container = st.beta_container()
        with container:
            # Show input widgets
            if "endpoint" not in hidden:
                endpoint = st.text_input("Endpoint", "http://0.0.0.0:65481/api/search")
            else:
                endpoint = endpoint

            query = st.text_input("Enter query")
            if "top_k" not in hidden:
                top_k = st.slider("Results", 1, top_k, int(top_k/2))
            else:
                top_k = top_k
            button = st.button("Search")

            if button:
                if output == "markdown":
                    text.results.markdown(endpoint=endpoint, query=query, top_k=top_k)
                elif output == "raw":
                    st.write(text.results.raw(endpoint=endpoint, query=query, top_k=top_k))

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
                top_k = st.slider("Results", 1, top_k, int(top_k/2))
            else:
                top_k = top_k
            button = st.button("Search")

            if button:
                image.results.render(query=query, endpoint=endpoint, top_k=top_k)

        return container
