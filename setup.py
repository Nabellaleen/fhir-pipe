from setuptools import setup

setup(
    name='fhirpipe',
    version='0.1',
    description='The smart ETL to standardize health data',
    url='https://github.com/arkhn/fhir-pipe',
    author='Théo Ryffel',
    author_email='theo@arkhn.org',
    license='Apache License 2.0',
    packages=['fhirpipe'],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'fhirpipe-run=fhirpipe.console.run:run',
            'fhirpipe-batchrun=fhirpipe.console.run:batch_run',
        ],
    },
)
