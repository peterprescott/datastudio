# Objectives
To build a new geodemographic classification for London that captures the characteristics of contemporary population and the places in which they live.

# A Framework

## Preliminary
* 0.1 Geography
https://geoportal.statistics.gov.uk/datasets/output-area-to-ward-to-local-authority-district-december-2018-lookup-in-england-and-wales
Output_Area_to_Ward_to_Local_Authority_District_December_2018_Lookup_in_England_and_Wales.csv

    This file is a best-fit lookup between output areas (December 2011), electoral wards/divisions and local authority districts in England and Wales as at 31st December 2018.
    
0.2 Postcode to OA/LSOA/MSOA
http://geoportal.statistics.gov.uk/datasets/postcode-to-output-area-to-lower-layer-super-output-area-to-middle-layer-super-output-area-to-local-authority-district-november-2018-lookup-in-the-uk

    A best-fit lookup between postcodes, frozen  2011 Census Output Areas (OA), Lower Layer Super Output Areas (LSOA), Middle Layer Super Output Areas (MSOA) and current local authority districts (LAD) as at November 2018 in the UK. Postcodes are best-fitted by plotting the location of the postcode's mean address into the areas of the output geographies


## 1. Population Characteristics
* 1.1 Age - https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/bulletins/annualsmallareapopulationestimates/mid2018/relateddata?:uri=peoplepopulationandcommunity/populationandmigration/populationestimates/bulletins/annualsmallareapopulationestimates/mid2018/relateddata&:uri=peoplepopulationandcommunity/populationandmigration/populationestimates/bulletins/annualsmallareapopulationestimates/mid2018/relateddata&page=1

    Mid-year (30 June 2018) estimates of the usual resident population for 2011 Census Output Areas (OAs) in the London region of England. Open Govt License (OGL).  {Output Area; Sex (Male/Female); Age (0 >= x >= 90+)}

* 1.2 Ethnicity
* 1.3 Churn - This could come from UCL
* 1.4 Families - https://data.london.gov.uk/dataset/pan-london-school-place-demand

    Ward-level projections of demand for school places over the period 2017-2028. License not specified, copyright Greater London Authority. {Ward (NOT Output Area); Academic Year; Residential Population; School Demand ({State/Non-State}x{Primary/Secondary}).

## 2. Economic Circumstances
* 2.1 Income Estimate - https://data.london.gov.uk/dataset/ons-model-based-income-estimates--msoa

    The small area model-based income estimates are the official estimates of average (mean) household income at the middle layer super output area (MSOA) level in England and Wales for 2011/12, 2013/14 and 2015/16. (OGLv3). {Middle Super Output Area; Annual Income Estimate ({Total/Net/Net before Housing Costs};{Lower < x < Upper Confidence Interval}; {Year (2012/2014/2016) NB: '12 and '14 weekly, '16 annual}). 
    

* 2.2 County Courth Judgements - https://data.cdrc.ac.uk/dataset/county-court-judgement

    Need to be granted access.

* 2.3 Free School Meals - https://data.london.gov.uk/dataset/london-schools-atlas

    (OGLv2). {LSOA; Total resident pupils; Number eligible for free school meals}

## 3. Work and Employment
* 3.1 Nightime Economy - https://data.london.gov.uk/dataset/london-night-time-economy

    (OGLv3). {Employees; Workplaces; Boroughs; MSOA; Year (2001 < x < 2017)}

## 4. Transport
* 4.1 PTAL - https://data.london.gov.uk/dataset/public-transport-accessibility-levels

    PTALS are a detailed and accurate measure of the accessibility of a point to the public transport network, taking into account walk access time and service availability. The method is essentially a way of measuring the density of the public transport network at any location within Greater London. 
    Each area is graded between 0 and 6b, where a score of 0 is very poor access to public transport, and 6b is excellent access to public transport.
    
    {LSOA; PTAL score; PTAL grade}

## 5. Housing
* 5.1 Price - See Jacob

    https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads
    OGLv3. 

* 5.2 Rent V Ownership
* 5.3 Mortgage Debt - https://www.ukfinance.org.uk/data-and-research/data/mortgages/mortgage-lending-within-uk-postcodes

    Value of residential mortgage loans outstanding in UK, split by sector postcode.  {Postcode Sector; 2013 < Quarter < 2019; Value of residential mortgage loans outstanding}

* 5.4 Rental Prices - CDRC Zoopla Data
* 5.5 New Builds / Flats (Gentrification?) -
 https://data.london.gov.uk/dataset/planning-permissions-on-the-london-development-database--ldd-
 
 (OGLv3). Housing completions recorded on the London Development Database, covering the period 01/04/2012 - 31/03/2019. Lots of data... perhaps {Ward; Proposed Units}
 
* 5.6 Energy - https://www.gov.uk/government/collections/sub-national-electricity-consumption-data#postcode-level-data

{Local Authority ~ LSOA; Domestic energy consumption (Total/Mean/Median); Number of domestic electricity meters}

## 6. Environment
* 6.1 Emissions - https://data.london.gov.uk/dataset/pm2-5-map-and-exposure-data

    OGLv3. Output Area.
