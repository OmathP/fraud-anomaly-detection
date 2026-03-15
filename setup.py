from setuptools import setup, find_packages


setup(
    name='fraud_anomaly_detection',
    packages=find_packages(),
    version="1.0",
    license="",
    install_requires = [
        "kagglehub",
        "kaggle",
        "pandas",
        "gdown"
    ]
)
