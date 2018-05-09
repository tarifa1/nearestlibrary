# nearestlibrary
Interact with Data at City of Chicago API to pull closest Chicago Public Library locations to input coordinates


Welcome to documentation on nearest_chicago_library.py, a small python script that interacts with the Chicago Public Library systems data by querying their API and pulling data regarding the closest libraray to a set of input coordinates (given in the form of longitude and latitude).

1) This script does not leverage any python modules not included in the standard Python library, therefore the requirements.txt are empty.

2) To run the script, simply clone a copy of the repo to your local disc, or download the files from Github. Navigate to the directory where the files are stored and the app can be kicked off by the following command:

	python nearest_chicago_library.py 11 35 WED 12:30

The inputs are as follows:

	-latitude
	-longitude
	-day (3 letter representation)
	-time of day (24 hour format)	

Sample input and output: 

	USWAL811733:nearestlibrary ahmedt$ python nearest_chicago_library.py 11 35 WED 12:30pm
	The latitude of your entry is 11 and the longitude is 35. You want to know the 5 nearest libraries to 11,35 on WED at 12:30pm.
		1)
		Library Name: Clearing
		Address: 6423 W. 63rd Place CHICAGO IL 60638
		Popularity: 
			Visitors Per Year: N/A
			City of Chicago Avg: 25440.341772151899 
		Hours of Operation: M, W: 12PM-8PM; TU, TH: 10AM-6PM; F, SA: 9AM-5PM; SU: Closed
		
		2)
		Library Name: Mount Greenwood
		Address: 11010 S. Kedzie Avenue CHICAGO IL 60655
		Popularity: 
			Visitors Per Year: N/A
			City of Chicago Avg: 25440.341772151899 
		Hours of Operation: M, W: 10AM-6PM;  TU, TH: 12PM-8PM; F, SA: 9AM-5PM; SU: Closed
		
		3)
		Library Name: Garfield Ridge
		Address: 6348 S. Archer Avenue CHICAGO IL 60638
		Popularity: 
			Visitors Per Year: N/A
			City of Chicago Avg: 25440.341772151899 
		Hours of Operation: M, W: 10AM-6PM;  TU, TH: 12PM-8PM; F, SA: 9AM-5PM; SU: Closed
		
		4)
		Library Name: Scottsdale
		Address: 4101 W. 79th Street CHICAGO IL 60652
		Popularity: 
			Visitors Per Year: N/A
			City of Chicago Avg: 25440.341772151899 
		Hours of Operation: M, W: 10AM-6PM;  TU, TH: 12PM-8PM; F, SA: 9AM-5PM; SU: Closed
		
		5)
		Library Name: Walker
		Address: 11071 S. Hoyne Avenue CHICAGO IL 60643
		Popularity: 
			Visitors Per Year: N/A
			City of Chicago Avg: 25440.341772151899 
		Hours of Operation: M, W: 10AM-6PM;  TU, TH: 12PM-8PM; F, SA: 9AM-5PM; SU: Closed
		
		USWAL811733:nearestlibrary ahmedt$		
