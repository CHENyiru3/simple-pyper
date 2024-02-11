from setuptools import setup
from setuptools import setup, find_packages

setup(
    name='pyreader',
    version='1.0',
    py_modules=find_packages(),
    url='https://github.com/your_username/pyreader',
    license='MIT',
    author='Your Name',
    author_email='your_email@example.com',
    description='A package for reading files in Python.',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        'numpy',
        'pandas',
    ],
)
