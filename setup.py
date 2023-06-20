import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tmd2023py",
    version="0.0.1",
    author="masaaki-kotera",
    author_email="maskot1977@gmail.com",
    description="tmd2023py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maskot1977/tmd2023py/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['sample_command = sample_command.sample_command:main']
    },
    python_requires='>=3.6',
)
