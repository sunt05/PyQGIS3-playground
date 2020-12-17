# QGIS with conda

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