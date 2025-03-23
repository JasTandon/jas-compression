### setup.py
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jas-compression",
    version="1.0.0",
    author="Your Name",
    author_email="youremail@example.com",
    description="A custom text compression library using tokenization and Huffman encoding.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/jas-compression",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "tqdm",
        "PyYAML",
    ],
)