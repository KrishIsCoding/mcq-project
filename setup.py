from setuptools import setup, find_packages


setup(

    name='mcqgenerator',
    version='0.1.0',
    author='Krish gautam',
    author_email="gautamkrish445@gmail.com",
    packages=find_packages(),
    install_requires=[
        'openai',
        'langchain',
        'streamlit',
        'python-dotenv',
        'PyPDF2']



)