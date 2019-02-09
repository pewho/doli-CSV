CSV-Doli
========

Un petit script pour reconstruire un csv valide pour l'import de données de compta
dans le module dolibear, depuis la source d'un fichier provenant d'un SI bancaire (?)


Installation
------------

Il est necessaire d'avoir une installation de python version 3 (le script a été developpé avec la version 3.6.1)
Il n'y a pas d'autres dependances.

- Se placer dans le dossier `csv-dolibear`. Si le script est téléchargé depuis github en zip, le deziper avant.
```
>>> cd csv-dolibear
```

- Lancer le script d'installation
```
>>> python setup.py
```


Utilisation
-----------

- Lancer la commande `csv-doli`, avec en parametre le chemin vers le CSV source
```
>>> csv-doli <path>
```

Le fichier est créé dans le dossier courant, avec pour nom `prepared_csv.csv`


Licence
-------

MIT

Authors
-------

les membres de l'ARALA :)
