#!/usr/bin/env python

from setuptools import find_packages, setup


def main():
    return setup(
        author="A&M",
        author_email="zhans@transport.govt.nz",
        version="1.0",
        description="openai_model",
        maintainer="A&M",
        maintainer_email="zhans@transport.govt.nz",
        name="openai_model",
        packages=find_packages(),
        data_files=[],
        zip_safe=False,
    )


if __name__ == "__main__":
    main()
