# Quality checks and remaining limits

Map edition, 14 October 2026.

## Data

- 90 cities, 23 countries, twelve station high/low/rain values each; 1,080 CSV rows.
- CSV station and supplemental fields checked against JSON with `python3 check_data.py`.
- All 90 NASA responses confirm custom January 1991-December 2020 and units RH2M %, WS10M m/s. No missing wind/humidity values in this edition.
- Every city anchor checked against returned country, settled-place type, name and administrative region. Rejected a "Mysore Road Tolgate" match near Bengaluru and fetched Mysuru; Marrakech required Marrakesh spelling. Original suspect station coordinates not used.
- Exact query URLs and NASA response hashes preserved. No model values claimed as station observations.
- Missing future values produce an unavailable comfort score, never zero or calm. City details say "not available"; legacy rules can still compare core temperature/rain.
- Wind is mean at 10 m, not gusts or an assurance of no wind. Humidity is relative humidity at 2 m, not dew point.
- Station and modeled grid samples are geographically distinct, with limitations beside details and in methodology.

## Interface

The map is compiled from Natural Earth outlines and embedded data, with no keys, runtime tile services, tracking or external libraries. Map dots are city anchors. The original monthly cards retain accessible source links and a no-JavaScript station-data fallback; map controls and dynamic scores require JavaScript.

Checks include desktop/mobile layout, city click details, country filter, monthly recoloring, preference switches, adjusted comfort limits, zoom, fit-to-country and reset. The whole-year score is not presented as year-round qualification; all 12 months must pass. See the task's visual evidence for the final live checks.

## Remaining limits

The city shortlist is curated and uneven. Monthly historical averages cannot count comfortable days or show extremes. Model grid cells (0.5° × 0.625°) can combine sea, urban, coast, hills and inland conditions. Local sheltered areas and neighbourhoods can differ sharply. Temperature/rain stations remain proxies, notably Gran Canaria, San Francisco and coastal Rome. The equirectangular map distorts toward the poles; small islands can be below its outline resolution. Generalized boundaries are orientation, not territorial claims.

UV, sunshine, fog, air quality, sea temperature, flood/fire/storm exposure and climate-change projections remain outside the score. Gaps in those measures do not mean low risk. This is not an exhaustive world ranking, health guidance or a relocation recommendation.
