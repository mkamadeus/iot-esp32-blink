import network

# constants
WLAN_SSID = "xxx"
WLAN_PASS = "xxx"

sta_if = network.WLAN(network.STA_IF)

if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect(WLAN_SSID, WLAN_PASS)
    while not sta_if.isconnected():
        pass
    
    print('connected to %s' % (WLAN_SSID))
    print('network config:', sta_if.ifconfig())
    

