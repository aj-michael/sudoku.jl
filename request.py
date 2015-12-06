import requests

hostname = 'localhost:8001'
puzzle = '340590820700060005050082607020000040030806070090000060403250010200070004075034086'
response = requests.get('http://'+hostname+'/solve/'+puzzle)
print response.text
