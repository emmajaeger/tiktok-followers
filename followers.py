import requests
import numpy as np
import math
import csv  

follower_count = 200 # TODO: your follower count here
max_cursors = ["0"]

for i in range(math.ceil(follower_count / 200)):
	print(str(i * 200) + " - " + str((i * 200) + 200))
	print("------------")
	url = "https://tiktok.p.rapidapi.com/live/user/follower/list"

	querystring = {"username":"TODO: your username here","max_cursor":max_cursors[i],"limit":"200"}

	headers = {
		# use the following link to sign up for an account + get your rapidapi key
		# https://rapidapi.com/logicbuilder/api/tiktok?endpoint=apiendpoint_22845da6-6ef6-480e-862e-63fbb6b2c226
	    'x-rapidapi-key': "TODO: your rapidapi key here",
	    'x-rapidapi-host': "tiktok.p.rapidapi.com"
	}

	# .json converts to a dictionary
	response = requests.request("GET", url, headers=headers, params=querystring).json()
	print("REQUEST " + str(i) + " MADE")
	print("------------")
	max_cursors.append(response.get("max_cursor"))

	# TODO: change this filename if desired
	with open(r'followers.csv', 'a') as f:
	    writer = csv.DictWriter(f, response.get("followers")[0].keys())
	    if i == 0:
	    	writer.writeheader()
	    for follower in response.get("followers"):
	    	writer.writerow(follower)