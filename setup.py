from setuptools import setup, find_packages
from lightorch import __author__, __email__, __version__
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

if __name__ == "__main__":
    setup(
        name="greentorch",
        version=__version__,
        packages=find_packages(),
        author=__author__,
        long_description=long_description,
        long_description_content_type="text/markdown",
        author_email=__email__,
        description="Pytorch based framework for PDE solving with Green's functions.",
        url="https://github.com/Jorgedavyd/GreenTorch",
        license="Apache License 2.0",
        install_requires=["lightning", "torch", "lightorch"], # define
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Scientific/Engineering :: Information Analysis",
            "Topic :: Scientific/Engineering :: Mathematics",
            "Topic :: Scientific/Engineering",
            "Topic :: Software Development",
            "Topic :: Software Development :: Libraries",
            "Topic :: Software Development :: Libraries :: Python Modules"
        ],
    )
