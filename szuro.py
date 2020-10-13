#!/usr/bin/env python3

import frida
import sys

logo = print("""
____ ___  _  _ ____ ____ 
[__    /  |  | |__/ |  | 
___]  /__ |__| |  \ |__| 

                    ~0xbiel
""")

if sys.argv[1] == 'help' or sys.argv[1] == '-h' or sys.argv[1] == '--help': 
    logo
    print("Usage: szuro [package id] [what you want to filter].\n")


appid = sys.argv[1]
mf = sys.argv[2]
    
print("\n")

session = frida.get_usb_device().attach(appid)

android_view_methods = []

source = """
Java.perform(function () {
    var v = Java.use("android.view.View");
    var m = v.class.getMethods();
    for(var i = 0; i < m.length; i++) {
        send(m[i].toString());
    }
});
"""

script = session.create_script(source)

def on_message(message, data):
    if mf in message['payload']: #replace "Text" with what you want to filter
        android_view_methods.append(message['payload'])

script.on('message', on_message)

script.load()

for method in android_view_methods:
    print(method)

session.detach()

