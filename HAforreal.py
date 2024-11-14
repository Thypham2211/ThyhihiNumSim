# Gruppe 01
# Ngoc Bao Thy, Pham, 481509
# Kossatz, Ida, 476046
# Schade, Lucie, 465926
# Marx, Loui, 465807
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.signal import convolve2d
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.transform import resize
from matplotlib.animation import FFMpegWriter

#Erstelle den FFMpegWriter
writer = FFMpegWriter(fps = 10, metadata = dict(artist = 'Me'), bitrate = 1800)


#Um Schleife zu vermeiden benutze ich diese Funktion, um die Startkonfiguration  in Abhängigkeit von k zuzuweisen.
def initialize_grid(n, k):
	#Zufällige Verteilung (k = 1)
	random_grid = np.random.choice([0, 1], size = (n, n), p =[0.5, 0.5])

#	Tub mit Störung (k = 2)
	tub = np.array([[0, 1, 0, 0],
					[1, 0, 1, 0],
					[0, 1, 0, 0],
					[0, 0, 0, 0]])
	#mid = n // 2
	#tub_grid = np.zeros((n, n))
	#tub_grid[mid - 2:mid + 2, mid - 2:mid + 2] = tub
	#tub_grid[mid, mid] = 1
	#Füge eine Störung hinzu

	# Wiederhole das Tub-Muster über die gesamte Matrix
	tub_grid = np.tile(tub, (n // tub.shape[0] + 1, n // tub.shape[1] + 1))[:n, :n]
	tub_grid[n // 2, n // 2] = 1  # Füge eine Störung im Zentrum hinzu

	#Acorn-Struktur (k = 3)
	acorn = np.array([
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 0, 0, 0, 0],
		[0, 1, 1, 0, 0, 1, 1, 1, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
	])
	#acorn_grid = np.zeros((n, n))
	#Berechne den Startpunkt (linke obere Ecke) für die Platzierung von acorn
	#acorn_mid_row = mid - acorn.shape[0] // 2
	#acorn_mid_col = mid - acorn.shape[1] // 2
	#Platzieren von acorn in acorn_grid
	#acorn_grid[acorn_mid_row:acorn_mid_row + acorn.shape[0],
	#acorn_mid_col:acorn_mid_col + acorn.shape[1]] = acorn

	# Wiederhole das Acorn-Muster über die gesamte Matrix
	acorn_grid = np.tile(acorn, (n // acorn.shape[0] + 1, n // acorn.shape[1] + 1))[:n, :n]

	#Bild einlesen (k = 4)
	img = imread('ihr_Foto.jpg')
	img_gray = rgb2gray(img)
	#rgb2gray konvertiert das Bild in Graustufen (Helligkeit zwischen 0 und 1).
	img_bin = img_gray > 0.5
	#erstellt ein binäres Bild, wobei Pixel mit Helligkeit über 0,5 als "1" (schwarz) und darunter als "0"
	#(weiß) gesetzt werden.
	image_grid = resize(img_bin, (n, n)).astype(int)
	#resize, damit das Bild auch n x n groß ist.

	#Liste der Startkonfigurationen
	configurations =[random_grid, tub_grid, acorn_grid, image_grid]

	#Rückgabe der Startkonfiguration basierend auf k (0-basiert: k-1)
	return configurations[k - 1]


def NumSimHA2 (n, J, k):
	#z = Startkonfiguration
	z = initialize_grid(n, k)
	#𝐽 Zeitschritten, k = vier Anfangsverteilungen und n = Gridgröße -> werden beim Ausführen definiert

		#--------------------------------------------------
	#Filter 'kernel', der bestimmt, wie die Nachbarschaft berechnet wird. Hier werden nur die ECHTE NACHBARN summiert.
	kernel = np.array([[1, 1, 1],
		   				[1, 0, 1],
		   				[1, 1, 1]])

	fig,ax = plt.subplots()
	img = ax.imshow(z, cmap = 'binary')
	#Liste zur Speicherung der Bilder für die Animation
	frames =[]

	#Wie funktioniert die Faltungconvolve2d?
	#1.Der Filter wird auf das Gitter gelegt, sodass er mit einem 3x3-Bereich überlappt.
	#2.Die Werte des Gitters und des Filters werden elementweise multipliziert.
	#3.Die Ergebnisse werden addiert und ergeben einen neuen Wert im Ergebnisgitter 'Summe'.
	#--------------------------------------------------

	for t in range(J):
		#Summe der Nachbarn (periodische Randbedingungen: wrap)
		Summe = convolve2d(z, kernel, mode = 'same', boundary = 'wrap')

		#Update-Regel:
		#Bedingung erfüllt: True = 1, sonst: False = 0
		z = (Summe == 3) | ((z == 1) & (Summe == 4))
		z = z.astype(int)
		#Konvertiere das Ergebnis zurück zu 0 und 1

		#Update des Plots 'img.set_array(z)' und Hinzufügen zum Frames-Array
		img.set_array(z)
		frames.append([plt.imshow(z, cmap = 'binary', animated = True)])

		#Erstellung der Animation
		#ArtistAnimation: Erstellt eine Animation aus der Liste frames.
		#interval=100: Setzt die Zeit zwischen den Frames auf 100 Millisekunden.
		#blit=True: Macht die Animation schneller, indem nur der Teil des Bildes aktualisiert wird, der sich ändert.
		ani = animation.ArtistAnimation(fig, frames, interval = 100, blit = True)

		#Speichern als MP4
		#fps steht für "Frames per Second" (Bilder pro Sekunde).
		ani.save('AnimationHA2.mp4', writer = writer)
		#writer="ffmpeg", fps=10)

		#Anzeige der Animation im Jupyter Notebook
	#plt.colorbar()
	plt.show()


#Beispiel für die Verwendung
#NumSimHA2(None, n, J, k)
#NumSimHA2(20,10,3)


#Startkonfiguration printen:
grid = initialize_grid(10, 2)
print(grid)
plt.imshow(grid, cmap='binary')  # cmap='binary' für Schwarz-Weiß
plt.show()
