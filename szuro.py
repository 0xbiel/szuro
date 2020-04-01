import frida

session = frida.get_usb_device().attach('org.mozilla.firefox')  #replace with the app you are hacking.

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
    if "Text" in message['payload']: #replace "Text" with what you want to filter
        android_view_methods.append(message['payload'])

script.on('message', on_message)

script.load()

for method in android_view_methods:
    print(method)

session.detach()
