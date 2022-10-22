from setuptools import setup

setup(
    name='audioserver',
    version='0.1.0',
    packages=['audioserver'],
    include_package_data=True,
    install_requires=[
        'arrow',
        'bs4',
        'Flask',
        'pycodestyle',
        'pydocstyle',
        'pylint',
        'pytest',
        'pytest-mock',
        'requests',
    ],
    python_requires='>=3.8',
)