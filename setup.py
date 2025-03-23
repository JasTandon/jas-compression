import setuptools

setuptools.setup(
    name="jas",
    version="1.0.0",
    author="Jas Tandon",
    author_email="jastandon@icloud.com",
    description="A custom text compression library using tokenization and Huffman encoding.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JasTandon/jas-compression",
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
    license_files=["LICENSE"],
)