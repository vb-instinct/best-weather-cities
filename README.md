# Good weather, city by city

**[Open the interactive map atlas](https://vb-instinct.github.io/best-weather-cities/)**

90 cities in 23 countries. Map edition checked 14 October 2026. All climate inputs cover 1991-2020.

## Start with the map

Choose a country or search a city, then tap a colored dot. See monthly temperature, rain, mean wind and relative humidity together. Drag to pan, use + / − to zoom, or choose "Fit cities". Choose one travel month or compare the year. Open monthly values and source links from each city.

The default preference is daytime monthly average highs **18-28 C**, light mean wind **≤3 m/s**, lower relative humidity **≤60%** and moderate rainfall **20-100 mm/month**. Adjust wind, humidity and rain under "Adjust the comfort rule". You can require both monthly average lows and highs to be 18-28 C instead. Legacy mild+drier, mild-temperature and warmer modes remain.

**Year-round fit means all 12 months pass every selected limit.** A high average score is not the same thing. The cutoffs and score weights are editable/editorial preferences, not scientific or medical limits. No wind is not realistic as a year-round promise.

## Know what the numbers represent

Temperature/rain are station normals from national-service WMO submissions hosted by NOAA NCEI (85 records) and IPMA PDFs (five Portuguese records). Wind/humidity are **NASA POWER / MERRA-2 model-derived grid climatologies**, not station readings. The period is custom 1991-2020, checked in every NASA response.

The model grid is roughly 50 km across. Coastal, mountain, airport and neighbourhood weather can differ. City map anchors are separately checked GeoNames locations via Open-Meteo, not station coordinates. Both sources and spatial caveats stay visible. Every candidate has complete wind/humidity arrays in this edition; future gaps are displayed, never filled as zero.

This is a curated shortlist, not every city or country. Ranks compare candidates within each country's included shortlist. Sunshine, fog, UV, air quality and extreme-event risks are not scored. Climate is not a forecast, safety assessment or relocation recommendation.

## Files and audit trail

| File | Purpose |
| --- | --- |
| [index.html](index.html) | Self-contained clickable, zoomable map, filters, score controls, city details and monthly values. Works offline after download; no keys, scripts, tracking or runtime API requests. |
| [cities.json](cities.json) | All station and model arrays, city anchors, exact source URLs and NASA response hashes. |
| [cities-monthly.csv](cities-monthly.csv) | 1,080 rows, including model wind/humidity, coordinates, periods and source links. |
| [METHODOLOGY.md](METHODOLOGY.md) | Exact fit rules, score formula, missing-data policy, spatial caveats and updates. |
| [SOURCES.md](SOURCES.md) | Primary sources, retrieval dates and hashes. |
| [QUALITY.md](QUALITY.md) | Checks and remaining limits. |
| [check_data.py](check_data.py) | Dependency-free offline data audit. |
| [enrich.py](enrich.py) | Re-fetch coordinates and the explicit-period NASA supplement. Review every changed location before publishing. |

Countries: Argentina, Australia, Brazil, Chile, China, Colombia, Cyprus, France, India, Italy, Japan, Mexico, Morocco, New Zealand, Portugal, Rwanda, South Africa, Spain, Tunisia, Turkiye, United Kingdom, United States, Uruguay. Sample sizes vary; Italy and the UK have only two candidates each. Ecuador and Namibia remain unranked for missing verified core data.

No personal data, credentials or copied article text are included. Natural Earth map outlines are public domain. Location data: GeoNames via Open-Meteo. Original climate data rights remain with their publishers. The SMH Traveller article inspired the first shortlist, not current rankings.
