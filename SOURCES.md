# Sources and audit trail

Retrieved 13 October 2026. Climate baseline 1991-2020.

## SMH Traveller, David Whitley (2016)

Inspiration only. Original question and candidate ideas, not inherited ranks or data.

https://www.smh.com.au/traveller/reviews-and-advice/the-worlds-greatest-climates-top-cities-to-visit-for-perfect-weather-all-year-round-20161104-gshzcu.html

## NOAA NCEI / WMO normals

Primary archive. National-service 1991-2020 submissions; min24 convention and parameter definitions.

https://www.ncei.noaa.gov/products/wmo-climate-normals

## IPMA station normals

Primary national data. Five Portuguese station PDFs, version 1.0 of 2024.

https://www.ipma.pt/en/oclima/normais.clima/1991-2020/normalclimate9120.jsp

## AEMET Santa Cruz normals

Cross-check only. Station identity and definitions; older 1981-2010 numbers are not mixed into our dataset.

https://www.aemet.es/es/serviciosclimaticos/datosclimatologicos/valoresclimatologicos?l=C449C

## NOAA Climate.gov

Climate explanation. Historical normals change as climate warms.

https://www.climate.gov/news-features/understanding-climate/climate-change-and-1991-2020-us-climate-normals

## WHO heat and health

Health context. Heat depends on humidity, wind and radiant heat, not just air temperature.

https://www.who.int/news-room/fact-sheets/detail/climate-change-heat-and-health

## WHO UV index

Health context. UV is separate from comfortable air temperature.

https://www.who.int/news-room/questions-and-answers/item/radiation-the-ultraviolet-%28uv%29-index

## Copernicus thermal comfort

Technical context. UTCI is a separate thermal stress dataset; not calculated here.

https://cds.climate.copernicus.eu/datasets/derived-utci-historical?tab=overview

## ScienceDaily (2014)

Independent historical discussion. Darack/Weatherwise discussion; no historic ranking imported.

https://www.sciencedaily.com/releases/2014/03/140320173249.htm

## WMO min24 TMAX

https://www.ncei.noaa.gov/archive/accession/0253808/data/0-data/data-composite-primary-parameters-min24/wmo_normals_9120_TMAX_min24.csv

SHA-256: `aeb759deb11e9422423206b18f9649525c9620e8d8be855708a656448a254abb`

## WMO min24 TMIN

https://www.ncei.noaa.gov/archive/accession/0253808/data/0-data/data-composite-primary-parameters-min24/wmo_normals_9120_TMIN_min24.csv

SHA-256: `3faef64b30a98ef1b37d79b8cd01cdd6a1156937cc0d4de81fa198c482372aad`

## WMO min24 PRCP

https://www.ncei.noaa.gov/archive/accession/0253808/data/0-data/data-composite-primary-parameters-min24/wmo_normals_9120_PRCP_min24.csv

SHA-256: `801539eae2aab9d65548489670b4b79e238754b47f84d3a9693724745f5a3cf4`

## WMO min24 DP01

https://www.ncei.noaa.gov/archive/accession/0253808/data/0-data/data-composite-primary-parameters-min24/wmo_normals_9120_DP01_min24.csv

SHA-256: `8e78c3dd883090f9384d5d7c457a3bbcb3541b91664e1fc9b88850d8d38f6bf2`

## Funchal, IPMA station 522

https://www.ipma.pt/bin/file.data/climate-normal/cn_91-20_FUNCHAL.pdf

1991-2020 version 1.0 of 2024. TX, TN, precipitation and >=1 mm days transcribed from original PDF.

## Faro, IPMA station 554

https://www.ipma.pt/bin/file.data/climate-normal/cn_91-20_FARO.pdf

1991-2020 version 1.0 of 2024. TX, TN, precipitation and >=1 mm days transcribed from original PDF.

## Ponta Delgada, IPMA station 513

https://www.ipma.pt/bin/file.data/climate-normal/cn_91-20_PONTA_DELGADA_OBSERVATORIO.pdf

1991-2020 version 1.0 of 2024. TX, TN, precipitation and >=1 mm days transcribed from original PDF.

## Lisbon, IPMA station 535

https://www.ipma.pt/bin/file.data/climate-normal/cn_91-20_LISBOA_GEOFISICO.pdf

1991-2020 version 1.0 of 2024. TX, TN, precipitation and >=1 mm days transcribed from original PDF.

## Porto, IPMA station 545

https://www.ipma.pt/bin/file.data/climate-normal/cn_91-20_PORTO_PEDRAS_RUBRAS.pdf

1991-2020 version 1.0 of 2024. TX, TN, precipitation and >=1 mm days transcribed from original PDF.

## Exclusions

Incomplete core series: Guanajuato, Naples, Catania, Caxias do Sul, Musanze/Ruhengeri. Guatemala station/value anomalies withheld pending national-source reconciliation. Suspect source geolocation fields not used. No missing data imputed. See methodology.

## Map edition supplement, retrieved 14 October 2026

NASA POWER climatology API and custom-period syntax:
https://power.larc.nasa.gov/docs/services/api/temporal/climatology/

NASA POWER meteorological methodology (MERRA-2, grid resolution, observation assimilation and heights):
https://power.larc.nasa.gov/docs/methodology/meteorology/

NASA POWER API tutorial (resolution and at most five concurrent requests):
https://power.larc.nasa.gov/docs/tutorials/service-data-request/api/

GeoNames city locations via Open-Meteo geocoding, country and feature-code definitions:
https://open-meteo.com/en/docs/geocoding-api

Natural Earth public-domain use terms:
https://www.naturalearthdata.com/about/terms-of-use/

Natural Earth countries 1:110m and boundary caveats:
https://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-0-countries/

Downloaded GeoJSON source, compiled into the page's map paths:
https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson

Every city's exact NASA API URL and GeoNames/Open-Meteo query URL is in cities.json and the CSV. The NASA response SHA-256 and custom 1991-2020 period are also in JSON. The wind/humidity numbers are model-derived, not a new set of national-service station normals. Core station-source dates and hashes above are unchanged.
