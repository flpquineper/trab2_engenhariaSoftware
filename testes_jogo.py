import unittest
from unittest.mock import patch, mock_open
import jogo_da_forca

class TestJogoDaForca(unittest.TestCase):

    @patch('jogo_da_forca.os.path.exists')
    @patch('builtins.open', new_callable=mock_open, read_data="Alice:30\nBob:20")
    def test_ler_ranking(self, mock_open, mock_exists):
        mock_exists.return_value = True
        ranking = jogo_da_forca.ler_ranking("ranking.txt")
        self.assertEqual(ranking, [('Alice', 30), ('Bob', 20)])

    @patch('builtins.open', new_callable=mock_open)
    def test_salvar_ranking(self, mock_open):
        ranking = [('Alice', 30), ('Bob', 20)]
        jogo_da_forca.salvar_ranking(ranking, "ranking.txt")
        mock_open.assert_called_once_with("ranking.txt", "w")
        mock_open().writelines.assert_called_once_with(['Alice:30\n', 'Bob:20\n'])



    @patch('jogo_da_forca.ler_ranking', return_value=[('Alice', 30), ('Bob', 20)])
    @patch('jogo_da_forca.salvar_ranking')
    def test_atualizar_ranking(self, mock_salvar_ranking, mock_ler_ranking):
        jogo_da_forca.atualizar_ranking('Charlie', 40, "ranking.txt")
        mock_salvar_ranking.assert_called_once_with([('Charlie', 40), ('Alice', 30), ('Bob', 20)], "ranking.txt")

    def test_mostrar_forca(self):
        with patch('builtins.print') as mock_print:
            jogo_da_forca.mostrar_forca(3)
            mock_print.assert_called_once_with("  -----\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========")

    def test_verificar_tentativa(self):
        letras_usuario = ['a', 'b', 'c']
        self.assertFalse(jogo_da_forca.verificar_tentativa('a', letras_usuario))
        self.assertTrue(jogo_da_forca.verificar_tentativa('d', letras_usuario))

    def test_calcular_pontos(self):
        self.assertEqual(jogo_da_forca.calcular_pontos(6, 2), 40)
        self.assertEqual(jogo_da_forca.calcular_pontos(6, 6), 0)

if __name__ == '__main__':
    unittest.main()
