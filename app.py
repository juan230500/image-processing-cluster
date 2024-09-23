from flask import Flask, request, send_file
from filters import apply_filter
import os
import math

app = Flask(__name__)

@app.route('/apply-filter', methods=['POST'])
def filter_image():
    if 'image' not in request.files:
        return "No image file provided", 400
    
    image = request.files['image']
    filter_type = request.form.get('filter', 'grayscale')
    
    input_path = 'input.jpg'
    output_path = 'output.jpg'
    
    image.save(input_path)
    
    apply_filter(input_path, output_path, filter_type)
    
    return send_file(output_path, mimetype='image/jpeg')

@app.route('/cpu-load', methods=['GET'])
def cpu_intensive_task():
    # Simulate a CPU-intensive task
    result = 0
    for i in range(1, 1000000):
        result += math.sqrt(i)
    return "Task Completed!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
