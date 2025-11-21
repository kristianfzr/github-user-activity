from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name="github-user-activity",
    version="1.0.0",
    author="Kristian Kanchev",
    description="A CLI task tracker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kristianfzr/github-user-activity",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "github-user-activity=github_user_activity.cli:main",
        ],
    },
)