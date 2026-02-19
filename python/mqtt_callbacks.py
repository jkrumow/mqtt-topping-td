def onConnect(_):
    op.MqttTopping.OnConnect()


def onConnectFailure(_, msg: str):
    op.MqttTopping.OnConnectionFailure(msg)


def onConnectionLost(_, msg: str):
    op.MqttTopping.OnConnectionLost(msg)


def onSubscribe(_):
    op.MqttTopping.OnSubscribe()


def onSubscribeFailure(_, msg: str):
    op.MqttTopping.OnSubscribeFailure(msg)
    return


def onUnsubscribe(_):
    op.MqttTopping.OnUnsubscribe()


def onUnsubscribeFailure(_, msg: str):
    op.MqttTopping.OnUnsubscribeFailure(msg)


def onPublish(_, topic: str):
    op.MqttTopping.OnPublish(topic)


def onMessage(_, topic: str, payload: str, __, ___, ____):
    op.MqttTopping.OnMessage(topic, payload)
