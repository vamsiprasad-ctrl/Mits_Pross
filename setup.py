from setuptools import setup, find_packages

setup(
    name="vvs",
    version="0.1.0",
    author="VVS",
    author_email="vamsipuram844@gmail.com",
    description="A package to calculate Jaccard, Overlap, and Hamming similarity metrics between strings.",  # Short description
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vvs/vvs",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
