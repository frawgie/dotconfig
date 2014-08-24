from setuptools import setup, find_packages

setup(
        name="DotConfig",
        version="0.1.1",
        author="Jonas Ericsson",
        author_email="jonas@agilefrog.se",
        py_modules = ["dotconfig"],
        url="http://github.com/frawgie/dotconfig",
        license="LICENSE.txt",
        description="A simpler way to read configuration files.",
        long_description=open("README.txt").read(),
        install_requires=[],
)
