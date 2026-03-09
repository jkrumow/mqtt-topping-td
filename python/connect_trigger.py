def onPulse(_):

    if op('mqttclient').par.active is True:
        parent().ReactivateClient()
    else:
        parent().ActivateClient()
