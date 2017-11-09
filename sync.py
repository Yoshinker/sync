import os
import time

def last_4chars(x):
    return(x[-4:])


def troncature(x):
	cut = str(x).split(".")
	t = float(cut[0] + "." + cut[1][:2])
	return t 

files = os.listdir()
files.remove("sync.py")
files.sort(key=str.swapcase, reverse=False)
files.sort(key=last_4chars, reverse=False)
nb_videos = int(len(files)/2)

videos = []
subtitles = []
episodes = []

for i in range(nb_videos):
	monEp = files[i][:-4]
	l = monEp.split(" ")
	monNom = str()
	for j in range(len(l)-1):
		monNom += l[j] + "\ "
	monNom += l[len(l)-1]
	episodes.append(monNom)
	videos.append(monNom + ".mkv")
	subtitles.append(monNom + ".srt")

t_total = 0
os.system("mkdir SYNC")

for i in range(nb_videos):
	nom = "SYNC/" + episodes[i] + "\ +SYNC.mkv"
	print("Rendu de {}...".format(episodes[i]))
	debut = time.time()
	os.system("sudo mkvmerge -o -q {0} --default-track 0 --language 0:fre {1} {2}".format(nom, subtitles[i], videos[i]))
	fin = time.time()
	t = troncature(fin - debut)
	print("Terminé en {0}s !".format(t))

print()
print("Tous les rendus sont terminés")
print("Temps total : {0}s".format(t_total))

