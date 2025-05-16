from kafka import KafkaConsumer # Classe para consumir mensagens do Kafka
import json # Para trabalhar com dados no formato JSON

# Initialize KafkaConsumer
consumer = KafkaConsumer(
    'temperature_sensor_topic',  # Nome do tópico que será monitorado
    api_version=(3, 8, 0), # Versão do Kafka (deve bater com a do servidor)
    bootstrap_servers='kafka:9092',  # Endereço do servidor Kafka
    auto_offset_reset='earliest',  # Começa a ler desde a 1ª mensagem disponível
    enable_auto_commit=True, # Confirma automaticamente o recebimento das mensagens
    group_id='temperature_sensor_consumer_group', # Identifica o grupo de consumidores
    value_deserializer=lambda x: json.loads(x.decode('utf-8')) # Converte bytes para JSON
)

if __name__ == '__main__':
    for message in consumer: # Fica escutando novas mensagens indefinidamente
        print(f"Received: {message.value}")  # Mostra o conteúdo de cada mensagem