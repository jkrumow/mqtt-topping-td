import logging

from mqtt_topping import MqttTopping, TouchDesignerClientAdaptor


class MqttController:
    def __init__(self, ownerComp):
        self._logger = logging.getLogger(self.__class__.__name__)
        self._owner_comp = ownerComp
        self._mqtt_topping = None
        self._client_adaptor = None

    def onInitTD(self):
        self._logger.info("startup")
        client = self._owner_comp.op('mqttclient')
        self._client_adaptor = TouchDesignerClientAdaptor(client)
        self._mqtt_topping = MqttTopping(self._client_adaptor)

    def ActivateClient(self):
        self._logger.info("activate")
        self._owner_comp.op('mqttclient').par.active = True
        self._owner_comp.op('mqttclient').par.reconnect.pulse()

    def DeactivateClient(self):
        self._logger.info("deactivate")
        self._owner_comp.op('mqttclient').par.active = False

    def OnConnect(self):
        self._logger.info("connect")
        self._owner_comp.DoCallback('onConnect')

    def OnConnectionFailure(self, error):
        self._logger.error("connection failure %s", error)
        info = {'error': error}
        self._owner_comp.DoCallback('onConnectFailure', info)

    def OnConnectionLost(self, error):
        self._logger.error("connection lost %s", error)
        info = {'error': error}
        self._owner_comp.DoCallback('onConnectionLost', info)

    def OnMessage(self, topic: str, payload: any):
        self._client_adaptor.on_message(topic, payload)

    def Subscribe(self, topic: str, callback: any):
        self._mqtt_topping.subscribe(topic, callback)

    def Unsubscribe(self, topic: str, callback: any):
        self._mqtt_topping.subscribe(topic, callback)

    def Publish(self, topic: str, payload: any):
        self._mqtt_topping.publish(topic, payload)
