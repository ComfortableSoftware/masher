

#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of CF.setup.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


from setuptools import find_packages
from setuptools import setup


setup(
  author="GaelicGrime",
  author_email="will.angus.blaylock@gmail.com",
  license="GPLv3",
  name="_PROJECT_NAME_",
  url="https://github.com/ComfortableSoftware/_PROJECT_NAME_",
  version="0.0.1",
  package_dir={"_PROJECT_NAME_": "_PROJECT_NAME_"},
  package_data={
      "_PROJECT_NAME_": [
          "../doc/*",
      ]
  },
  packages=["_PROJECT_NAME_"],
  install_requires=[
      "CS-CF",
  ],
  extras_require={
  },
  scripts=["scripts/_PROJECT_NAME_"],
)
