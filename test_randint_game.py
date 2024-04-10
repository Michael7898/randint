import pytest
from unittest.mock import patch
from randint_game import jeu_devine_le_nombre

# Test pour une bonne réponse simulée
def test_avec_bonne_reponse(capsys):
    # Simule l'entrée utilisateur avec la bonne réponse présumée du nombre aléatoire
    with patch('builtins.input', return_value='5'):
        with patch('random.randint', return_value=5):  # S'assure que le nombre aléatoire est 5
            jeu_devine_le_nombre()
            captured = capsys.readouterr()
            assert "Bravo! Tu as deviné le nombre correctement." in captured.out

# Test pour vérifier le message lorsqu'on épuise tous les essais
def test_avec_essais_epuises(capsys):
    with patch('builtins.input', side_effect=['1', '2', '3']):
        with patch('random.randint', return_value=5):  # Fixe le nombre aléatoire à 5 pour le test
            jeu_devine_le_nombre()
            captured = capsys.readouterr()
            assert "Dommage! Le nombres à deviner était 5" in captured.out

# Test pour simuler une mauvaise réponse suivie d'une bonne réponse
def test_avec_une_mauvaise_reponse_et_puis_une_bonne(capsys):
    with patch('builtins.input', side_effect=['1', '5']):
        with patch('random.randint', return_value=5):  # Assure que le nombre aléatoire est 5
            jeu_devine_le_nombre()
            captured = capsys.readouterr()
            assert "Bravo! Tu as deviné le nombre correctement." in captured.out

# Test pour simuler des réponses toutes mauvaises
def test_avec_toutes_mauvaises_reponses(capsys):
    with patch('builtins.input', side_effect=['1', '2', '4']):
        with patch('random.randint', return_value=5):  # Le nombre aléatoire est 5
            jeu_devine_le_nombre()
            captured = capsys.readouterr()
            assert "Dommage! Le nombres à deviner était 5" in captured.out
