from setuptools import setup, find_packages

setup(
    name="investment_detector",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "python-dotenv>=0.19.0",
        "aiohttp>=3.8.0",
        "pyairtable>=1.3.0",
        "mistralai>=0.0.1",
    ],
    python_requires=">=3.8",
) 