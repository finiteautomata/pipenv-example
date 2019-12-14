import setuptools

setuptools.setup(
    name="mypackage", # Replace with your own username
    version="0.0.1",
    author="John Doe",
    author_email="author@example.com",
    description="A small example package using Pipenv",
    url="https://github.com/finiteautomata/pipenv-sample",
    packages=setuptools.find_packages(),
    install_requires=[
        'flask==0.12.1',
        'numpy==1.17.4',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
