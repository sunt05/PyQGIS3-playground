# %%
# initialise QGIS
from qgis.core import *
from processing.core.Processing import Processing
from qgis.analysis import QgsNativeAlgorithms
from processing import algorithmHelp,run

import geopandas as gpd

#%%
Processing.initialize()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

for alg in QgsApplication.processingRegistry().algorithms():
        print(alg.displayName(), 'of ', alg.id(),  'is working')
# %%
shp_CQ = QgsVectorLayer('Chongqing.geojson')
chongqing = gpd.read_file('Chongqing.geojson')

total_bounds = chongqing.to_crs('EPSG:2381').total_bounds
# %%
# get help info of a specific algorithm
algorithmHelp("native:creategrid")
# %%
params = {
    'INPUT': chongqing,
    'TYPE': 2,
    'EXTENT': f'{total_bounds[0]},{total_bounds[2]},{total_bounds[1]},{total_bounds[3]}',
    'HSPACING': 10000,
    'VSPACING': 10000,
    'HOVERLAY': 0,
    'VOVERLAY': 0,
    'CRS': 'EPSG:2381',
    'OUTPUT': 'gridded_CQ.geojson' # export the processed file
}
feedback = QgsProcessingFeedback()
run("native:creategrid", params, feedback=feedback)
# %%
gpd.read_file('./gridded_CQ.geojson')
# %%
