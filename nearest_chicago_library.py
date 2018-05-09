import json
import requests
import sys

# Collect input arguments ; output as statement for both readability and debugging purposes 
latitude = sys.argv[1]
longitude = sys.argv[2]
day = sys.argv[3]
time = sys.argv[4]


print("""
	The latitude of your entry is {0} and the longitude is {1}. You want to know the 5 nearest libraries to {0},{1} on {2} at {3}.""".format(latitude,longitude,day,time))

# Connect to Data at City of Chicago API and query their data and convert response into python dictionary (#21)
url_request = "https://data.cityofchicago.org/resource/psqp-6rmg.json?&$order=distance_in_meters(location, 'POINT ({1} {0})') DESC &$limit=5&$select=*, distance_in_meters(location, 'POINT ({1} {0})') AS range &$$app_token=fevN3wRxa84iW0hOhExU6BLa7&".format(longitude,latitude)

response = requests.get(url_request)
chicago_library_dataset = json.loads(response.text)

# Calculate average library visitations for the whole city (part of metric to determine popularity)
visitors_avg_url = "https://data.cityofchicago.org/resource/bbyd-w2e7.json?$select=avg(ytd)&$$app_token=fevN3wRxa84iW0hOhExU6BLa7&"

visitors_avg = requests.get(visitors_avg_url)
average_visitors = json.loads(visitors_avg.text)
avg_visitors = average_visitors[0]['avg_ytd']

# For all entries in the return data, assign values to variables
range_len = len(chicago_library_dataset)
for i in range(0, range_len):
	# print(chicago_library_dataset[i])
	hours_of_operation = (chicago_library_dataset[i]["hours_of_operation"])
	library_name = (chicago_library_dataset[i]["name_"])
	address = (chicago_library_dataset[i]["address"])
	city = (chicago_library_dataset[i]["city"])
	state = (chicago_library_dataset[i]["state"])
	zip_code = (chicago_library_dataset[i]["zip"])
	location = (chicago_library_dataset[i]["location"]["coordinates"])
	
	''' Attempt to query Chicago Library data to determine yearly visits per site. As of writing this comment, this particular query returns empty data in a list [] instead of the actual value - this would be an area we need to revisit on a second pass through the code. Empty data causes an IndexError, hence the exception handling (# 52) which assigns a generic 'N/A' string to those entries'''

	visitors_url_request = "https://data.cityofchicago.org/resource/bbyd-w2e7.json?$$app_token=fevN3wRxa84iW0hOhExU6BLa7&location={}".format(library_name)

	visitors_response = requests.get(visitors_url_request)
	chicago_library_visitors = json.loads(visitors_response.text)

	try:
		site_yearly_visitors =(chicago_library_visitors[0]['ytd'])
	except IndexError as error:
		site_yearly_visitors = 'N/A'

	print("""
		{})
		Library Name: {}
		Address: {} {} {} {}
		Popularity: 
			Visitors Per Year: {}
			City of Chicago Avg: {} 
		Hours of Operation: {}
		""".format((i+1),library_name,address,city,state,zip_code,site_yearly_visitors,avg_visitors,hours_of_operation))