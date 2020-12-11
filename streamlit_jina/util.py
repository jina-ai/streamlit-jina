__copyright__ = "Copyright (c) 2020 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

import requests
from PIL import Image
import base64
from io import BytesIO

default_top_k = 10

headers = {
    "Content-Type": "application/json",
}


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

        content = response.json()["search"]["docs"][0]["topkResults"]
        results = []
        for doc in content:
            text = doc["matchDoc"]["text"]
            results.append(text)

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


class Defaults:
    text_query = "Hello world"
    endpoint = "http://3.140.167.7:34567/api/search"
    error = "**Error**: Please check your endpoint is available and that your media type is correct"
    jina_text = """
    <center>
    <a href="https://www.github.com/jina-ai/jina">Jina on GitHub</a> •
    <a href="https://github.com/jina-ai/jina/tree/master/docs/chapters/101">Jina 101</a> •
    <a href="https://github.com/jina-ai/integration-streamlit-advanced/">Code for This Project</a>
    <center>
    """
