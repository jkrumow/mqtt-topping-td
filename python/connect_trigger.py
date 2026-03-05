def onPulse(_):
    if op('mqttclient').par.active is True:
        op('mqttclient').par.reconnect.pulse()
    else:
        op('mqttclient').par.active = True
