import frida

print("""
____ ___  _  _ ____ ____ 
[__    /  |  | |__/ |  | 
___]  /__ |__| |  \ |__| 
                                 
""")

appid = input("Package ID: ")

mf = input("What do you want to filter? ")

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

