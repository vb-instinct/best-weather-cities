# How this atlas works

Research checked 13 October 2026. Climate baseline: 1991-2020 throughout.

## What the ranking means

This is a curated comparison of 90 city/station candidates in 23 countries, not an exhaustive survey of all cities or all countries. Rank means "best match among the cities included in this country under the selected rule". It is neither a worldwide league table nor a quality-of-life score. Equal month counts are broken by the number of temperature-fit months, then lower annual precipitation, then city name. Tiny score differences are not meaningful evidence of superiority.

The default **mild + drier** rule counts a month when its average daily high is 18-28 C, its average daily low is 8-20 C, and its average monthly precipitation is at most 100 mm. The **mild temperature** rule removes the rain limit. The **warmer** rule uses average highs of 22-32 C, lows of 12-24 C, and precipitation at most 150 mm. These thresholds are editorial preferences, not medical safety limits, tourism standards, daily comfort probabilities or an established scientific index. Change the rule: the ranking can change sharply.

Why use simple rules? A visible rule can be challenged. An unexplained weighted "perfect climate" score cannot. No claim is made that 101 mm is uncomfortable and 99 mm is comfortable. Month counts are screening indicators. Use the actual monthly values and rain days for the decision.

## Sources and selection

The 85 non-Portuguese station records are extracted from national meteorological-service submissions to the WMO, hosted in NOAA NCEI's 1991-2020 min24 composite files. The files contain values based on at least 24 years of reported observations; where a year count is not provided, the archive assumes 30. The source parameter files are TMAX (mean daily maximum, C), TMIN (mean daily minimum, C), PRCP (precipitation amount, mm), and DP01 (days with at least 1 mm precipitation). Missing values are not zeros.

Five Portuguese records come directly from IPMA's 1991-2020 station normals, version 1.0 of 2024: Funchal, Faro, Lisbon Instituto Geofisico, Porto Pedras Rubras and Ponta Delgada Observatorio Afonso Chaves. These use the same climate period, but their source and station identifiers remain separate from the WMO composite.

Candidate selection began with the supplied 2016 SMH travel article, then expanded to coastal, highland and seasonal alternatives across regions. Data access and complete monthly series also shaped coverage. It is not a representative statistical sample. Countries absent from the atlas are not judged to have bad weather. Ecuador and Namibia, both discussed by the article, are not quantitatively ranked here because comparable verified 1991-2020 station series were not obtained in this run.

Only candidates with complete 12-month high, low and precipitation arrays are ranked. Five candidates were excluded for incomplete core data: Guanajuato, Naples, Catania, Caxias do Sul and Musanze/Ruhengeri. Guatemala candidates were withheld after the composite returned implausible station/value combinations requiring reconciliation with the national source. They were not silently corrected. Some source geolocation fields also looked suspect (notably Auckland); no maps or coordinate-based interpretations are generated. The month arrays are used as published, with uncertainty kept visible.

## Stations are not cities

A single station is a proxy. Airports can be warmer, cooler, drier, windier or higher than where a visitor will stay. Gran Canaria airport is on a different coast from Las Palmas: that row is an island-coastal lead, not a direct Las Palmas city normal. San Francisco airport is south of the city. Rome's Fiumicino airport is coastal, not central Rome. Medellin uses Olaya Herrera in the valley, not the higher airport near Rionegro. The exact original station name and identifier are visible in every record and in the downloadable CSV.

## Climate is not the forecast

A normal describes a historical average over 30 years. It is not the weather expected on a particular date, the maximum temperature ever reached, or a guarantee against heavy rain. A month averaging a 25 C daily high can include dangerous heat. A dry month can include a damaging storm. Climate change means the 1991-2020 baseline can understate present-day warmth. No 2026 observations, real-time forecasts or future projections are mixed into these tables.

## What is deliberately not scored

Humidity/dew point, wind, cloud, fog, sunshine, UV, air pollution, sea temperature, flood/fire/cyclone exposure and heat-wave frequency are not available on a consistently verified basis for this candidate set. Missing coverage is not evidence of low risk. WHO notes that heat stress depends on temperature, humidity, air movement and radiant heat; UV risk cannot be inferred from pleasant air temperature. Check all of these before a trip or relocation. Visa rules, safety, housing, healthcare, language and cost of living are outside this climate-only project.

## Reading the display

- "High" means the monthly average of daily maxima, not the day's forecast or a record maximum.
- "Low" means the monthly average of daily minima, not a minimum you can rely on every night.
- "Rain" is mean monthly precipitation in mm. 1 mm is 1 litre per square metre.
- "Rain days" means days with at least 1 mm of precipitation; missing is shown as "not available".
- Highlighted months pass the chosen rule. A month that does not pass is not necessarily a bad month to visit.
- "Fit months" is a count of qualifying monthly averages, never a count or percentage of comfortable days.

## Reuse and updates

The CSV and JSON preserve station-level provenance. The source ledger lists the exact data URLs, retrieval date and file hashes. For an update, fetch the current composite files, reselect the same station names and identifiers, preserve the period, compare changes and investigate anomalies before publishing. Do not mix all-years Bureau of Meteorology averages with fixed-period WMO normals without relabelling them. Data rights remain with the original publishers; no source photographs or article text are republished.
