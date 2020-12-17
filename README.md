# QGIS with conda

---

**Acknowledgement:**

This repo is greatly inspired by [CNFerrery](https://github.com/CNFeffery) 's work [here](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/（数据科学学习手札94）QGIS%2BConda%2Bjupyter玩转Python%20GIS).

---

## set up a QGIS environment in conda
in your terminal:
```
conda env create -f qgis_env.yaml
```
this will install QGIS, geopandas and other geospatial analysing tools.

## test the available algorithms

in your terminal:
```
# launch the environement
conda activate qgis_env

# test the environment
python test-qgis.py

```

this should print a whole lot of available working algorithms in your screen:
```
Aspect of  gdal:aspect is working
Assign projection of  gdal:assignprojection is working
Buffer vectors of  gdal:buffervectors is working
Build virtual raster of  gdal:buildvirtualraster is working
Build virtual vector of  gdal:buildvirtualvector is working
Clip raster by extent of  gdal:cliprasterbyextent is working
Clip raster by mask layer of  gdal:cliprasterbymasklayer is working
Clip vector by extent of  gdal:clipvectorbyextent is working
Clip vector by mask layer of  gdal:clipvectorbypolygon is working
Color relief of  gdal:colorrelief is working
Contour of  gdal:contour is working
...

Multi-ring buffer (constant distance) of  native:multiringconstantbuffer is working
Nearest neighbour analysis of  native:nearestneighbouranalysis is working
Offset lines of  native:offsetline is working
Order by expression of  native:orderbyexpression is working
Oriented minimum bounding box of  native:orientedminimumboundingbox is working
Orthogonalize of  native:orthogonalize is working
Package layers of  native:package is working
Raster pixels to points of  native:pixelstopoints is working
Raster pixels to polygons of  native:pixelstopolygons is working
Point on surface of  native:pointonsurface is working
Points along geometry of  native:pointsalonglines is working
Create layer from point of  native:pointtolayer is working
Pole of inaccessibility of  native:poleofinaccessibility is working
Extract layer extent of  native:polygonfromlayerextent is working
Polygonize of  native:polygonize is working
Polygons to lines of  native:polygonstolines is working
PostgreSQL execute SQL of  native:postgisexecutesql is working
Print layout map extent to layer of  native:printlayoutmapextenttolayer is working
```