from setuptools import setup

setup(
    name='umd_python_cas',
    version='1.0.0',
    description='A python client to access the University of Maryland Central Authentication Services (CAS) remote instance.',
    url='https://github.com/umd-python-cas/umd-python-cas',
    author='Jacob (Coby) Winfield',
    author_email='coby.winfield@gmail.com',
    license='MIT',
    packages=['umd_python_cas'],
    install_requires=['urllib3',
                      'xmltodict',
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
