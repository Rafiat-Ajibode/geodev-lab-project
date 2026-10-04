# Data notes

## GRID3 Nigeria Operational Wards v3.0 (published 15th July 2026)
- Source: https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v3-0/about
- Dataset: Nigeria Operational Wards (GRID3) for Nigeria Ward Level Boundaries
- Downloaded: 20th September 2026
- Study area: Ado-Odo/Ota LGA, Ogun State
- 5872 features, polygons 
- Columns: OBJECTID (integer64), country (text), iso3 (text), state (text), state_code (text), lga (text), lga_alt_names (text), ward (text), ward_alt_names (text), ward_v1_grid3 (text), ward_in_grid3_ward_list    (decimal), multipart_count (decimal), source (text), date (date), area_sqkm (decimal).
- Columns_type: Text(string), Decimal(double), Integer(64 bit)
- Geometry: Polygon (MultiPolygon)
- Null values: No nulls in the ward column
- Coverage: The Nigeria Operational Wards GeoPackage file from Grid3 doesn't fully represent the boundary or cover the study area well.
- Notes: This layer was used to identify and define the Nigeria Ward Level Boundaries  of Ado-Odo/Ota LGA.


## GRID3 Nigeria LGA Boundaries 
- Source: https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about
- Dataset: Nigeria LGA Level Boundaries (GRID3)
- Downloaded: 20th September 2026
- Study area: Ado-Odo/Ota LGA, Ogun State
- 774 features, polygons 
- Columns: FID (integer), globalid (text), uniq_id (decimal), timestamp (date&time), editor (text), lganame (text), lgacode (decimal), statename (text), statecode (text), source (text), amapcode (text).
- Columns_type: Text(string), Decimal(double), Integer(64)
- Geometry: Polygon (MultiPolygon)
- Null values: No nulls in the lganame column
- Coverage: The Nigeria LGA Level Boundaries from Grid3 don't fully represent the boundary or cover the study area well; some parts of the boundaries are missing and don't fit.
- Notes: This layer was used to identify and define the Nigeria LGA-level boundaries  of Ado-Odo/Ota LGA.


## GRID3 Nigeria Operational State Boundaries 
- Source: https://data.grid3.org/datasets/GRID3::grid3-nga-operational-state-boundaries-/about
- Dataset: Nigeria Operational State (GRID3) for Nigeria Ward-Level Boundaries
- Downloaded: 20th September 2026
- Study area: Ado-Odo/Ota LGA, Ogun State
- 20 features, polygons 
- Columns: Fid (integer), globalid (text), uniq_id (decimal), timestamp (date&time), editor (text), lganame (text), lgacode (decimal), statename (text), statecode (text), source (text), amapcode (text). 
- Geometry: Polygon (MultiPolygon)
- Null values: No nulls in the statename column
- Coverage: The Nigeria Operational State Boundaries file from Grid3 fully represents the boundary and covers the study area well.
- Notes: This layer was used to identify and define the Nigeria Ward Level Boundaries  of Ado-Odo/Ota LGA.


## GRID3 Nigeria Health Facilities v3.0 (published 13th August 2026) 
- Source: https://data.grid3.org/datasets/827e3638dc204f4b9ddbbd19b00954d6/about
- Dataset: Health Facilities in Ado-Odo/Ota (GRID3) 
- Downloaded: 20 September 2026
- Study area: Ado-Odo/Ota LGA, Ogun State
- Features: 289 features, points
- Geometry: Point (Point)
- Columns: OBJECTID (decimal), unique_id, latitude, longitude, country, iso, state_standard, lga_standard, ward_standard, ward boundary, facility_name, alt_name,  settlement_name, facility_level etc.
- Null values: No null values in facility_name
- Coverage: Health facilities are properly mapped in the study area, but there is a need to determine if these facilities are still in good condition and functional for human use
- Notes: This layer will be used to assess the accessibility of wards to health facilities in Ado-Odo/Ota LGA.


## OSM roads, extracted via QuickOSM
- Source: https://www.openstreetmap.org/
- Query: highway =* within Ado_Odo_Ota_LGA_wards extent
- Extracted: 20 September 2026
- Features: 49562 lines
- Geometry: Line (LineString)
- Columns: fid, full_id, osm_id, osm_type, plant:source, seasonal, payment:bank   transfer, weather:rain, motorcycle, junction, motorroad, motor_vehicle etc.
- Coverage: The roads cover the LGA. Several road features are missing names (Null) and surface information, such as: road, construction, covered, cutting, embankment, psv, bus, motor vehicle, lit, sidewalk, service, horse, bicycle, access, foot, lanes, surface, bridge, ref, one_way, name, lanes. The majority of the features are unpaved and have null values, which doesn't give clarity on which areas are paved in the LGA. 
- Notes: The road network was extracted from OpenStreetMap using the QuickOSM plugin in QGIS.

  
## CRS and preparation
- All source layers arrived in EPSG:4326 
- Study area: Ado-Odo/Ota LGA, Ogun State, Nigeria, extracted from GRID3 Nigeria LGA Boundaries 
- All layers clipped to study area, then reprojected to EPSG:32631 (UTM 31N) 
- Area check: Ado-Odo/Ota LGA 853 km2, matches published figure 
- Working files in data/processed/, raw files untouched 
