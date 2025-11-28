from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Load the dataset
with open('TreecEva_data_merged_cot.json', 'r', encoding='utf-8') as f:
    dataset = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    """Get all data IDs and basic info"""
    items = []
    for item in dataset:
        if 'id' in item:
            items.append({
                'id': item['id'],
                'language': item['metadata']['language'],
                'difficulty': item['metadata']['difficulty']
            })
    return jsonify(items)

@app.route('/api/data/<data_id>')
def get_item(data_id):
    """Get specific item by ID"""
    for item in dataset:
        if item.get('id') == data_id:
            return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

@app.route('/api/search')
def search():
    """Search by ID"""
    query = request.args.get('q', '').upper()
    results = []
    for item in dataset:
        if 'id' in item and query in item['id']:
            results.append({
                'id': item['id'],
                'language': item['metadata']['language'],
                'difficulty': item['metadata']['difficulty']
            })
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)