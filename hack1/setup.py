from setuptools import setup, find_packages

setup(
    name="firstapp",
    version="0.1.0",
    packages=find_packages(),  # Automatically finds `mypackage/`
    author="Your Name",
    author_email="your.email@example.com",
    long_description_content_type="text/markdown",
    url="https://github.com/gamerpanda/firstapp",  # Change this if needed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
