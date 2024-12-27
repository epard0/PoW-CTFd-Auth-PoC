from setuptools import setup, find_packages

setup(
    name="PoW-CTFd",
    version="0.1.0",
    author="Evan Pardon (supasuge)",
    author_email="epardo1742@proton.me",
    description="Python package to easily solve proof-of-work challenges for GrizzHacks CTF 2025",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/supasuge/PoW-CTFd",  # Replace with your private repo URL
    packages=find_packages(),  # Automatically find packages in `PoW/`
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=[],
)
