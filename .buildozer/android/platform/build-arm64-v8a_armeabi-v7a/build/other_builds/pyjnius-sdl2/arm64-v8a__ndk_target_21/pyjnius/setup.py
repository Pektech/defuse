'''
Setup.py for creating a binary distribution.
'''

from __future__ import print_function
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
try:
    import subprocess32 as subprocess
except ImportError:
    import subprocess

from os import environ
from os.path import dirname, join
import sys
from setup_sdist import SETUP_KWARGS

# XXX hack to be able to import jnius.env withough having build
# jnius.jnius yet, better solution welcome
syspath = sys.path[:]
sys.path.insert(0, 'jnius')
from env import get_java_setup
sys.path = syspath

def getenv(key):
    '''Get value from environment and decode it.'''
    val = environ.get(key)
    if val is not None:
        try:
            return val.decode()
        except AttributeError:
            return val
    return val


PYX_FILES = [
    'jnius.pyx',
]
PXI_FILES = [
    'jnius_compat.pxi',
    'jnius_conversion.pxi',
    'jnius_export_class.pxi',
    'jnius_export_func.pxi',
    'jnius_jvm_android.pxi',
    'jnius_jvm_desktop.pxi',
    'jnius_jvm_dlopen.pxi',
    'jnius_localref.pxi',
    'jnius_nativetypes3.pxi',
    'jnius_proxy.pxi',
    'jnius.pyx',
    'jnius_utils.pxi'
]

EXTRA_LINK_ARGS = []

# detect Python for android
PLATFORM = sys.platform
NDKPLATFORM = getenv('NDKPLATFORM')
if NDKPLATFORM is not None and getenv('LIBLINK'):
    PLATFORM = 'android'

JAVA=get_java_setup(PLATFORM)

assert JAVA.is_jdk(), "You need a JDK, we only found a JRE. Try setting JAVA_HOME"

def compile_native_invocation_handler(java):
    '''Find javac and compile NativeInvocationHandler.java.'''
    javac = java.get_javac()
    source_level = '8'
    try:
        subprocess.check_call([
            javac, '-target', source_level, '-source', source_level,
            join('jnius', 'src', 'org', 'jnius', 'NativeInvocationHandler.java')
        ])
    except FileNotFoundError:
        subprocess.check_call([
            javac.replace('"', ''), '-target', source_level, '-source', source_level,
            join('jnius', 'src', 'org', 'jnius', 'NativeInvocationHandler.java')
        ])

compile_native_invocation_handler(JAVA)


# generate the config.pxi
with open(join(dirname(__file__), 'jnius', 'config.pxi'), 'w') as fd:
    if PLATFORM == 'android':
        cython3 = environ.get('ANDROID_PYJNIUS_CYTHON_3', '0') == '1'
    else:
        import Cython
        cython3 = Cython.__version__.startswith('3.')
    fd.write('DEF JNIUS_PLATFORM = {0!r}\n\n'.format(PLATFORM))
    # record the Cython version, to address #669
    fd.write(f'DEF JNIUS_CYTHON_3 = {cython3}')

# pop setup.py from included files in the installed package
SETUP_KWARGS['py_modules'].remove('setup')

ext_modules = [
    Extension(
        'jnius', 
        [join('jnius', x) for x in PYX_FILES],
        depends=[join('jnius', x) for x in PXI_FILES],
        libraries=JAVA.get_libraries(),
        library_dirs=JAVA.get_library_dirs(),
        include_dirs=JAVA.get_include_dirs(),
        extra_link_args=EXTRA_LINK_ARGS,
    )
]

for ext_mod in ext_modules:
    ext_mod.cython_directives = {'language_level': 3}


# create the extension
setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules,
    **SETUP_KWARGS
)
