from setuptools import setup, find_packages

setup(
    name='pinyin_tools',
    packages=["pinyin_tools"],
    package_dir={"":"src"},
    url='https://github.com/Bowowzahoya/pinyin_tools',
    description='Tools for dealing with pinyin strings.',
    long_description=open('README.txt', encoding="utf-8").read(),
    install_requires=[
        "re",
        "pytest"
        ],
    include_package_data=True,
)