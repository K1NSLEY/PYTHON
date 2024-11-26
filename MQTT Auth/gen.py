import paho.mqtt.client as mqtt

# Configurações do broker MQTT
BROKER = "broker.hivemq.com"  # Endereço do broker
PORT = 1883  # Porta padrão
TOPIC_SUBSCRIBE = "PontoNet/AutoFiller/Auth"  # Tópico para escutar
TOPIC_PUBLISH = "PontoNet/AutoFiller/Post"  # Tópico para publicar
CLIENT_ID = "d21439d3-919e-43bd-a938-bff79da815fa"  # ID único do cliente

# Callback para quando o cliente se conecta ao broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao broker com sucesso!")
        client.subscribe(TOPIC_SUBSCRIBE)  # Inscreve-se no tópico
    else:
        print(f"Falha na conexão. Código de retorno: {rc}")

# Callback para quando uma mensagem é recebida
def on_message(client, userdata, msg):
    mensagem = msg.payload.decode()
    print(f"Mensagem recebida no tópico {msg.topic}: {mensagem}")
    if mensagem == "Auth":
        client.publish(TOPIC_PUBLISH, "Approve")
        print("Mensagem 'Approve' enviada!")

        ##fazer um liga e desliga por outro mqtt

# Configuração do cliente MQTT
client = mqtt.Client(client_id=CLIENT_ID, userdata=None, protocol=mqtt.MQTTv311)
client.on_connect = on_connect
client.on_message = on_message

try:
    # Conexão ao broker
    client.connect(BROKER, PORT)
    print("Tentando conectar ao broker...")

    # Loop para manter a conexão ativa e processar mensagens
    client.loop_forever()
except Exception as e:
    print(f"Erro: {e}")
