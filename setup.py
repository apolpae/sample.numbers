from setuptools import setup

setup(
    name='sample_numbers',
    version='1.0',
    description='Sample program generating an equation from a vocabulary and a given result',
    author='Ivan Voevodov',
    author_email='notifmail@icloud.com',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'sample_numbers=sample_numbers.__main__:main'
        ]
    }
)
