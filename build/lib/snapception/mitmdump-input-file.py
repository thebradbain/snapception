import os
import uuid
import requests
from subprocess import call

home = os.path.expanduser('~')
conf = {}

def request(context, flow):
	request = flow.request
	if(request.host == "feelinsonice-hrd.appspot.com" and request.path == '/bq/blob'):
		blobURI = "http://"+request.host+request.path+"?"+request.content
		print "Downloading intercepted blob ("+blobURI+")"
		r = requests.get(blobURI)

		print "Downloaded blob"
		b = open(home+'/snaps/blob', 'w+')
		print >> b, r.content

		print "Decrypting file..."
		blobFile = home+'/snaps/blob'
		outputFile = home+"/snaps/snap_"+str(uuid.uuid4())
		rubyFile = '/Users/bradbain/snapception/ENV/lib/python2.7/site-packages/snapception-0.1-py2.7.egg/snapception/decrypt_snap.rb'

		call(['ruby', rubyFile, blobFile, outputFile])

		print "File decrypted! Your picture is now available."
		print "---- Waiting for a Snapchat... ----"

def start(context, argv):
	print "---- Waiting for a Snapchat... ----"