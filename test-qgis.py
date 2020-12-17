# %%
# initialise QGIS
from qgis.core import *
from processing.core.Processing import Processing
from qgis.analysis import QgsNativeAlgorithms

Processing.initialize()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

for alg in QgsApplication.processingRegistry().algorithms():
        print(alg.displayName(), 'of ', alg.id(),  'is working')
# %%
