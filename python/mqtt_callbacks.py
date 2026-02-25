def onConnect(_):
    parent().OnConnect()


def onConnectFailure(_, msg: str):
    parent().OnConnectionFailure(msg)


def onConnectionLost(_, msg: str):
    parent().OnConnectionLost(msg)


def onSubscribe(_):
    parent().OnSubscribe()


def onSubscribeFailure(_, msg: str):
    parent().OnSubscribeFailure(msg)


def onUnsubscribe(_):
    parent().OnUnsubscribe()


def onUnsubscribeFailure(_, msg: str):
    parent().OnUnsubscribeFailure(msg)


def onPublish(_, topic: str):
    parent().OnPublish(topic)


def onMessage(_, topic: str, payload: str, __, ___, ____):
    parent().OnMessage(topic, payload)
