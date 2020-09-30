"""Setup Requirements."""
import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="Multiplicative Persistence Tools",
    version="0.9",
    author="Erwin van Eijk",
    author_email="235739+erwinvaneijk@users.noreply.github.com",
    description="Tools to find the mp-order of natural numbers.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    scripts=['find_all.py', 'list_all.py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>3.6',
)
