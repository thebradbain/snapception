import os
import sys
import uuid
import requests
from subprocess import call

conf = {
	'quiet' : True,
	'snapsDir' : '~/snaps/',
	'pyDir' : ''
}

def request(context, flow):
	request = flow.request
	if(request.host == "feelinsonice-hrd.appspot.com" and request.path == '/bq/blob'):
		blobURI = "http://"+request.host+request.path+"?"+request.content
		log("Downloading intercepted blob ("+blobURI+")")
		r = requests.get(blobURI)

		log("Downloaded blob")
		blobFile = './blob'
		b = open(blobFile, 'w+')
		print >> b, r.content

		log("Decrypting file...")
		if(not os.path.exists(os.path.expanduser(conf['snapsDir']))):
			os.makedirs(os.path.expanduser(conf['snapsDir']))
		outputFile = os.path.expanduser(conf['snapsDir']) + 'snap_%s' % str(uuid.uuid4())
		rubyFile = conf['pyDir']+'/decrypt_snap.rb'

		call(['ruby', rubyFile, blobFile, outputFile])

		log("File decrypted! Your picture is now available.")
		log("---- Waiting for a Snapchat... ----")

def start(context, argv):
	conf['pyDir'] = os.path.dirname(argv[0])
	args = argv[1].split()
	if('--verbose' in args):
		conf['quiet'] = False
		args.remove('--verbose')
	if(args[0]):
		snapsDir = args[0]
		if(not snapsDir[-1:] == '/'):
			snapsDir = snapsDir+'/' 
		conf['snapsDir'] = snapsDir

	print 'Snapception is now running on Port 8080. Configure your device to point to this port via a proxy.'
	print 'If you have not already done so, you will need to install a Certificate Authority. The easiest way to do this is to visit mitm.it on your device.'
	log("---- Waiting for a Snapchat... ----")

def log(str):
	if(not conf['quiet']):
		print str