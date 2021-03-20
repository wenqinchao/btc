import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="src",
  version="0.0.1",
  author="Wen",
  author_email="wenqinchao@gmail.com",
  description="A package interact with bitcoin node",
  long_description=long_description,
  license="MIT",
  url="https://github.com/wenqinchao/btc",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)