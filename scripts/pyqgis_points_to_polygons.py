import processing
from qgis.core import QgsProject, QgsVectorLayer

layer = iface.activeLayer()
if not layer or not layer.isValid():
    raise ValueError("Select a valid point layer.")

if "Name" not in layer.fields().names():
    raise ValueError("Selected layer must have 'Name' column.")

path_inputs = {
    "INPUT": layer,
    "CLOSE_PATH": True,
    "ORDER_EXPRESSION": "to_int(substr(Name, strpos(Name, '-') + 1))",
    "GROUP_EXPRESSION": "substr(Name, 0, strpos(Name, '-') - 1)",
    "OUTPUT": "TEMPORARY_OUTPUT",
}
paths = processing.run("native:pointstopath", path_inputs)["OUTPUT"]

poly_inputs = {"INPUT": paths, "OUTPUT": "TEMPORARY_OUTPUT"}
polygons = processing.run("qgis:linestopolygons", poly_inputs)["OUTPUT"]


polygons.setName(f"{layer.name().split('.shp')[0]}_polygons")
QgsProject.instance().addMapLayer(polygons)
