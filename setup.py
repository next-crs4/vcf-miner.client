from setuptools import setup

AuthorInfo = (
    ("Atzeni Rossano", "ratzeni@crs4.it"),
)

setup(name = "vcfminerclient",
      version = '0.1',
      description = "client package for VCFMiner",
      author = ",".join(a[0] for a in AuthorInfo),
      author_email = ",".join("<%s>" % a[1] for a in AuthorInfo),
      install_requires = [],
      packages = ['vcfminerclient'],
      license = 'MIT',
      platforms = "Posix; MacOS X; Windows",
      classifiers = ["Development Status :: 3 - Alpha",
                     "Intended Audience :: Developers",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                     "Topic :: Internet",
                     "Programming Language :: Python :: 2.7"],
)
