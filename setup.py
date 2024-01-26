

from setuptools import find_packages
from setuptools import setup
from Cython.Build import cythonize


# pylint: disable=W0105
'''
setup(
    name='Hello world app',
    ext_modules=cythonize("hello.pyx"),
)

# pylint: disable=e0611
from hello import sayHello


sayHello()

'''


setup(
  author="GaelicGrime",
  author_email="will.angus.blaylock@gmail.com",
  license="GPLv3",
  name="masher",
  url="https://github.com/ComfortableSoftware/masher",
  version="0.0.1",
  package_dir={"masher": "masher"},
  package_data={
      "masher": [
          "../doc/*",
      ]
  },
  packages=find_packages(),
  install_requires=[
      "CSCF",
  ],
  extras_require={
  },
  #scripts=["scripts/masher"],
)
