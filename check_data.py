"""Run: python3 check_data.py. No dependencies or network access."""
import csv
import json
from pathlib import Path

root = Path(__file__).resolve().parent
cities = json.loads((root / 'cities.json').read_text())
rows = list(csv.DictReader((root / 'cities-monthly.csv').open()))
assert len(cities) == 90
assert len({c['country'] for c in cities}) == 23
assert len(rows) == len(cities) * 12
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
assert len({c['number'] for c in cities}) == len(cities)
for city in cities:
    assert city['period'] == '1991-2020'
    for field in ['TMAX', 'TMIN', 'PRCP', 'DP01']:
        assert len(city[field]) == 12, (city['city'], field)
    assert all(h >= l for h, l in zip(city['TMAX'], city['TMIN']))
    assert all(r >= 0 for r in city['PRCP'])
    matches = [r for r in rows if r['country'] == city['country'] and r['city'] == city['city']]
    assert len(matches) == 12
    for i, row in enumerate(matches):
        assert row['month'] == months[i]
        assert row['station_id'] == city['id']
        for csv_key, json_key in [('mean_daily_high_c', 'TMAX'), ('mean_daily_low_c', 'TMIN'), ('precipitation_mm', 'PRCP')]:
            assert float(row[csv_key]) == city[json_key][i], (city['city'], i, csv_key)
        rain_days = city['DP01'][i]
        if rain_days is not None:
            assert float(row['rain_days_ge_1mm']) == rain_days
        else:
            assert row['rain_days_ge_1mm'] == ''
        assert row['source_family'] == ('IPMA' if city['country'] == 'Portugal' else 'WMO_NCEI_min24')
print('PASS: 90 cities, 23 countries, 1080 monthly rows; CSV and JSON agree.')
for c in cities:
    assert c['supplement_period'] == '1991-2020'
    assert -90 <= c['latitude'] <= 90 and -180 <= c['longitude'] <= 180
    for field, maximum in [('RH2M', 100), ('WS10M', 100)]:
        assert len(c[field]) == 12
        assert all(v is None or 0 <= v <= maximum for v in c[field])
    matches = [r for r in rows if r['country'] == c['country'] and r['city'] == c['city']]
    for i, row in enumerate(matches):
        for field, key in [('RH2M','relative_humidity_2m_pct_model'),('WS10M','mean_wind_10m_m_s_model')]:
            assert (row[key] == '' if c[field][i] is None else float(row[key]) == c[field][i])
        assert row['supplement_source'] == c['supplement_source']
        assert row['supplement_period'] == c['supplement_period']
mysuru = next(c for c in cities if c['city'] == 'Mysuru')
assert mysuru['geocoded_name'] == 'Mysuru' and mysuru['longitude'] < 77
print('PASS: model wind/humidity and city anchors; supplemental CSV/JSON fields agree.')
