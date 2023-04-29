
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iap",
    version="0.1",
    author="Luis Arthur Rodrigues da Silva",
    author_email="luisarthurlards03@gmail.com",
    description="Um pacote que integra o OpenAI GPT ao seu computador",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seu-usuario/meu-pacote",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "openai",
    ],
    entry_points={
        "console_scripts": [
            "iap=iap.main:main",
            "setToken=iap.helpers:setToken"
        ],
    },
)
