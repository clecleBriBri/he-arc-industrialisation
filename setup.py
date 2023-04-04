from setuptools import find_packages, setup

setup(
    name="TP2",
    version="0.3.0",
    description="Travail pratique sur la qualité de code et le CI/CD",
    # long_description=open("README.md", encoding="utf-8").read(),
    author="clement.brigliano",
    package_dir={"TP2": "src"},
    install_requires=open("requirements.txt").readlines()
)
