import setuptools

with open("README.md", 'r') as file_handler:
    long_description  = file_handler.read()

setuptools.setup(
    name="comms-utils",
    version="0.0.2",
    author="Jos Craw",
    author_email="jos@joscraw.net",
    description="A set of tools for the ENEL422 Comms Assignment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.sys-io.net/scm/enel422/comms-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)