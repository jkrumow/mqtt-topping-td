import logging
import platform
import uuid

from mqtt_topping import MqttTopping, TouchDesignerClientAdaptor


class MqttController:
    def __init__(self, ownerComp):
        self._logger = logging.getLogger(self.__class__.__name__)
        self._logger.info("init")

        self._owner_comp = ownerComp
        self._is_initial_connect = True

        client = self._owner_comp.op('mqttclient')
        self._client_adaptor = TouchDesignerClientAdaptor(client)
        self._mqtt_topping = MqttTopping(self._client_adaptor)

    def ActivateClient(self):
        self._logger.info("activate")
        self.CreateClientId()
        self._owner_comp.op('mqttclient').par.active = True

    def DeactivateClient(self):
        self._logger.info("deactivate")
        self._owner_comp.op('mqttclient').par.active = False

    def CreateClientId(self):
        app_id = self._owner_comp.op('app_id')[0, 0]
        hostname = platform.node()
        random_uuid = uuid.uuid4()
        short_uuid = str(random_uuid)[-8:]
        op('mqtt_client_id')[0, 0] = f"{app_id}-{hostname}-{short_uuid}"

    # ------------ MQTT client callbacks ------------

    def OnConnect(self):
        self._logger.info("connected")
        if self._is_initial_connect:
            self._logger.info("first connect")
            self._owner_comp.DoCallback('onConnect')
        else:
            self._logger.info("internal reconnect")
            self._mqtt_topping.refresh_subscriptions()
            self._owner_comp.DoCallback('onReconnect')
        self._is_initial_connect = False

    def OnConnectionFailure(self, error):
        self._logger.error("connection failure %s", error)
        info = {'error': error}
        self._owner_comp.DoCallback('onConnectFailure', info)

    def OnConnectionLost(self, error):
        self._logger.error("connection lost %s", error)
        info = {'error': error}
        self._owner_comp.DoCallback('onConnectionLost', info)

    def OnSubscribe(self):
        self._owner_comp.DoCallback('onSubscribe')

    def OnSubscribeFailure(self, error):
        info = {'error': error}
        self._owner_comp.DoCallback('onSubscribeFailure', info)

    def OnUnsubscribe(self):
        self._owner_comp.DoCallback('onUnsubscribe')

    def OnUnsubscribeFailure(self, error):
        info = {'error': error}
        self._owner_comp.DoCallback('onUnsubscribeFailure', info)

    def OnPublish(self, topic):
        info = {'topic': topic}
        self._owner_comp.DoCallback('onPublish', info)

    # ------------ MQTT Topping Methods ------------

    def Subscribe(self, topic: str, callback: any):
        self._mqtt_topping.subscribe(topic, callback)

    def Unsubscribe(self, topic: str, callback: any):
        self._mqtt_topping.subscribe(topic, callback)

    def Publish(self, topic: str, payload: any):
        self._mqtt_topping.publish(topic, payload)

    def OnMessage(self, topic: str, payload: any):
        self._client_adaptor.on_message(topic, payload)
