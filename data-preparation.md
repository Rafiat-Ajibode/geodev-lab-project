# DATA PREPARATION

## STUDY AREA
Ado-Odo/Ota LGA, Ogun State, Nigeria, extracted from GRID3 Nigeria LGA Boundaries

## COORDINATE REFERENCE SYSTEM
The source layers arrived in EPSG:4326 as the CRS, but were reprojected to EPSG:32631 (UTM ZONE 31N), which is suitable for area measurement.

## DATA REPROJECTED
The following data were reprojected as stated above and saved as a GeoPackage file.
- Ado-Odo/Ota LGA Boundary
- Wards
- Roads
- Health facilities

## DATA CLIPPED 
All layers (roads, health facilities, wards) were clipped to the study area, then reprojected to EPSG:32631 (UTM ZONE 31N). 

## QUALITY NOTES

# GRID3 Nigeria Ado-Odo/Ota LGA Boundaries
The clipped study area aligns with the satellite imagery to some extent, but it does not blend with the edges shown in the satellite imagery.

# GRID3 Nigeria Ado-Odo/Ota Operational Wards
The clipped Wards_in_Ado_Odo_Ota_LGA aligns with the satellite imagery almost 90%, but it does not match the boundary edges shown in the imagery. The wards were edited and published 30th June 2026

# OSM Roads, Ado-Odo/Ota LGA
- Extracted [20th September 2026] via Quick OSM, highway=*
- 25578 features, reprojected and clipped
- COMPLETENESS: good in built-up areas; covers 90% of roads within the study area, sparse at the northwestern and southwestern edges.   
- CURRENCY: most edits 2020-2024. New (6) structures within the Polytechnic (OGITECH, Igbesa) on Lusada-Igesa road are not present
- POSITIONAL: roads align well with satellite imagery; no systematic offset visible.
- ATTRIBUTE: Only about 10% or less carry a surface tag, so paved and unpaved cannot be separated reliably
- FITNESS: it's adequate for access analysis in the built-up area, but not adequate for a tag-related (paved) question.

# GRID3 Nigeria, Ado-Odo/Ota LGA Health Facilities v3.0 (published 13th August 2026)
- Extracted [20th September 2026] 
- 287 features, reprojected and clipped
- COMPLETENESS: covers 80% of known health facilities within the study area.
- CURRENCY: the health facilities were edited and published 13th August 2026.
- POSITIONAL: there were a few duplications, and some facilities didn't align with satellite imagery.
- ATTRIBUTE: all were properly tagged for analysis, but had some null values for facility_type, level, ownership, and functionality of the facilities.
- FITNESS: It's adequate for analysis but will require some corrections concerning the duplicates and null values.


