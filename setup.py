## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
# This parenthesis literally HAS to be on this line, f*ck you python for making me spend an hour debugging that 
setup_args = generate_distutils_setup (
    packages=['ping_driver'],
    scripts=['nodes/pingDriver.py'],
    package_dir={'': 'src'}
)

setup(**setup_args)