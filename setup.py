from setuptools import find_packages, setup

setup(
    name="sample-python-calculator",
    version="1.0.0",
    author="Devskiller.com",
    author_email="support@devskiller.com",
    packages=find_packages(),
    test_suite="test",
    tests_require=[
        "nose",
    ],
)
