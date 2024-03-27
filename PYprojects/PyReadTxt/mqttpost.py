from paho.mqtt import client as mqtt_client
import random

broker = 'mqtt-dashboard.com'
port = 1883
topic = "oi15"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = ''
password = ''

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    # Set Username and Password
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client
import paho.mqtt.client as mqtt

# Configurações do broker
broker_host = "mqtt-dashboard.com"
broker_port = 1883

# Cria o cliente MQTT
client = mqtt.Client()

# Conecta-se ao broker
client.connect(broker_host, broker_port)

# Publica uma mensagem
client.publish("oi/oi", "Hello, world!")

# Desconecta-se do broker
client.disconnect()
