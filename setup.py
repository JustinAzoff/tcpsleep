from setuptools import setup, find_packages

setup(name="tcpsleep",
    version="1.1",
    author="Justin Azoff",
    author_email="JAzoff@uamail.albany.edu",
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    entry_points = {
        'console_scripts': [
            'tcpsleep   = tcpsleep.server:main',
        ]
    },
    extras_require = {
        'docs' : ['sphinx'],
    },
    setup_requires=[
        "nose",
    ],
    test_suite='nose.collector',
)
