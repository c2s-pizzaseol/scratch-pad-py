import setuptools
from distutils.core import setup


with open("README.md", "r", encoding="utf-8") as f:
    long_descriprion = f.read()

setuptools.setup(
    name             = 'pyscratchpad',
    version          = '0.0.2',
    description      = 'python logger libary',
    long_description = long_descriprion,
    long_description_content_type = "text/markdown",
    author           = 'chirichidi',
    author_email     = 'tolessnoise@gmail.com',
    url              = "https://github.com/chirichidi/scratch-pad-py",
    packages         = ["scratch_pad_py"],
    install_requires=[
        'thrift==0.16.0',
        'requests==2.28.1',
        'facebook-scribe==2.0.post1',
        'fluent-logger==0.10.0'
    ],
    keywords         = ['logger'],
    python_requires  = '>=3.7',
    classifiers      = [
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)