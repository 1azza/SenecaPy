import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name="SenecaPy", # Replace with your username

    version="1.0.0",

    author="1azza",

    author_email="rennoldsonlarry@gmail.com",

    description="Seneca package",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="<https://github.com/authorname/templatepackage>",

    packages=setuptools.find_packages(),

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

    python_requires='>=3.6',
)