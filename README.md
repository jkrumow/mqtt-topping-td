# TouchDesigner MQTT Topping Component

TD Component to use the Python library `mqtt_topping-py`.

## Requirements

- Touchdesigner  >= 2025
- Python 3.11

## Installation

Add this dependency to your `requirements.txt`:

```sh
mqtt-topping-td @ git+https://github.com/artcom/mqtt-topping-td.git@0.1.1#egg=mqtt-topping-td
```

Load the tox into your project:

1. create a baseCOMP
2. Common -> External .tox Path = `mod.mqtt_topping_td.ToxFile`
3. Common -> Enable External .tox = ON
4. Common -> Reload custom parameters = OFF

## Usage

Parameters on page "Mqtt":

| Parameter      | Description                                                 |
| :------------- | :---------------------------------------------------------- |
| `Active`       | Enable / disable MQTT connection                            |
| `AppId`        | App id used for client id                                   |
| `TcpBrokerUri` | Broker uri for TCP connection                               |
| `MaxInFLight`  | Max count of messages which can be processed simultaniously |
| `Username`     | Username for client                                         |
| `Password`     | Password for client                                         |
| `Reconnect`    | Manual trigger for reconnect                                |

## Usage

The mqtt-topping can be accessed by the Extension `MqttTopping`:

```py
def cb_my_callback(topic, payload):
    # code here

op.MqttTopping.Subscribe("test/hello", cb_my_callback)
```

Callbacks will inform over status and are identical to callbacks for mqttclient:

[https://derivative.ca/UserGuide/MqttclientDAT_Class](https://derivative.ca/UserGuide/MqttclientDAT_Class)
