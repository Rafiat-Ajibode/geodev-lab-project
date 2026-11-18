import geopandas as gpd

print(gpd.list_layers("data/processed/my_wards.gpkg"))

wards = gpd.read_file("data/processed/my_wards.gpkg", layer="my_wards")

print(wards.head())
print("Rows and columns:", wards.shape)
print(wards.geom_type.value_counts())
print("CRS:", wards.crs)
print("Bounds:", wards.total_bounds)