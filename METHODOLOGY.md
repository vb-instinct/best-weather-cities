# How this atlas works

Map edition, checked 14 October 2026. All climate inputs cover 1991-2020.

## Your default comfort rule

A month passes when its **average daily high is 18-28 C**, model-derived mean wind at 10 m is **at most 3 m/s**, model-derived relative humidity at 2 m is **at most 60%**, and precipitation is **20-100 mm/month**. The wind, humidity and rain limits are editable. A second temperature setting requires both average low and average high to fall within 18-28 C. The default interprets 18-28 C as daytime weather, not warm nights; the low is always shown.

These are starting preferences, not a scientific comfort index, medical limits or proof of no wind. Literal zero wind year-round is not realistic as a climate promise. Relative humidity changes with temperature and does not replace dew point or heat stress. A rain lower bound distinguishes moderate rainfall from an arid climate; set it to zero if dry is preferable.

**Year-round fit requires all 12 monthly averages to pass every selected limit.** A high fit score alone is not a year-round match. Monthly averages cannot establish how many individual days are comfortable or capture gusts, hot afternoons or heavy storms.

## Map colors and scoring

For comfort mode, each of four components gets 100 within its selected range. Outside the range, deduct 100 times distance from the nearest limit divided by: 15 C for temperature, 150 mm for rainfall, 40 percentage points for humidity, 5 m/s for wind. Clip each component to 0-100. The monthly fit score is the equal-weight mean of the four. In low-and-high temperature mode, the temperature component is the lower of the high and low scores.

Year view averages the 12 monthly scores. Month view uses that month's score. Colors: 90-100 dark green, 75-89 green, 50-74 tan, under 50 grey. A missing wind or humidity month makes the comfort score unavailable for that month; any such month makes the year score unavailable. Missing values are never calm, dry or zero. Color cutoffs, weights and penalty scales are editorial. Tiny differences are not evidence of superiority.

Within-country ranks sort by selected-month pass first (if selected), then fit-month count, then fit score, temperature-fit count, lower annual precipitation and name. Ranking is among this country's included candidates, not every city. There is no national or worldwide champion claim.

Legacy modes remain: mild + drier (high 18-28 C, low 8-20 C, rain ≤100 mm); mild temperature (same temperatures, no rain limit); warmer (high 22-32 C, low 12-24 C, rain ≤150 mm). In these modes wind/humidity are displayed but deliberately not scored, and map score is the share of rule-fit months times 100 (or a pass/fail 100/0 for one month).

## Temperature and rain: station observations

85 records use national meteorological-service WMO submissions hosted by NOAA NCEI, from 1991-2020 min24 composite files. The archive uses at least 24 reported years; unspecified counts are assumed to be 30. Parameters: TMAX mean daily maximum C, TMIN mean daily minimum C, PRCP precipitation mm, DP01 days with ≥1 mm. Five Portuguese records use IPMA 1991-2020 PDFs, version 1.0 of 2024.

Candidate selection began with a 2016 SMH article, expanded to coastal, highland and seasonal alternatives. Data access shaped coverage. The 90 cities in 23 countries are a curated, uneven sample, not a statistical census. Ecuador and Namibia are absent because comparable verified core station series were not obtained. Five incomplete core records were excluded: Guanajuato, Naples, Catania, Caxias do Sul and Musanze/Ruhengeri. Guatemala candidates remain withheld pending reconciliation of station/value anomalies.

## Wind and humidity: separately modeled supplement

NASA POWER's custom climatology API returns **January 1991-December 2020**, verified in every response header. RH2M is relative humidity at 2 m (%); WS10M is mean wind speed at 10 m (m/s). Values originate in NASA's **MERRA-2 assimilation/reanalysis model**, not direct station observations. Source resolution is 0.5° latitude by 0.625° longitude, roughly 50 km, with variable east-west width. All 90 candidates have 12 usable months for both parameters in this edition; no values were filled in.

Requests use the city anchor, not the temperature/rain station. That matters especially near coasts, mountains and airports. The grid can mix ocean, coast, urban and inland terrain. Los Angeles (coast), for example, uses the city anchor for its grid, not a particular coastal neighbourhood. Do not interpret the extra decimal places returned by the API as local accuracy. Sheltered streets, sea breezes, altitude and gusts can differ greatly.

## Map locations and boundaries

City anchors come from GeoNames via Open-Meteo, filtered by country and checked by name and administrative region. Mysuru and Marrakech required corrected search aliases; the first Mysore result was a Bengaluru-area locality and was rejected. Map dots represent cities, **not station coordinates**. Suspect original station geolocation fields (notably Auckland) were not used. Exact query links and returned names are preserved in JSON. Generalized map outlines are Natural Earth public-domain 1:110m countries; boundaries are for orientation, not a territorial claim. The map is equirectangular, with distortion toward the poles. Some small islands are smaller than the map outlines can show, but their city dots remain available.

## Local proxies and excluded measures

Gran Canaria airport is on another coast from Las Palmas; San Francisco airport is south of the city; Fiumicino is not central Rome; Medellin uses Olaya Herrera, not Rionegro. Each record retains its exact station and caveat. The grid supplement does not fix these proxies.

Sunshine, fog, UV, air quality, sea temperature, flood/fire/cyclone exposure and heat-wave frequency remain outside the score. Historical normals are not forecasts; warming can make 1991-2020 cooler than present conditions. This is climate context, not a safety, health or relocation score.

## Reuse and updates

The page embeds its data and map outlines and works offline. CSV/JSON preserve all inputs and exact source URLs. `enrich.py` fetches coordinate and NASA supplement responses, verifies period and units, caches source bytes, and leaves gaps explicit on failure. Review every changed coordinate match before publication; cached responses should be removed deliberately for refresh. `check_data.py` audits the committed inputs and CSV. Temperature/rain updates still require the exact source station and period, comparison to prior values and investigation of anomalies. Do not mix changing default POWER periods or all-years station averages with 1991-2020.
