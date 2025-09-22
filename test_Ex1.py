import pytest
from ExDebug1 import environnement_optimal

# Arrange
@pytest.mark.parametrize("temp, poussiere, humidite, resultat_attendu", [
    (25, "faible", 40, True),
    (30, "faible", 40, False),
    # Ajoutez d'autres cas de test si nécessaire
])
def test_environnement_optimal(temp, poussiere, humidite, resultat_attendu):
    afficher_message : bool = False

    # Act
    resultat = environnement_optimal(temp, poussiere, humidite, afficher_message)

    # Assert
    assert resultat is None or isinstance(resultat, bool)
    assert resultat_attendu == resultat