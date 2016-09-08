from setuptools import setup, find_packages
import versioneer

setup(
    name='anaconda-client',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='Sean Ross-Ross',
    author_email='srossross@gmail.com',
    url='http://github.com/Anaconda-Platform/anaconda-client',
    description='Anaconda Cloud command line client library',
    packages=find_packages(),
    install_requires=['clyent',
                      'requests>=2.9.1',
                      'pyyaml',
                      'python-dateutil',
                      'pytz'],
    entry_points={
        'console_scripts': [
            'anaconda = binstar_client.scripts.cli:main',
            'binstar = binstar_client.scripts.cli:main',
            'conda-server = binstar_client.scripts.cli:main'
        ]
    },
    license='BSD License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ]
)
