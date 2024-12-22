# Gruppe 01
# Ngoc Bao Thy, Pham, 481509
# Kossatz, Ida, 476046
# Schade, Lucie, 465926
# Marx, Loui, 465807

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import time



def gitter_ersteller(n,m):
    """Verantwortliche/r: Lucie Schade

    Erstellt ein Gitter mit n Spalten und m Zeilen. Sorgt dafür, dass m ungerade ist, indem es für gerade m eine
    Zeile hinzufügt. Prüft das n>=m ist.

    Args:
        n (int): anzahl an Spalten im Scheibengitter
        m (int): anzahl an Zeilen im Scheibengitter

    Returns:
        (2D NumPy Array): Das Fertige Gitter
    """
    # erstelle das Gitter
    # Test
    if n < m: #Stellt sicher, das m grösser als n ist und bricht andern Falls das Programm ab
        raise ValueError("Fehler: n ist kleiner als m. Das Programm wird beendet.")

    if m % 2 ==0: # Checkt, ob m gerade ist
        m = m+1 # ist m gerade, addiere 1 => m = ungerae

    gitter = np.zeros(m, n) # m x n Nullen Gitter

    return gitter



def NumSim(n,m,F,c,grid):
    """Verantwortliche/r:

    Simmuliert die Verschiebungen einer mit einer Streckenlast belastete linearelastischen, isotropen, Scheibe.

    Args:
        n (int): anzahl an Spalten im Scheibengitter
        m (int): anzahl an Zeilen im Scheibengitter
        F (float): Betrag der Kräfte, die auf die Oberkannte des Gitters wirken (bilden Streckenlast ab)
        c (float): Federsteifigkeit der Hoirzontal- und Vertikalfedern, Federsteifigkeit der Diagonalen ist c/2
        grid (2D NumPy Array): Gitter, auf dem die Simulation durchgeführt wird.

    Returns:
        (1D-np.array, 3D-np.array): (ein Touple aus Zwei NumPy Arrays)
            (1D-np.array): Resultierende Biegelinie der Numerischen Simulation in Form von einem 1D NumPy Array welches
                die Verschiebung der Scheibe in y-Richtung angibt. Jedes Element gehört dabei zu einer x-Position auf
                der Scheibe.
            (3D-np.array): 3D NumPy Array, welches die Verschiebungen der Scheibe in x- und y-Richtung angibt. Jedes
                Element reperäsentiert dabei einen Gitterpunkt und enthält die Verschiebungen in x- und y-Richtung. Das
                array hat also die Form (n x m x 2)
        """
    # Bestimme die Verschiebungen der Scheibe
    # Siehe übung 4
    NumSimBiegeline = None
    NumSimVerschiebungsArray = None

    return NumSimBiegeline, NumSimVerschiebungsArray



def Figure1Plotter(n, m, NumSimVerschiebungsArray, delta_x, delta_y):
    """Verantwortliche/r:

    In Figure 1 sollen nach dem Ausführen der NumSim Funktion die Positionen der Gitterpunkte gezeigt werden.
    Verwenden Sie dazu einfach kleine schwarze Punkte. Die Ausgangslage der Gitterpunkte soll nicht
    geplottet werden. Die feste Einspannung kann z.B. über etwas dickere schwarze Punkte dargestellt
    werden.

    Args:
        NumVerschiebungsArray (1D-np.array): _description_
        delta_x (float): _description_
        delta_y (float): _description_
    Returns:
        Figure 1: Plot der Verschobenen Gitterpunkte. Punkte auf x-y-Ebene, wobei der Abstand der Punkte der dritten
        Dimension des NumSimVerschiebungsArray entnommen werden kann. Skalierung mit delta_xy nicht vergessen. Fest
        eingespannte Punkte dick Plotten.
    """
    # Erzeuge den Plot
    # Anfangskoordinaten der Gitterpunkte (np.arange(m): Erstellt eine Folge von Zahlen von 0 bis m-1)
    x_coords, y_coords = np.meshgrid(np.arange(m) * delta_x, np.arange(n) * delta_y)

    # Verschobene Positionen der Gitterpunkte
    x_disp = x_coords + NumSimVerschiebungsArray[:, :, 0] #Verschiebung in x-Richtung
    y_disp = y_coords + NumSimVerschiebungsArray[:, :, 1] #Verschiebung in y-Richtung

    # Erstellen des Plots
    plt.figure(figsize=(8, 6))

    # Gitterpunkte als kleine schwarze Punkte plotten (schwarz = k)
    plt.plot(x_disp.flatten(), y_disp.flatten(), 'k.', label='Verschobene Gitterpunkte')

    # Feste Einspannungen (z.B. erste Zeile) dicker darstellen
    plt.plot(x_disp[0, :], y_disp[0, :], 'ko', markersize=6, label='Feste Einspannung')

    # Achsenbeschriftungen und Titel
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Figure 1: Nummerisch ermittelte verschobene Gitterpunkte')

    # Y-Achse invertieren, um Biegung nach unten darzustellen
    plt.gca().invert_yaxis()

    # Legende hinzufügen
    plt.legend()

    # Plot anzeigen
    plt.grid(True)
    plt.axis('equal') #Skalen der x- und y-Achsen sind gleich (in m)
    plt.show()
    return None



def Scheibentheroie(n,m,F,c,delta_x,delta_y):
    """Verantwortliche/r:

    Wertet die Scheibentheorie aus und gibt die Verschiebungen der Scheibe zurück.
    Args:
        n (int): anzahl an Spalten im Scheibengitter
        m (int): anzahl an Zeilen im Scheibengitter
        F (float): Betrag der Kräfte, die auf die Oberkannte des Gitters wirken (bilden Streckenlast ab)
        delta_x (float): Abstand zwischen den Gitterpunkten in x-Richtung
        delta_y (float): Abstand zwischen den Gitterpunkten in y-Richtung
    Returns:
        (1D-np.array): Resultierende Biegelinie der Scheibentherorie in Form von einem 1D NumPy Array welches die
        Verschiebung der Scheibe in y-Richtung angibt. Jedes Element gehört dabei zu einer x-Position auf der Scheibe.
    """
    # Bestimme die Scheibenbiegeline

    # Parameter der Scheibe
    l = n*delta_x    # Länge der Scheibe [m]
    h = m/2*delta_y  # Höhe der Scheibe

    # Materialparameter
    nu = 1 / 3             # Poissonzahl
    Et = 4/3 * c           # Ergibt sich aus der Multiplikation mit E (-Modul) und t, t kürzt sich raus
    q0 = F / delta_x       # Streckenlast

    # x-Koordinaten (n Gitterpunkte entlang x)
    x = np.arange(0, n, step=delta_x) ### evt. muss dass im plott auch gecalled werden

    # y - Koordinaten mit passender Anzahl für Plott
    y = np.linspace(0,h,num=int(n/delta_x))

    # Analytische Lösung (Scheibentheorie)
    u_analytic = -(q0 * nu) / (2 * Et) * x  # Längsverschiebung
    v_analytic = -(q0 * h) / (Et) * (
        - (1 / (16 * h**4)) * (6 * l**2 * x**2 - 4 * l * x**3 + x**4)
        + (3 / 5) * (x**2 / h**2)
        + (3 / 8) * (nu**2 * x**2 / h**2)
    ) # Querverschiebung

    ScheibenBiegeline_x = x+u_analytic
    ScheibenBiegeline_y = y + v_analytic

    return ScheibenBiegeline_x, ScheibenBiegeline_y



def Balkentheorie(n,m,F,c, delta_x, delta_y):
    """Verantwortliche/r:

    Wertet die Balkentheorie aus und gibt die Verschiebungen der Scheibe zurück.
    Args:
        n (int): anzahl an Spalten im Scheibengitter
        m (int): anzahl an Zeilen im Scheibengitter
        F (float): Betrag der Kräfte, die auf die Oberkannte des Gitters wirken (bilden Streckenlast ab)
        delta_x (float): Abstand zwischen den Gitterpunkten in x-Richtung
        delta_y (float): Abstand zwischen den Gitterpunkten in y-Richtung
    Returns:
        (1D-np.array): Resultierende Biegelinie der Balkentherorie in Form von einem 1D NumPy Array welches die
        Verschiebung der Scheibe in y-Richtung angibt. Jedes Element gehört dabei zu einer x-Position auf der Scheibe.
    """
    # Bestimme die Balkenbiegeline

    # Parameter der Scheibe
    l = n*delta_x         # Länge der Scheibe [m]
    h = m/2*delta_y          # Höhe der Scheibe

    # x-Koordinaten (n Gitterpunkte entlang x)
    x = np.arange(0, n, step=delta_x)

    # y-Koordinaten
    y=np.linspace(0,h,num=int(n/delta_x))

    # Materialparameter
    EI = 8/9 *h**3 * c      # E-Modul multipiziert mit Trägheitsmoment I
    q0 = F / delta_x       # Streckenlast
     #Analytische Lösung (Balkentheorie) für Querverschiebung
    v_beam = (q0 / (EI)) * x**2 * (x**2 / 24 - l * x / 6 + l**2 / 4)
    BalkenBiegeline = x, v_beam

    return BalkenBiegeline



def Figure2Plotter(n, m, F, c, delta_x, delta_y):
    """Verantwortliche/r:
    Args:
        n (int): anzahl an Spalten im Scheibengitter
        NumSimBiegeline (1D-np.array): Resultierende Biegelinie der Numerischen Simulation in Form von einem 1D NumPy Array
                                welches  die Verschiebung der Scheibe in y-Richtung angibt. Jedes Element gehört dabei
                                zu einer x-Position auf der Scheibe.
        ScheibenBiegeline (1D-np.array): Resultierende Biegelinie der Scheibentherorie in Form von einem 1D NumPy Array
                                    welches die Verschiebung der Scheibe in y-Richtung angibt. Jedes Element gehört
                                    dabei zu einer x-Position auf der Scheibe.
        BalkenBiegeline (1D-np.array): Resultierende Biegelinie der Balkentherorie in Form von einem 1D NumPy welches
                                die Verschiebung der Scheibe in y-Richtung angibt. Jedes Element gehört dabei zu
                                einer x-Position auf der Scheibe.
        delta_x (float): Abstand zwischen den Gitterpunkten in x-Richtung
        delta_y (float): Abstand zwischen den Gitterpunkten in y-Richtung

    Returns:
        Figure 2: 3 Graphen in einem Plot. Der erste Graph zeigt die Biegelinie der Numerischen Simulation, der zweite der
                Scheibentheorie und der dritte der Balkentheorie. Die Graphen sind Farblich unterschieden und haben eine
                Legende.
    """
    # Erzeuge den Plot
    # Anfangskoordinaten der Gitterpunkte (ähnlich wie beim 1. Plot)
    x_coords = np.arange(n) * delta_x
    #Hier braucht man keine y-Koordinate definieren, da es um 1D Biegelinien geht.
    #Die Verschiebungen in y-Richtung wird mit den Arrays dargestellt.
    plt.figure(figsize=(8, 6))

    # Plot der ursprünglichen Position der Gitterpunkte (Mittellinie des Balkens bei y = 0)
    plt.plot(x_coords, np.zeros_like(x_coords), label='Ursprüngliche Position (Mittellinie)', color='k', linestyle='--')

    # Plot der Biegelinien
    plt.plot(x_coords, NumSimBiegeline, label='Numerische Simulation', color='b')
    plt.plot(x_coords, ScheibenBiegeline, label='Scheibentheorie', color='g')
    plt.plot(x_coords, BalkenBiegeline, label='Balkentheorie', color='r')

    # Achsenbeschriftungen und Titel
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Figure 2: Biegelinien (einschließlich der ursprünglichen Position)')

    # Legende und Gitter
    plt.legend()
    plt.grid(True)

    # Plot anzeigen
    plt.show()




    #
    ScheibenBiegeline_x, Scheibenbiegeline_y = Scheibentheroie(n, m, F, c, delta_x, delta_y)
    BalkenBiegeline_x, BalkenBiegeline_y = Balkentheorie(n, m, F, c, delta_x, delta_y)
    # Plot der Ergebnisse (Figure 2) - Querverschiebung
    plt.figure(figsize=(10, 6))
    plt.plot(ScheibenBiegeline_x,Scheibenbiegeline_y , label="Analytische Querverschiebung (Scheibentheorie)", linestyle="-.", color="red")
    plt.plot(BalkenBiegeline_x, BalkenBiegeline_y, label="Querverschiebung (Balkentheorie)", linestyle="--", color="green")
    plt.title("Biegelinen")
    plt.xlabel("$x$")
    plt.ylabel("$v(x)$")
    plt.legend(loc="best")
    # Y-Achse invertieren, um Biegung nach unten darzustellen
    plt.gca().invert_yaxis()
    plt.grid()
    plt.tight_layout()
    plt.show()
    return None



def NumSimHA4(n,m,F,c):
    """Verantwortliche/r: Loui Marx

    Simmuliert die Verschiebungen einer mit einer Streckenlast belastete linearelastischen, isotropen, Scheibe.
    i ist index in x-Richtung

    Args:
        n (int): anzahl an Spalten im Scheibengitter
        m (int): anzahl an Zeilen im Scheibengitter
        F (float): Betrag der Kräfte, die auf die Oberkannte des Gitters wirken (bilden Streckenlast ab)
        c (float): Federsteifigkeit der Hoirzontal- und Vertikalfedern, Federsteifigkeit der Diagonalen ist c/2

    Returns:
        Figure 1: Darstellung der Verschiebungen der Scheibe
        Figure 2: Vergleich der Numerischen Ergebnisse für Längs- und Querverschiebungen mit analytischen Ergebnissen.
                    y über x Plot der Profielsehnen im selben Diagramm.
    """
    # Alle Funktionen sind weiter oben dokumentiert
    delta_x = 0.1
    delta_y = 0.1
    # Erstellt das Simulationsgitter als 2D NumPy Array
    gitter = gitter_ersteller(n,m)
    # Touple Output von NumSim() wird in 2 seperaten Variablen gespeichert. Die Biegeline als 1D NumPy Array und die
    # Verschiebungen als 3D NumPy Array, für mehr details siehe NumSim() dokumentation.
    NumSimBiegeline, NumSimVerschiebungsArray = NumSim(n,m,F,c,gitter)
    # Plottet Figure 1
    Figure1Plotter(NumSimVerschiebungsArray, delta_x, delta_y)
    # Bestimme die Analytischen Biegelinien und gibt die Verschiebungen als 1D NumPy Arrays zurück.
    ScheibenBiegeline = Scheibentheroie(n,m,F,c,delta_x,delta_y)
    BalkenBiegeline = Balkentheorie(n,m,F,c, delta_x, delta_y)
    # Plottet Figure 2
    Figure2Plotter(n, NumSimBiegeline, ScheibenBiegeline, BalkenBiegeline, delta_x, delta_y)

    return None

# Beispielaufruf der Funktion mit Parametern
n = 500  # Anzahl der Gitterpunkte
m = 205  # Anzahl der Zeilen
F = 1.0  # Kraft auf jeden Punkt [N]
c = 1000  # Materialkonstante
delta_x = 0.1  # Abstand zwischen den Gitterpunkten in x-Richtung
delta_y = 0.1  # Abstand zwischen den Gitterpunkten in y-Richtung

Figure2Plotter(n, m, F, c, delta_x, delta_y)