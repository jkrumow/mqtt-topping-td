# TouchDesigner MQTT Topping Component

TD Component to use the Python library `mqtt_topping`.

## Requirements

- Touchdesigner  >= 2023.12370
- Python 3.11

## Installation

Copy this directory into the "external" folder on the base directory of your project:

```sh
./external/mqtt-topping
```

Load the tox into your project:

1. drag into your project
2. Common -> Enable External .tox = ON
3. Common -> External .tox Path = set to tox file
4. Common -> Reload custom parameters = OFF

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
