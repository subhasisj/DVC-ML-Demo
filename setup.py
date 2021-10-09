from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="src",
    version="0.0.1",
    author="subhasisj",
    description="Sample package for DVC based ML Pipeline",
    long_description=long_description,
    url="https://github.com/subhasisj/DVC-ML-Demo",
    author_email="subhasis.jethy@gmail.com",
    packages=["src"],
    license="BSD",
    python_requires=">=3.7",
    install_requires=["dvc", "pandas", "scikit-learn"],
)
