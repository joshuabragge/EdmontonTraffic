import datetime
import os
import time
import requests

if __name__ == '__main__':
	name = 'edmonton_traffic_incident_data' + datetime.datetime.today().strftime('%Y%m%d_%H%M') + '.csv'
	path = os.path.join('traffic_incident_data', name)
	r = requests.get('https://data.edmonton.ca/resource/87ck-293k.csv', stream=True)
	if r.status_code == 200:
		print("Writing to file", name)
		with open(path, 'wb') as f:
			for chunk in r:
				f.write(chunk)
		f.close()
	print("Sleeping for 12 hours")
	time.sleep(43200)