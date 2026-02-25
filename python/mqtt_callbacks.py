def onConnect(_):
    parent.MqttTopping.OnConnect()


def onConnectFailure(_, msg: str):
    parent.MqttTopping.OnConnectionFailure(msg)


def onConnectionLost(_, msg: str):
    parent.MqttTopping.OnConnectionLost(msg)


def onSubscribe(_):
    parent.MqttTopping.OnSubscribe()


def onSubscribeFailure(_, msg: str):
    parent.MqttTopping.OnSubscribeFailure(msg)
    return


def onUnsubscribe(_):
    parent.MqttTopping.OnUnsubscribe()


def onUnsubscribeFailure(_, msg: str):
    parent.MqttTopping.OnUnsubscribeFailure(msg)


def onPublish(_, topic: str):
    parent.MqttTopping.OnPublish(topic)


def onMessage(_, topic: str, payload: str, __, ___, ____):
    parent.MqttTopping.OnMessage(topic, payload)
