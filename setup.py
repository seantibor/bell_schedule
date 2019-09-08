import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bell_schedule",
    version="0.0.2",
    author="Sean Tibor",
    author_email="sean.tibor@pinecrest.edu",
    description="a middle school bell schedule library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seantibor/bell_schedule",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'python-dateutil>=2.8.0',
        'iso8601>=0.1.12'
    ]
)
