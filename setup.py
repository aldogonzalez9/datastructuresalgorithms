from setuptools import setup, find_packages
 
 
 
setup(name='datastructuresalgorithms',
 
      version='0.1',
 
      url='https://github.com/aldogonzalez9/datastructuresalgorithms',
 
      license='ALDO',
 
      author='Aldo Gonzalez',
 
      author_email='aldogonzalez.campos@gmail.com',
 
      description='Python data structures and algorithms book samples',
 
      packages=find_packages(exclude=['tests']),
 
      long_description=open('README.md').read(),
 
      zip_safe=False,
 
      setup_requires=['nose>=1.0'],
 
      test_suite='nose.collector')