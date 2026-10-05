## Month 1 Summary

## Research Question
Which wards in Ado-Odo/Ota Local Government Area, Ogun State, Nigeria, are within 2 km of a health facility?

## Operation Run and Why
- Buffered GRID3 health facilities by 2km, dissolved, then took the difference against ward boundaries and calculated the uncovered percentage of each ward. 
- The buffer helped visually identify wards within 2 km of at least one health facility. To identify the wards covered by the buffer, I overlaid the buffer layer on Google satellite.

## Expected
Three or four peripheral wards flagged.

## Got
Three wards with over 30% of the area uncovered, all on the northern and western edge.

## What Surprised Me
- I noticed that the distribution of health facilities is not uniform across the LGA. Some wards have access to several health facilities, while others have access to fewer facilities within the 2 km buffer. 
- The facilities data undercounts. Of the four clinics that I personally know, only two are correct; the other two are wrongly named. 
- The real coverage is better than this analysis suggests, and I cannot say by how much.

## Limitations
- The analysis is based on the available GRID3 health facilities data.
- Some health facilities may not be mapped in the dataset, which means the data is incomplete.
- The analysis does not consider factors such as road conditions, traffic, terrain, or the capacity and functionality of each health facility.
- The facility type labels are inconsistent, so I counted all types together rather than weighting by capability.

## What I Still Need
- To verify the completeness and accuracy of the health facility dataset.
- Road network with surface, for travel distance in month five.
- Population per ward, to convert area uncovered into people uncovered, which is the number that actually matters.
