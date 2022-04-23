from setuptools import setup, find_packages

setup(
    name="tslabel_weak",
    packages=find_packages(exclude=["notebooks", "docs"]),
    version='beta',
    author='Ivan José dos Reis Filho, Rodrigo Neves Trindade',
    author_email='ivanfilhoreis@gmail.com, rodrigonevest@gmail.com',
    
    url='https://github.com/ivanfilhoreis/tslabel_weak',
    
    classifiers=[
        'Programming Language :: Python',
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires='>=3.6',
)