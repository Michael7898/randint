import random
import pytest
from unittest.mock import patch
from Jeu_nombre import jeu_devine_le_nombre

def test_avec_bonne_reponse():
    with patch('builtins.input', return_value='5'):
        assert jeu_devine_le_nombre() == "Bravo! Tu as deviné le nombre correctement."

def test_avec_essais_epuises(capsys):
    with patch('builtins.input', side_effect=['1', '2', '3']):
        jeu_devine_le_nombre()
        captured = capsys.readouterr()
        assert "Dommage! Le nombre à deviner était" in captured.out

def test_avec_une_mauvaise_reponse_et_puis_une_bonne(capsys):
    with patch('builtins.input', side_effect=['1', '2', '5']):
        jeu_devine_le_nombre()
        captured = capsys.readouterr()
        assert "Bravo! Tu as deviné le nombre correctement." in captured.out

def test_avec_toutes_mauvaises_reponses(capsys):
    with patch('builtins.input', side_effect=['1', '2', '4']):
        jeu_devine_le_nombre()
        captured = capsys.readouterr()
        assert "Dommage! Le nombre à deviner était" in captured.out
