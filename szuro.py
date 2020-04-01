import frida

session = frida.get_usb_device().attach('org.mozilla.firefox') #replace with the app you are hacking.

android_view_methods[] #store methods in an array

source = """

Java.perform(function() {
    var v = Java.use("android.view.View");
    var m = v.class.getMethods();
    for var i = 0; i < m.length; i++) {
        send(m[i].toString());
    }
});

"""
