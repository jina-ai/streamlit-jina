import setuptools

setuptools.setup(
    name="streamlit-jina",
    version="0.1.1",
    author="Jina AI",
    author_email="alex.cg@streamlit.io",
    description="Streamlit component for Jina neural search",
    long_description="Streamlit component for Jina neural search",
    long_description_content_type="text/plain",
    url="https://github.com/randyzwitch/streamlit-embedcode",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=["streamlit >= 0.63"],
)
