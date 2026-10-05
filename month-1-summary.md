## Month 1 Summary

## Research Question
Which wards in Ado-Odo/Ota Local Government Area, Ogun State, Nigeria, are within 2 km of a health facility?

## Operation Run and Why
Buffered GRID3 health facilities by 2km, dissolved, then took the difference against ward boundaries and calculated the uncovered percentage of each ward. 
The buffer was used to visually identify wards located within 2 km of at least one health facility. To identify the wards covered by the buffer, I overlaid the buffer layer on Google imagery.

## Expected
Three or four peripheral wards flagged.

## Got
Three wards with over 30% of area uncovered, all on the northern and western edge.

## What Surprised Me
I noticed that the distribution of health facilities is not uniform across the LGA. Some areas have access to several health facilities, while other areas have access to fewer facilities within the 1 km buffer.

## Limitations
The analysis is based on the available GRID3 health facility data.
Some health facilities may not be mapped in the dataset.
The analysis does not consider factors such as road conditions, traffic, terrain, or the capacity and functionality of individual health facilities.

## What I Still Need
to verify the completeness and accuracy of the health facility dataset.
to verify the operational status of the health facilities.
to download and verify the settlement area dataset and identify any missing settlements.
to overlay the settlement dataset with the health facility buffer and calculate the percentage of settlements within 1 km.
to perform a network-based analysis using the road network to calculate actual travel distances or travel times.
Future updates will incorporate population, for more comprehensive flood modelling.
