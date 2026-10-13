"""Rebuild geographic anchors and NASA POWER supplement from explicit source queries.
No secrets or keys. Run: python3 enrich.py. Review coordinate matches before publishing.
"""
import json,urllib.request,urllib.parse,concurrent.futures,hashlib,pathlib,time
root=pathlib.Path(__file__).resolve().parent
cities=json.loads((root/'cities.json').read_text())
codes=dict(zip(['Spain','United States','Australia','New Zealand','South Africa','Colombia','Mexico','Chile','Morocco','France','Italy','Cyprus','India','China','Japan','Brazil','Argentina','Turkiye','United Kingdom','Rwanda','Tunisia','Uruguay','Portugal'],['ES','US','AU','NZ','ZA','CO','MX','CL','MA','FR','IT','CY','IN','CN','JP','BR','AR','TR','GB','RW','TN','UY','PT']))
alias={1:'Las Palmas de Gran Canaria',24:'Port Elizabeth',31:'Mexico City',34:'Viña del Mar',51:'Nicosia',52:'Bengaluru',53:'Mysuru',42:'Marrakesh',79:'Gisenyi'}
months=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
cache=root/'source-cache';cache.mkdir(exist_ok=True)
def fetch(url,path):
 if path.exists():return json.loads(path.read_text())
 with urllib.request.urlopen(url,timeout=30) as r:data=r.read()
 path.write_bytes(data);return json.loads(data)
def one(c):
 name=alias.get(c['number'],c['city'].split(' (')[0]);url='https://geocoding-api.open-meteo.com/v1/search?'+urllib.parse.urlencode(dict(name=name,count=10,countryCode=codes[c['country']],language='en',format='json'))
 try:
  g=fetch(url,cache/f"geo-{c['number']}.json")
  hits=[v for v in g.get('results',[]) if v.get('country_code')==codes[c['country']] and v.get('feature_code','').startswith('PPL')]
  if not hits: raise ValueError('No settled-place match')
  hit=max(hits,key=lambda v:v.get('population',0));c['latitude']=hit['latitude'];c['longitude']=hit['longitude'];c['coordinate_source']=url;c['geocoded_name']=hit['name'];c['coordinate_note']='City anchor from GeoNames via Open-Meteo, not the temperature/rain station location.'
  purl='https://power.larc.nasa.gov/api/temporal/climatology/point?'+urllib.parse.urlencode(dict(parameters='RH2M,WS10M',community='RE',longitude=c['longitude'],latitude=c['latitude'],start=1991,end=2020,format='JSON'))
  p=fetch(purl,cache/f"power-{c['number']}.json")
  assert 'January 1991 - December 2020' in p['header']['range']
  assert p['parameters']['RH2M']['units']=='%' and p['parameters']['WS10M']['units']=='m/s'
  fill=p['header']['fill_value']; c['RH2M']=[None if p['properties']['parameter']['RH2M'].get(m,fill)==fill else p['properties']['parameter']['RH2M'][m] for m in months];c['WS10M']=[None if p['properties']['parameter']['WS10M'].get(m,fill)==fill else p['properties']['parameter']['WS10M'][m] for m in months]
  c['supplement_source']=purl;c['supplement_period']='1991-2020';c['supplement_type']='NASA POWER / MERRA-2 model-derived grid climatology, not station observations';c['supplement_sha256']=hashlib.sha256((cache/f"power-{c['number']}.json").read_bytes()).hexdigest()
  print(c['number'],c['city'],'=>',hit['name'],hit.get('admin1'),c['latitude'],c['longitude'],flush=True)
 except Exception as e:
  c['RH2M']=[None]*12;c['WS10M']=[None]*12;c['supplement_gap']=str(e);print('GAP',c['city'],str(e),flush=True)
 return c
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: results=list(ex.map(one,cities))
(root/'cities.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
