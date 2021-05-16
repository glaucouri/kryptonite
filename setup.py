import setuptools
from kryptonite import version

with open("README.md", "rt") as fh:
    long_description = fh.read()

with open("requirements.txt",'rt') as fn:
    reqs = fn.read().split()

setuptools.setup(
    name="kryptonite",
    version=version,
    author="Glauco Uri",
    author_email="glauco@uriland.it",
    description="A near real time symbol collector for crypto values.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/glaucouri/kryptonite",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
    ],
    python_requires='>=3.6',
    install_requires = reqs,
    entry_points={
            'console_scripts': [
                'krypto = kryptonite.cmd:cli'
          ]}
)