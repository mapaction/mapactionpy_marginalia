from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()
		
setup(name='mapactionpy_marginalia',
      version='0.1',
      description='Generate items that go in the marginalia of maps and infographics',
      url='http://github.com/mapaction/mapactionpy_marginalia',
      author='MapAction',
      author_email='github@mapaction.com',
      license='GPL3',
      packages=['mapactionpy_marginalia'],
	  test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)