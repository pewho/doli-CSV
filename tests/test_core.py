# coding: utf-8
from csv_doli.core import HEADER


def test_header():
    assert "Date" in HEADER
    assert "Date valeur" in HEADER
    assert "Libellé" in HEADER
    assert "Débit Euros" in HEADER
    assert "Crédit Euros" in HEADER
