
from js import document
import pyodide
import turtle
import importlib
import sys

def run_turtle(e):
    code = document.getElementById('code')

    with open('tt.py', 'w') as f:
        f.write(code.value)

    turtle.reset()
    turtle.resetscreen()

    if not 'tt' in sys.modules.keys():
        import tt
    else:
        importlib.reload(sys.modules['tt'])

    
    pyscript.write('output', turtle.svg())

document.getElementById('run-turtle').addEventListener('click', pyodide.create_proxy(run_turtle))

