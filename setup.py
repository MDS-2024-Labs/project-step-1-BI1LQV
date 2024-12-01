from setuptools import setup
from version import VERSION

setup(
    name='reactive-python',  # package name
    version="0.1.0",  # package version
    description='A simple reactive programming library',  # package description
    packages=['reactive'],
    # package_dir={"": "src"},
    zip_safe=False,
    author="yunfan, jiahao",
    author_email="bi1lqy.y@gmail.com",
    license="MIT",
    install_requires=[]
)
