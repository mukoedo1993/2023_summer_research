import os
from qgis.core import *
#replace it with the real pyqgis root
dir_path = '/home/student/Documents/2023summer_intern/pyqgis/'
path_to_vf_layer = f"{dir_path}state_border_and _vf/points_vf.shp"
path_to_state_border_layer = f"{dir_path}state_border_and _vf/state_border.shp"

vlayer2 = QgsVectorLayer(path_to_state_border_layer, "State Border layer", "ogr")
if not vlayer2.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer2)


vlayer1 = QgsVectorLayer(path_to_vf_layer, "Points layer", "ogr")
if not vlayer1.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer1)
    
