from setuptools import setup, find_packages

setup(
    name="genai_2083",
    version="0.1.0",
    author="TheAIRhishi",
    description="Reproducible AI Research Repository",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "numpy>=1.24.3",
        "pandas>=2.0.2",
        "scikit-learn>=1.3.0",
    ],
)