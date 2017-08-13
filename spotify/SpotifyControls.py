import requests
import json

def getCredentials():
	f = open("auth.txt", "r")
	header = json.loads({"Authorization":"Bearer {}".format(f.readline())}) 
	url = f.readline()
	f.close()
	return header, url

def pause():
	header, url = getCredentials()
	response = requests.put(url + "/me/player/pause", headers = header)
 
def play():
	header, url = getCredentials()
	response = requests.put(url + "/me/player/play", headers = header)
#r = json.loads(response.text)

def skip():
	header, url = getCredentials()
	response = requests.post(url + "/me/player/next", headers = header)

def back():
	header, url = getCredentials()
	response = requests.post(url + "/me/player/previous", headers = header)


def setVolume(volume):
	header, url = getCredentials()
	response = requests.post(url + "/me/player/volume?volume_percent=" + str(vol), headers = header)

