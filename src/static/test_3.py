import pytest
from math import pi
import solution



@pytest.mark.parametrize("raio, area", [
    pytest.param(raio, area, id=f'Raio: {raio}')
    for raio, area in [
        (1, True),
        (2, False),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False)
    ]])
def test_vários_raios(numero, primo):
    dica = ''
    saida = solution.calcula_primo(numero)
    if type(saida) != type(primo):
        dica += f'O tipo da resposta esperado é {type(primo)}, mas sua função devolve {type(saida)}.'
    assert primo == saida, f'Algo deu errado. \nAo calcular a área para o raio {numero}, esperava {primo} mas obteve {saida}.\n{dica}'
