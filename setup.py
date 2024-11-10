# setup.py
from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1.0',
    description='A simple math quiz game with random questions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Muhammad Suhaib',
    author_email='isuhaibsalarzai@gmail.com',
    url='https://github.com/suhaibsalarzai/dsss_homework_2.git',  # replace with your GitHub repo URL
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
