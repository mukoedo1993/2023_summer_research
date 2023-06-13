#replace the path_to_tif below with the absolute directory:
path_to_tif = "/home/student/Documents/2023summer_intern/pyqgis/TIFs/critical area.tif"
rlayer = QgsRasterLayer(path_to_tif, "SRTM layer name")
if not rlayer.isValid():
    print("Layer failed to load!")
print(rlayer)

iface.addRasterLayer(path_to_tif, "layer name you like")