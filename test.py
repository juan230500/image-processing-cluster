import requests
import threading

# URL of the Flask service
url_filter = 'http://127.0.0.1:64052/apply-filter'
url_cpu = 'http://127.0.0.1:64052/cpu-load'

def test_image_filter():
    files = {'image': open('input.jpg', 'rb')}
    data = {'filter': 'grayscale'}
    
    response = requests.post(url_filter, files=files, data=data)
    
    if response.status_code == 200:
        with open('output.jpg', 'wb') as f:
            f.write(response.content)
        print("Filter applied successfully, output saved as output.jpg")
    else:
        print("Failed to apply filter")

def test_cpu_load():
    try:
        response = requests.get(url_cpu)
        print(response.status_code, response.text)
    except Exception as e:
        print(e)

# Test Image Filtering
test_image_filter()

# Test CPU Load
threads = []
for i in range(500):
    t = threading.Thread(target=test_cpu_load)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
