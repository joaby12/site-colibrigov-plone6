"""Installer for the site_plone6 package."""
from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.md").read(),
        open("CONTRIBUTORS.md").read(),
        open("CHANGES.md").read(),
    ]
)


setup(
    name="site_plone6",
    version="1.0a1",
    description="site_plone6 configuration package.",
    long_description=long_description,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="Joaby Souto",
    author_email="joaby@colibrigov.com",
    url="https://github.com/https://github.com/https://github.com/joaby12/site_plone6",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/site_plone6",
        "Source": "https://github.com/https://github.com/joaby12/site_plone6",
        "Tracker": "https://github.com/https://github.com/joaby12/site_plone6/issues",
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "setuptools",
        "Plone",
        "prettyconf",
        "kitconcept.api",
    ],
    extras_require={
        "test": [
            "zest.releaser[recommended]",
            "plone.app.testing[robot]>=7.0.0a3",
            "plone.restapi[test]",
            "collective.MockMailHost",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = site_plone6.locales.update:update_locale
    """,
)
