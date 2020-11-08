# coding: utf-8

def rectangle(prost1, prost2):
	""" Na płaszczyźnie z układem współrzędnych rozpatrujemy prostokąty, których krawędzie są równoległe do osi.
	Takie prostokąty są w pełni określone albo przez zadanie współrzędnych naprzeciwległych wierzchołków,
	albo przez zadanie jednego określonego wierzchołka oraz wymiarów: szerokości i wysokości.
		ax1 i ay1 są to wspóżedne pierwszego narożnika prostokąta
		   ax2 i ay2 druga para danych współżedne drugiego narożnika lub wyskość i szerokośc prostokąrta.
		   czy_dx_dy to zmienna logoczna:
			   0 znaczy że x2 i y2 to współrzędne
			   1 znaczy że x2 i y2 wysokość i szerokość prostokąta"""
	# https://app.diagrams.net/#G1WASNnKS-loYv3Eg2p8GDDvbuMSfy8CHT
	#             0     1    2      3       4
	# prost1=a_x1, a_y1, a_x2, a_y2, a_czy_dx_dy
	# prost2=b_x1, b_y1, b_x2, b_y2, b_czy_dx_dy
	if prost1[4] == True:
		prost1[2] = prost1[0] + prost1[2]
		prost1[3] = prost1[1] + prost1[3]
	if prost2[4] == True:
		prost2[2] = prost2[0] + prost2[2]
		prost2[3] = prost2[1] + prost2[3]
	""" Wyznaczyć część wspólną dwóch danych prostokątów. 
	Dana wynikowa ma opisywać prostokąt w taki sam sposób, jak każda z danych wejściowych."""
	if prost1[0] > prost1[2]:
		X_min = prost1[2]
		X_max = prost1[0]
		prost1[0] = X_min
		prost1[2] = X_max
	if prost1[1] > prost1[3]:
		Y_min = prost1[3]
		Y_max = prost1[1]
		prost1[1] = Y_min
		prost1[3] = Y_max
	if prost2[0] > prost2[2]:
		X_min = prost2[2]
		X_max = prost2[0]
		prost2[0] = X_min
		prost2[2] = X_max
	if prost2[1] > prost2[3]:
		Y_min = prost2[3]
		Y_max = prost2[1]
		prost2[1] = Y_min
		prost2[3] = Y_max
	wsp=[max(prost1[0],prost2[0]),max(prost1[1],prost2[1]),min(prost1[2],prost2[2]),min(prost1[3],prost2[3])]
    #todo:wyznaczanie cześci wspólnej prostokątów
	print(f'Dane są dwa prostokąty {prost1[0:2]} , {prost1[2:4]} oraz {prost2[0:2]} , {prost2[2:4]} ich część wspólną stanowi prostokąt o w spórzędnych {wsp[0:2]} , {wsp[2:4]}')

rectangle([100, 110, 200, 220, 1], [180, 175, 20, 20, 1])
rectangle([100, 110, 200, 220, 1], [200, 220, -30, -50, 1])
rectangle([100, 110, 200, 220, 0], [180, 175, 20, 20, 0])
rectangle([100, 110, 200, 220, 0], [200, 220, -30, -50, 0])
rectangle([100, 110, 230, 250, 0], [200, 220,  300, 350, 0])
