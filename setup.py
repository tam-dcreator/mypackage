from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # Specify the content type for long description
    install_requires=['numpy'],
    setup_requires=['setuptools>=65.5.1'], # Package installs properly on this version
    url='https://github.com/tam-dcreator/mypackage>',
    author='tam-dcreator',
    author_email='thebeginning724@gmail.com'
)

