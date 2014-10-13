#Snapception

Intercept and decrypt all snapchats received over your network

## Quickstart
Installing is easy: 
```
pip install snapception 
```

Starting it is easy too: 
```
snapception --help
Usage: snapception [OPTIONS]

Options:
  -v, --verbose        Enable logging
  -vv, --very-verbose  Include mitmdump in logging
  -o, --output TEXT    Specify output directory (Default is ~/snaps)
  --help               Show this message and exit.
```

Configuring it is also pretty easy:

1. Configure your device to use a proxy pointing to Port 8080 of the host computer
2. Install a CA on your device by visiting mitm.it once connected to the proxy
3. Watch all the Snapchats you receive over the network become available on your computer

## Isn't this just SnapSave/SnapBox/SnapSomething?
Nope. Those require you to authenticate with Snapchat's backend by giving the third party your username and password. Snapception, on the other hand, intercepts *all* snapchats received over the network so long as the receiving device is connected to the computer running Snapception via a proxy. Those applications also require you to manually login and save your snapchat before officially opening it; Snapception automatically intercepts, decrypts, and saves your received snaps.

## What's your aim? Privacy invasion? World domination? 
Nope. I just created this to call attention to a security vulnerability that's been present in Snapchat for over a year. Did you know they use *one*, *hardcoded* key for *all* video and image encryption? 

Anyway, for Snapception to intercept your snapchats, you must be connected to the computer via a proxy and have installed its CA, so someone can't just intercept your snapchats if you merely are using their network.

## What's the technology stack behind Snapception?
Glad you asked! The core of my script is basically a glorified event handler built on top of [mitmdump](https://github.com/mitmproxy/mitmproxy), a highly extensible and easily scriptable man-in-the-middle proxy. Besides the event handler I built a basic command line interface using [click](https://github.com/mitsuhiko/click), which both launched mitmdump and glued together its custom event handler.

I would not have been able to build Snapception without the decryption ruby script by [AJ Jenkins](https://github.com/ajenkins/comp116-ajenkins/tree/master/final_project), who in turn based it upon the code written by [Amelia Cuss](https://kivikakk.ee/2013/05/10/snapchat.html). My code expands upon theirs in that in automatically intercepts the encrypted snapchats before decrypting them whereas before the encrypted snapchats would have to manually be obtained some other way.

## Can I contribute?
Please! Feel free to submit any pull requests. I whipped this application up in less than a day, so there is bound to be some bugs, missing features, or hastily written code.
