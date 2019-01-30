from distutils.core import setup
import py2exe

base = None    

executables = [Executable("BubblePlot.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<any name>",
    options = options,
    version = "1.0",
    description = '<any description>',
    executables = executables
)