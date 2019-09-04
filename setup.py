import setuptools

REQUIRED = [
    "numpy",
    "pandas",
    "scikit-learn"
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata-noreallyimfine", 
    version="0.0.11",
    author="Avraham Jacobsohn",
    author_email="noreallyimfine@users.noreply.github.com",
    description="Data Science helper functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/noreallyimfine/lambdata",
    packages=setuptools.find_packages(),
    instal_requires = REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

