from kafka import KafkaProducer # Para enviar mensagens ao Kafka
from faker import Faker # Gerar dados fictícios (datas/horas)
import time
import json
import random
# Funções básicas de tempo, JSON e aleatoriedade

# Initialize Faker and KafkaProducer
fake = Faker()
producer = KafkaProducer(
    bootstrap_servers='kafka:9092', # Endereço do servidor Kafka
    api_version=(3, 8, 0), # Versão compatível com o servidor
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),  # Converte valores para JSON
    key_serializer=lambda k: k.encode('utf-8') # Converte chaves para texto
)

def generate_temperature_data():
    return {
        'sensor_id': str(random.randint(1, 50)),  # ID aleatório entre 1-50
        'temperature': round(random.uniform(-10.0, 40.0), 2),  # Temperatura entre -10°C e 40°C
        'timestamp': fake.date_time().isoformat()  # Data/hora realística
    }

if __name__ == '__main__':
    topic = 'temperature_sensor_topic' # Nome do tópico Kafka
    
    while True:
        data = generate_temperature_data() # Gera dados
        key = data['sensor_id']  # Usa ID do sensor como chave
        print(data)
        producer.send(topic, key=key, value=data)  # Envia mensagem
        time.sleep(1)  # Espera 1 segundo entre mensagens