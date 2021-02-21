import io
import re
from collections import OrderedDict

from setuptools import setup, find_packages

DESCRIPTION = "Easy555 admin backend"
with open("README.rst") as f:
    LONG_DESCRIPTION = f.read()

with io.open("src/easy555_admin/__init__.py", "rt", encoding="utf8") as f:
    VERSION = re.search(r"__version__ = \"(.*?)\"", f.read()).group(1)

with open('requirements/core.txt') as f:
    INSTALL_REQUIRES = f.read().splitlines()

EXTRAS_REQUIRE = {}
with open('requirements/docs.txt') as f:
    EXTRAS_REQUIRE["docs"] = f.read().splitlines()
with open('requirements/tests.txt') as f:
    EXTRAS_REQUIRE["tests"] = f.read().splitlines()

EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["docs"]

setup(
    name="easy555-admin",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    author="Daniel Xiang",
    author_email="daniel.xiang@foxmail.com",
    url="http://www.easy555.com",
    project_urls=OrderedDict(
        (
            ("Documentation", "http://www.easy555.com"),
            ("Code", "https://github.com/easy555/easy555-admin"),
            ("Issue tracker", "https://github.com/easy555/easy555-admin/issues"),
        )
    ),
    license="MIT",
    platforms=["any"],
    packages=find_packages(),
    test_suite="tests",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
