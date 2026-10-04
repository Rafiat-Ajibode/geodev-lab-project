# My project brief 

# Spatial Accessibility to Health Facilities in Ado-Odo/Ota LGA, Ogun State, Nigeria.

## The question

**Which wards in Ado-Odo/Ota Local Government Area, Ogun State, Nigeria, are more than 2km from a health facility?**

## Why It Matters

The geographic distance between communities and health facilities affects access to essential healthcare services. Identifying underserved wards located more than 2 km from a health facility can help reveal areas where residents may have limited access to healthcare and inform decisions on where adequate access to health facilities or services should be prioritized in Ado-Odo/Ota LGA, Ogun State.

## The Data I need 

- Ward boundaries
- Health facility locations
- Ado-Odo/Ota LGA boundary
- Road network data
- Population data 

## The Dataset Sources

- **Ward boundaries:** - (GRID3 Nigeria – Geospatial Data) - https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v3-0/about - GeoPackage - 191 MB
- **State Boundaries** - (GRID3 Nigeria – Geospatial Data) - https://data.grid3.org/datasets/GRID3::grid3-nga-operational-state-boundaries-/about - GeoPackage - 2 MB
- **LGA and administrative boundaries:** - (GRID3 Nigeria – Geospatial Data) - https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about - GeoPackage - 4.3 MB
- **Health facility locations:** - (GRID3 Nigeria – Geospatial Data) - https://grid3.org/geospatial-data-nigeria - GeoPackage - 16 MB
- **Road network data:** - (OSM via QuickOSM) - https://plugins.qgis.org/plugins/QuickOSM/ - extracted for Ado-Odo/Ota LGA
- **Population Data:** - (GRID3 Nigeria – Geospatial Data) / (WorldPop) – https://grid3.org/geospatial-data-nigeria / https://www.worldpop.org - 43.61 MB

## What I would build

Using the ward boundaries and health-facility locations, I can create a 5-km health-service accessibility map showing which wards fall outside the 5-km distance from the nearest health facility. The analysis can help government and planners prioritise underserved wards for new health centres, upgrading existing facilities, mobile healthcare services, or improved referral/access arrangements. Adding the population data would make the results more useful because I can estimate how many residents are affected in each underserved ward, rather than only identifying the locations.

The results would be useful to the following parastatals:
- Ogun State Ministry of Health
- Ogun State Ministry of Physical Planning and Urban Development
- Ado-Odo/Ota LGA authorities
- Primary Health Care Development Agency
- Urban and regional planners
- Public health planners and NGOs 
