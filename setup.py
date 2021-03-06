import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-visitor-activity',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',  # example license
    description='A Django app to track down and save source and data for requested urls',
    long_description=README,
    url='https://github.com/prusya/django-visitor-activity',
    author='Ruslan Pozin',
    author_email='Ruslan Pozin@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        # 'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)