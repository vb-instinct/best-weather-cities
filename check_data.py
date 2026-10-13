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
            assert row['rain_days_ge_1mm'] == 'None'
        assert row['source_family'] == ('IPMA' if city['country'] == 'Portugal' else 'WMO_NCEI_min24')
print('PASS: 90 cities, 23 countries, 1080 monthly rows; CSV and JSON agree.')
