import requests
import json
import base64

def GetCredentials():
	f = open("auth.txt", "r")
	#print f.readline()
	header = f.readline()
	url = f.readline()
	f.close()
	#print url
	return (header, url)

def Pause():
	header = {"Authorization":"Bearer {}".format(str(GetCredentials()[0][:-1]))}
	url = str(GetCredentials()[1])
	response = requests.put(url + "/me/player/pause", headers = header)
	print response.text
 
def Play():
	header = {"Authorization":"Bearer {}".format(str(GetCredentials()[0][:-1]))}
	url = str(GetCredentials()[1])
	response = requests.put(url + "/me/player/play", headers = header)
#r = json.loads(response.text)

def Skip():
	header = {"Authorization":"Bearer {}".format(str(GetCredentials()[0][:-1]))}
	url = str(GetCredentials()[1])
	response = requests.post(url + "/me/player/next", headers = header)

def Back():
	header = {"Authorization":"Bearer {}".format(str(GetCredentials()[0][:-1]))}
	url = str(GetCredentials()[1])
	response = requests.post(url + "/me/player/previous", headers = header)


def SetVolume(volume):
	header = {"Authorization":"Bearer {}".format(str(GetCredentials()[0][:-1]))}
	url = str(GetCredentials()[1])
	response = requests.post(url + "/me/player/volume?volume_percent=" + str(vol), headers = header)
