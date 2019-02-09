#!/usr/bin/env python
# coding: utf-8

import csv
import tempfile
import os
import argparse


HEADER = ("Date", "Date valeur", "Libellé", "Débit Euros", "Crédit Euros")
data_list = []


class InpDial(csv.Dialect):
    delimiter = ";"
    strict = True
    quoting = csv.QUOTE_MINIMAL
    quotechar = '"'
    lineterminator = "\r\n"


class OutDial(csv.Dialect):
    delimiter = ";"
    strict = True
    quoting = csv.QUOTE_NONE
    quotechar = '"'
    lineterminator = "\r\n"


def prepare_csv(path):
    with open(path, "rb") as inf:
        for x in range(0,10):
            inf.readline()
        return inf.read().decode("cp1252").replace(";\r\n", ";&&&&").replace("\r\n", "").replace(";&&&&",";\r\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process CSV to importable CSV to dolibear')
    parser.add_argument('path', type=str)
    arg_path = parser.parse_args()

    data = prepare_csv(arg_path.path)
    f_temp = tempfile.TemporaryFile(mode="w+")
    f_temp.write(data)
    f_temp.seek(0)
    c = csv.DictReader(f_temp, fieldnames=HEADER, dialect=InpDial)
    for row in c:
        data_list.append(row)
    f_temp.close()
    
    with open("prepared_csv.csv", "w") as outf:
        c = csv.DictWriter(outf, fieldnames=HEADER, dialect=OutDial)
        for row in data_list:
            row.pop(None, None) 
            c.writerow(row)
