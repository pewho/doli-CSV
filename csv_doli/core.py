#!/usr/bin/env python
# coding: utf-8

import os
import argparse
import tempfile
import csv

__all__ = ["main"]

HEADER = ("Date", "Date valeur", "Libellé", "Débit Euros", "Crédit Euros")

# Dialect CSV (banque)
class InpDial(csv.Dialect):
    delimiter = ";"
    strict = True
    quoting = csv.QUOTE_MINIMAL
    quotechar = '"'
    lineterminator = "\r\n"


# Dialect CSV (Dolibear)
class OutDial(csv.Dialect):
    delimiter = ";"
    strict = True
    quoting = csv.QUOTE_NONE
    quotechar = '"'
    lineterminator = "\r\n"


# Prepare le csv, retire les 10 premieres lignes, corrige les saut de lignes
def prepare_csv(path):
    with open(path, "rb") as inf:
        for x in range(0,10):
            inf.readline()
        return inf.read().decode("cp1252").replace(";\r\n", ";&&&&").replace("\r\n", "").replace(";&&&&",";\r\n")


# parse command arguments
def parse_args():
    parser = argparse.ArgumentParser(description='Process CSV to importable CSV to dolibear')
    parser.add_argument('path', type=str)
    return parser.parse_args()


# parse csv avec le dialect banque, returne une liste de dictionnaire
def parse_csv(data):
    f_temp = tempfile.TemporaryFile(mode="w+")
    f_temp.write(data)
    f_temp.seek(0)

    c = csv.DictReader(f_temp, fieldnames=HEADER, dialect=InpDial)
    data_list = []
    for row in c:
        data_list.append(row)
    f_temp.close()
    return data_list


# réécrit le CSV avec le dialect dolibear
def write_csv(data):
    with open("prepared_csv.csv", "w") as outf:
        c = csv.DictWriter(outf, fieldnames=HEADER, dialect=OutDial)
        for row in data:
            row.pop(None, None)  # fix, remove invalid column
            c.writerow(row)


# Main fn
def main():
    arg_path = parse_args()

    raw_data = prepare_csv(arg_path.path)

    data_list = parse_csv(raw_data)

    write_csv(data_list)


if __name__ == '__main__':
    main()
