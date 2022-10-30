from js import document
import pyodide
import importlib
import contextlib
import io
import pytest


def run_tests(e):
    print('iniciando teste!')
    code = document.getElementById('code')
    print(code.value)

    with open('solution.py', 'w') as f:
        f.write(code.value)    
        print('solucao atual', code.value)

    try:
        import solution
        importlib.reload(solution)

    except:
        return
    
    err = io.StringIO()
    with contextlib.redirect_stderr(err):
        with contextlib.redirect_stdout(err):
            pytest.main()

    if "8 passed" in err.getvalue():
        pyscript.write('pytest-output', 'Parabéns! Você acertou o exercício!')
        document.getElementById("next_button").style.color = "white"
        document.getElementById("next_button").style.background = "#5bcf4f"
        document.getElementById("next_button").style.pointerEvents = "all"
    else:
        frase = err.getvalue().find('AssertionError: Algo deu errado.')
        print(frase)
        pyscript.write('pytest-output', err.getvalue())




code = document.getElementById('code')
with open('solution.py') as f:
    code.value = f.read()
    print(code.value)


document.getElementById('run-tests').addEventListener('click', pyodide.create_proxy(run_tests))
