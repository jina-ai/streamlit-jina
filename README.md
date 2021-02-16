# streamlit-jina

<!--
![Python package](https://github.com/randyzwitch/streamlit-jina/workflows/Python%20package/badge.svg)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/randyzwitch/streamlit-jina/examples/streamlit_app.py)
-->

streamlit-jina lets you search text or images in your Streamlit app, using [Jina's neural search framework](https://github.com/jina-ai/jina/).

## Installation

streamlit-jina is distributed via [PyPI](https://pypi.org/project/streamlit-jina/):

```python
pip install streamlit-jina
```

## Examples

Using streamlit-jina is as simple as setting an endpoint and what type of thing you want to search for:

```python
import streamlit as st
from streamlit_jina import jina
```

And then choose your search type and plug in your endpoint:

### Text ([example](https://github.com/jina-ai/streamlit-jina/blob/main/examples/jina_text.py))

```python
jina.text_search(endpoint="http://0.0.0.0:45678/api/search")
```

![](https://github.com/jina-ai/streamlit-jina/raw/main/.github/images/text.gif)

### Images ([example]())

```python
jina.image_search(endpoint="http://0.0.0.0:45678/api/search")
```

![](https://github.com/jina-ai/streamlit-jina/raw/main/.github/images/images.gif)

### Parameters

You can pass several parameters to the component:

| Parameter  | Type   | Details                                                 |          |
| ---        | ---    | ---                                                     | ---      |
| `endpoint` | `str`  | Endpoint of your Jina instance                          | Required |
| `top_k`    | `int`  | How many results you want returned                      | Optional |
| `hidden`   | `list` | Widgets you want hidden from user (`endpoint`, `top_k`) | Optional |

## Todo

- Canvas drawing as input
- Audio/video file upload input
- Audio/video recording input
- Audio/video output widgets
