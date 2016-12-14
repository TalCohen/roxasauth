from setuptools import setup

setup(
    name="roxasauth",
    description="Authentication API for Roxas",
    author="Tal Cohen",
    author_email="tcohen123@gmail.com",
    url="https://github.com/TalCohen/roxasauth",
    version="1.0.0",
    license="GPLv3",
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="development ibutton nfc csh roxas",
    py_modules=["roxasauth"],
    install_requires=["requests"],
)
