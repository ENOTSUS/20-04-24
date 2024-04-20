import requests
import threading

url = 'https://roams.io'  # Замените на URL целевого сервера
num_requests = 1000  # Количество запросов для отправки

def send_request():
    response = requests.get(url)
    print(response.status_code)

# Создаем и запускаем несколько потоков для отправки запросов
threads = []
for _ in range(num_requests):
    thread = threading.Thread(target=send_request)
    threads.append(thread)
    thread.start()

# Ждем завершения всех потоков
for thread in threads:
    thread.join()