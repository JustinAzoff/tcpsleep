from setuptools import setup, find_packages

setup(name="tcpsleep",
    version="1.0",
    author="Justin Azoff",
    author_email="JAzoff@uamail.albany.edu",
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    entry_points = {
        'console_scripts': [
            'tcpsleep   = tcpsleep.server:main',
        ]
    },
    test_suite='nose.collector',
)
