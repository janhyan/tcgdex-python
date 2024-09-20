# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="tcgdex-python",
    version="0.0.1",
    description="Python 3 Wrapper for Trading Card Game (TCGDex) API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/janhyan/tcgdex-python",
    author="Hyan Jan Suamina",
    author_email="hyanjansuamina@gmail.com",
    classifiers=[ 
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="tcg, setuptools, development",
    package_dir={"": "src"}, 
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    install_requires=["requests"],
    project_urls={
        "Bug Reports": "https://github.com/janhyan/tcgdex-python/issues",
        "Source": "https://github.com/janhyan/tcgdex-python",
    },
)