import setuptools
import os

setuptools.setup(
    name="genencoder",
    version="4.20",
    author="Jakob S. Kottmann",
    author_email="jakob.kottmann@utoronto.ca",
    packages=["genencoder"],
    package_dir={"": "src/"},
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: Hopefully OS Independent",
    ),
    #install_requires=["tequila-basic"], # won't enforce this

)
