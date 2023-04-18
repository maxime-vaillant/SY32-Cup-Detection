# Projet Detection Ecocup - SY32

## Auteurs

- Maxime Vaillant
- Louis Jeanneau

## Pré-requis

- Avoir les librairies `Scikit-Learn`, `Numpy`, `Pandas` et `Scikit-Image`.

- Installer le dataset :

```
git clone https://gitlab.utc.fr/sy32/sy32-ecocup-p22/dataset.git
```

- Installer yolov5 :

```
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -qr requirements.txt
```

Il faudra aussi créer des dossiers vides : `images`, `labels`, `train_images`, et `runs`. Libre à l'utilisateur de choisir d'autre nom de dossier, mais il faudra changer le code en conséquence.

## Utilisation

La majorité des fichiers se présentent sous forme de Jupyter Notebook.
Les scripts commençant par `ml` sont les scripts concernant la première partie du projet.
Ceux commençant par `yolo` sont ceux concernant la deuxième partie du projet.

Ces différentes parties se commposent de la même manière :
- Génération de la base de donnée.
- Entraînement du modèle.
- Détection sur image.

Les scripts sont à exécuter dans cet ordre et possèdent chacun d'entre eux, une cellule avec les paramétrages à choisir. 

La première partie n'ayant pas aboutie, elle n'est pas à 100% fonctionnelle.

## Avertissement

/!\ Ce code a été réalisé sous MacOS. Il devrait donc fonctionner correctement sous système UNIX, mais peut être pas sous Windows. /!\

