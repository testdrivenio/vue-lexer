import io
import os

from setuptools import setup, find_packages


VERSION = '0.0.4'
here = os.path.abspath(os.path.dirname(__file__))
README = io.open(os.path.join(here, 'README.md'), encoding="utf8").read()

setup(
    name='vue-lexer',
    description='A Vue lexer for Pygments',
    long_description=README,
    long_description_content_type="text/markdown",
    version=VERSION,
    url='https://github.com/testdrivenio/vue-lexer',
    author='Michael Herman',
    author_email='michael@mherman.org',
    classifiers=[
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3'
    ],
    keywords='pygments highlight vue',
    install_requires=[
        'Pygments >= 2.3'
    ],
    test_suite='tests',
    license='MIT License',
    packages=find_packages(exclude=["docs", "tests", "tests.*"]),
    entry_points="""
        [pygments.lexers]
        vue=vue:VueLexer
    """
)
