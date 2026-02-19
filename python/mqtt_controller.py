import logging
import platform
import uuid

from mqtt_topping import MqttTopping, TouchDesignerClientAdaptor


class MqttController:
    def __init__(self, ownerComp):
        self._logger = logging.getLogger(self.__class__.__name__)
        self._owner_comp = ownerComp
        self._mqtt_topping = None
        self._client_adaptor = None
        self._logger.info("init")

        self._is_initial_connect = True

        self._build_topping()
        self._activate_client()

    # def onInitTD(self):
    #     self._logger.info("startup")
    #     client = self._owner_comp.op('mqttclient')
    #     self._client_adaptor = TouchDesignerClientAdaptor(client)
    #     self._mqtt_topping = MqttTopping(self._client_adaptor)

    def _build_topping(self):
        client = self._owner_comp.op('mqttclient')
        self._client_adaptor = TouchDesignerClientAdaptor(client)
        self._mqtt_topping = MqttTopping(self._client_adaptor)

    def _activate_client(self):
        self._logger.info("activate")
        self.CreateClientId()
        self._owner_comp.op('mqttclient').par.active = True

    def CreateClientId(self):
        app_id = self._owner_comp.op('app_id')[0, 0]
        hostname = platform.node()
        random_uuid = uuid.uuid4()
        short_uuid = str(random_uuid)[-8:]
        op('mqtt_client_id')[0, 0] = f"{app_id}-{hostname}-{short_uuid}"

    def OnConnect(self):
        self._logger.info("connected")
        if not self._is_initial_connect:
            self._logger.info("internal reconnect")
            self._mqtt_topping.refresh_subscriptions()
        else:
            self._owner_comp.DoCallback('onConnect')
        self._is_initial_connect = False

    def OnConnectionFailure(self, error):
        self._logger.error("connection failure %s", error)
        info = {'error': error}
        self._owner_comp.DoCallback('onConnectFailure', info)

    def OnConnectionLost(self, error):
        self._logger.error("connection lost %s", error)
        info = {'error': error}
        self._owner_comp.DoCallback('onConnectionLost', info)

        # how do we proceed from here?
        # √ reconnect caused by network error: keep session and subscriptions alive
        # √ reconnect caused by app crash: fresh session and subscriptions
        # √ -> reconnect + refresh subscriptions for EXISTING callbacks

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


#####################


    def OnMessage(self, topic: str, payload: any):
        self._client_adaptor.on_message(topic, payload)

    def Subscribe(self, topic: str, callback: any):
        self._mqtt_topping.subscribe(topic, callback)

    def Unsubscribe(self, topic: str, callback: any):
        self._mqtt_topping.subscribe(topic, callback)

    def Publish(self, topic: str, payload: any):
        self._mqtt_topping.publish(topic, payload)
