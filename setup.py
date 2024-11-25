from setuptools import setup
import flask_hcaptcha

PACKAGE = flask_hcaptcha
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=PACKAGE.__NAME__,
    version=PACKAGE.__version__,
    license=PACKAGE.__license__,
    author=PACKAGE.__author__,
    author_email='hello@knugi.com',
    description="A hCaptcha extension for Flask based on flask-recaptcha",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/KnugiHK/flask-hcaptcha/',
    py_modules=['flask_hcaptcha'],
    include_package_data=True,
    install_requires=[
        "requests"
    ],
    extras_require = {
        "quart": ["aiohttp"]
    },
    keywords=['flask', 'hcaptcha', "validate", "captcha"],
    platforms='any',
    python_requires='>=3.9',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=False
)
