# -*- coding: UTF-8 -*-
from distutils.command.install import INSTALL_SCHEMES
from distutils.core import setup
from setuptools import find_packages
import os
import re
import time


_version = "0.1.dev%s" % int(time.time())
_packages = find_packages('elpassolito', exclude=["*.tests", "*.tests.*", "tests.*", "tests"])



# make sure that data files go into the right place
# see http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values(): 
    scheme['data'] = scheme['purelib']
    
    

# find any static content such as HTML files or CSS
_INCLUDE = re.compile("^.*\.(json|html|less|js|png|gif|jpg|mo)$") 
_root_directory='elpassolito'

def get_package_data():
    package_data = {}
    for pkg in os.listdir(_root_directory):
        pkg_path = os.path.join(_root_directory, pkg)
        if os.path.isdir(pkg_path):
            package_data[pkg] = create_paths(pkg_path)
    return package_data

def create_paths(root_dir):
    paths = []
    is_package = os.path.exists(os.path.join(root_dir, '__init__.py'))
    children = os.listdir(root_dir)
    for child in children:
        childpath = os.path.join(root_dir, child)
        if os.path.isfile(childpath) and not is_package and _INCLUDE.match(child):
            paths.append(child)
        if os.path.isdir(childpath):
            paths += [os.path.join( child, path ) for path in create_paths( os.path.join(root_dir, child) ) ]
    return paths


# common dependencies
_install_requires = [
            'django>=1.4',
            'south>=0.7.6',
            'django-compressor>=1.2',
            'django-crispy-forms>=1.2.0',
            'django-gubbins>=1.1',
            'boto>=2.6.0',
            'django-storages>=1.1.5',
            'gunicorn',
            'dj_database_url',
            'psycopg2!=2.4.2',
            'django-social-auth',
            ]


setup( name='elpassolito',
       version=_version,
       
       packages=_packages,
       package_dir={'': 'elpassolito'},
       package_data=get_package_data(),

       install_requires=_install_requires,
 )
