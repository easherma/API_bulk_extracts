from factual import Factual
import json
# getting paramaters 
key = 'SEQDH9X3sOycBDUzKubGqgzFVOybhdHPgAJrYggu'
scrt = 'mwjLAzVZsaPOwavzkXBeu44B1VEYNAfRGczh3wow'
factual = Factual(key, scrt)
# api call, currently hard coded
places = factual.table('places')
data = places.filters({'$and':[{'category_ids':{'$includes':185}},{'locality':{'$eq':'chicago'}}]}).data()
# parse returned data
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)