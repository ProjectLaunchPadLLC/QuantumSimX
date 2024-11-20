from setuptools import setup, find_packages

setup(
    name="QuantumSimX",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'numpy',  # Adding numpy as a dependency
    ],
    description="A custom quantum simulation library for educational and research purposes.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/QuantumSimX",
)
