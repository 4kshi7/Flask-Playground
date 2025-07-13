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

# create 
@app.route("/items", methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = {
        "id" : items[-1]["id"] + 1 if items else 1,
        "name" : data["name"]
    }
    items.append(new_item)
    return jsonify(new_item) , 201

# update
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    i = next((i for i in items if i["id"]==item_id), None)
    if i:
        i["name"] = data["name"]
        return jsonify(i)
    return jsonify({"error" : "item not found"}), 404


# delete
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = next((item for item in items if item["id"]==item_id), None)
    if item:
        items.remove(item)
        return jsonify({"message" : "item deleted"}), 200
    return jsonify({"error" : "item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
