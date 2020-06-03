from setuptools import find_packages, setup
from package import Package

setup(name='eyezmi',
      version='0.1.0',
      author='eye',
      author_email='eye@example.com',
      packages=find_packages(),
      include_package_data=True,
      cmdclass={
            "package": Package
      }
      )
