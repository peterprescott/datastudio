import geopandas as gpd
import geoplot
import os.path
import sys


data = gpd.read_file(os.path.join(sys.path[0], 'data', 'ESRI','LSOA_2011_London_gen_MHW.shp'))

data.plot()
