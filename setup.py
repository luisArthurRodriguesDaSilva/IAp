
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="auto-iap-enviroment",
    version="0.1.3",
    author="Luis Arthur Rodrigues da Silva",
    author_email="luisarthurlards03@gmail.com",
    description="Um pacote que integra o OpenAI GPT ao seu computados",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luisArthurRodriguesDaSilva/IAp/tree/main",
    packages=['iap'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "openai",
    ],
    python_requires='>=3.8',
    entry_points={
        "console_scripts": [
            "iap=iap.main:main",
            "setToken=iap.helpers:setToken"
        ],
    },
)
