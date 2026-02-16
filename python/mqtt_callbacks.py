def onConnect(_):
    op.MqttTopping.OnConnect()


def onConnectFailure(_, msg: str):
    op.MqttTopping.OnConnectionFailure(msg)


def onConnectionLost(_, msg: str):
    op.MqttTopping.OnConnectionLost(msg)


def onSubscribeFailure(_, __):
    return


def onUnsubscribeFailure(_, __):
    return


def onMessage(_, topic: str, payload: str, __, ___, ____):
    op.MqttTopping.OnMessage(topic, payload)
