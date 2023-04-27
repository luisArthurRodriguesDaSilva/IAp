import setuptools

setuptools.setup(
    name="iap",
    version="0.1",

    packages=["iap"],
    author="Luis Arthur Rodrigues da Silva",
    author_email="luisarthurlards03@gmail.com",
    description="Um pacote que integra o OpenAI GPT ao chat",
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "iap=iap.main:main",
        ],
    },
)
