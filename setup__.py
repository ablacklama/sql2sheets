import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sql2sheets",
    version="0.0.1",
    author="Spencer Kelly",
    author_email="spencerwellskelly@gmail.com",
    description="Connect and schedule sql queries to be dumped in google sheets.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ablacklama/sql2sheets",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
    'console_scripts': [
        'sql2sheets = command_line:main'
    ],
},
)