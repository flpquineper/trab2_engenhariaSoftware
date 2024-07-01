import pytest
from unittest.mock import patch, mock_open
import jogo_da_forca

@patch('jogo_da_forca.os.path.exists')
@patch('builtins.open', new_callable=mock_open, read_data="Alice:30\nBob:20")
def test_ler_ranking(mock_open, mock_exists):
    mock_exists.return_value = True
    ranking = jogo_da_forca.ler_ranking("ranking.txt")
    assert ranking == [('Alice', 30), ('Bob', 20)]

@patch('builtins.open', new_callable=mock_open)
def test_salvar_ranking(mock_open):
    ranking = [('Alice', 30), ('Bob', 20)]
    jogo_da_forca.salvar_ranking(ranking, "ranking.txt")
    mock_open.assert_called_once_with("ranking.txt", "w")
    mock_open().writelines.assert_called_once_with(['Alice:30\n', 'Bob:20\n'])

@patch('jogo_da_forca.ler_ranking', return_value=[('Alice', 30), ('Bob', 20)])
@patch('jogo_da_forca.salvar_ranking')
def test_atualizar_ranking(mock_salvar_ranking, mock_ler_ranking):
    jogo_da_forca.atualizar_ranking('Charlie', 40, "ranking.txt")
    mock_salvar_ranking.assert_called_once_with([('Charlie', 40), ('Alice', 30), ('Bob', 20)], "ranking.txt")

@patch('builtins.print')
def test_mostrar_forca(mock_print):
    jogo_da_forca.mostrar_forca(3)
    mock_print.assert_called_once_with("  -----\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========")

def test_verificar_tentativa():
    letras_usuario = ['a', 'b', 'c']
    assert not jogo_da_forca.verificar_tentativa('a', letras_usuario)
    assert jogo_da_forca.verificar_tentativa('d', letras_usuario)

def test_calcular_pontos():
    assert jogo_da_forca.calcular_pontos(6, 2) == 40
    assert jogo_da_forca.calcular_pontos(6, 6) == 0
