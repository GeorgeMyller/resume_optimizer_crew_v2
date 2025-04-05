from setuptools import setup, find_packages

setup(
    name="matchcv",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "crewai",
        "python-dotenv",
        "crewai-tools"
    ],
    entry_points={
        "console_scripts": [
            "matchcv=matchcv.main:run",
        ],
    },
)
