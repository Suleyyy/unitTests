import os

from setuptools import find_packages, setup

with open("requirements.txt", encoding='utf-8', errors='replace') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('��')]

version = os.getenv(
    "VERSION", "0.0.0"
)  # Fallback to '0.0.0'version = os.getenv('PACKAGE_VERSION', '0.0.0')  # Fallback to '0.0.0'



setup(
    name="unitTests_ms",
    version=version,
    author="Mikołaj Sulkowski",
    author_email="mikolaj.sulkowski@edu.uekat.pl",
    description="Repo deploy",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Suleyyy/unitTests.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)