import setuptools


setuptools.setup(
    name = "ysApi",
    version = "1.2",
    author = "Yousign",
    packages=['ysApi'],
    #packages=setuptools.find_packages(),
    # Project uses suds
    # installed or upgraded on the target machine
    install_requires = ['suds-jurko>=0.4']
)
