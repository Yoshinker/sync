# sync.py
Un script python pour synchroniser tous les fichiers vidéos .mkv avec leurs sous-titres .srt d'un dossier.
Un dossier "SYNC" est créé et contient les fichiers vidéos après rendu.

# REQUIS
Ce script nécessite python3 ainsi que le paquet mkvmerge.
Fonctionne sur les distributions Debian

# UTILISATION
Le script doit se trouver dans le dossier contenant les fichiers à synchroniser.
Dans un terminal de commande, entrer:

    $ python3 sync.py

# NOTES
Le script ne fonctionne pour l'instant que si le dossier contient UNIQUEMENT les fichiers vidéos et de sous-titres.
Seul les .mkv et .srt sont pris en charge.
