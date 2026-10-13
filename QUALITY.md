# Quality checks and remaining limits

## Data checks

- All 90 records have twelve monthly highs, lows and precipitation values.
- Every high is at least its corresponding low; precipitation is non-negative.
- The 1,080 CSV rows match the JSON high and precipitation arrays exactly.
- Missing source values are not imputed or turned into zeros.
- All records use the same 1991-2020 period. Portuguese PDFs identify version 1.0 of 2024.
- WMO composite rows are matched by country and exact original station name, not by fuzzy city-name similarity.
- Station names, station IDs and source parameter URLs are retained.
- Annual rain shown in the page is the sum of rounded monthly values, explicitly labelled. It can differ slightly from a source annual value.
- Five incomplete candidate records were excluded. Guatemala candidates were withheld for unresolved station/value anomalies, not silently repaired.
- Some source coordinates looked suspect. Coordinates are not used or published; no map or distance inference is made.

## Interface checks

- The page was rendered at 320, 390 and 1280 pixels.
- Long city and station labels, month chips, units and caveats wrap inside the mobile width.
- Country filter, city search, month selection, all preference buttons, reset and empty-state behaviour were exercised.
- Monthly disclosures contain the actual data; charts use the same -5 to 40 C scale for every city and exact values are printed below.
- Every city record remains in the HTML even without JavaScript; source links and downloadable CSV/JSON remain available. Dynamic fit summaries require JavaScript.
- No external scripts, stylesheets, fonts, tracking or runtime API requests. The page works offline once downloaded.

## Limits that matter

The candidate sample is curated and uneven; ranks mean best among included cities, not national champions. Monthly averages cannot establish daily comfort, humidity, wind, fog, sunshine, UV, air pollution, sea temperature or hazard exposure. Stations are local proxies, especially at airports. Climate change can make historical normals cooler than present-day conditions.

## Upgrade priorities

1. Reconcile the Guatemala anomalies with the national meteorological service before adding its cities.
2. Obtain direct Las Palmas city and central Rome normals instead of relying on coastal airport proxies.
3. Add Ecuador and Namibia using verified comparable station normals.
4. Expand thin country samples, especially Italy and the United Kingdom.
5. Add independently sourced humidity/dew point, wind, sunshine and extreme-event indicators. Do not blend them into an unexplained score.
6. Add neighbourhood/station context and hazard guidance without pretending this is a safety or relocation ranking.

These are improvement priorities, not scheduled promises. Corrections should identify the exact station, month, source and baseline period so the evidence can be checked.
