import sys

import setuptools

if sys.version_info < (3, 6, 0):
    raise OSError(f'Streamlit requires Python 3.7 and above, but yours is {sys.version}')

try:
    with open('README.md', encoding='utf8') as fp:
        _long_description = fp.read()
except FileNotFoundError:
    _long_description = ''


setuptools.setup(
    name="streamlit-jina",
    version="0.1.2",
    author="Alex Cureton-Griffiths",
    author_email="alex.cg@jina.ai",
    description="Streamlit component for Jina neural search",
    long_description="Streamlit component for Jina neural search",
    long_description_content_type="text/plain",
    url="https://github.com/jina-ai/streamlit-jina",
    download_url='https://github.com/jina-ai/streamlit-jina/tags',
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Unix Shell',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Database :: Database Engines/Servers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Multimedia :: Video',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='jina cloud-native neural-search query search index elastic neural-network encoding '
             'embedding serving docker container image video audio deep-learning streamlit frontend',
    python_requires=">3.6",
    install_requires=["streamlit >= 0.63"],
)
