from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message" : "Learning CRUD in FLASK"})

items = [
    {"id": 1, "name": "Rust"},
    {"id": 2, "name": "TypeScript"},
    {"id": 3, "name": "Java"}
]

# read all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# read single item
@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id']==item_id), None)
    if item:
        return jsonify(item)
    return jsonify({
        "error" : "cant find bro"
    }), 404


if __name__ == '__main__':
    app.run(debug=True)
