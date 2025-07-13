````markdown
# Flask Playground 🔥

A simple project to learn how to build **RESTful APIs** using [Flask](https://flask.palletsprojects.com/) in Python. This covers **CRUD operations** (Create, Read, Update, Delete) using in-memory data.

---

## 🚀 Getting Started

### 1. Install Flask

```bash
pip install flask
````

### 2. Run the App

```bash
python app.py
```

App runs on: [http://localhost:5000](http://localhost:5000)

---

## 📌 API Endpoints

| Method | Endpoint      | Description       |
| ------ | ------------- | ----------------- |
| GET    | `/`           | Welcome message   |
| GET    | `/items`      | Get all items     |
| GET    | `/items/<id>` | Get item by ID    |
| POST   | `/items`      | Create a new item |
| PUT    | `/items/<id>` | Update item by ID |
| DELETE | `/items/<id>` | Delete item by ID |

---

## 📚 Example Requests & Responses

### ➤ `GET /`

```json
{
  "message": "Learning CRUD in FLASK"
}
```

---

### ➤ `GET /items`

```json
[
  {"id": 1, "name": "Rust"},
  {"id": 2, "name": "TypeScript"},
  {"id": 3, "name": "Java"}
]
```

---

### ➤ `GET /items/2`

```json
{
  "id": 2,
  "name": "TypeScript"
}
```

Error if not found:

```json
{
  "error": "cant find bro"
}
```

---

### ➤ `POST /items`

**Request Body (JSON):**

```json
{
  "name": "Python"
}
```

**Response:**

```json
{
  "id": 4,
  "name": "Python"
}
```

---

### ➤ `PUT /items/3`

**Request Body:**

```json
{
  "name": "Java SE"
}
```

**Response:**

```json
{
  "id": 3,
  "name": "Java SE"
}
```

---

### ➤ `DELETE /items/1`

**Response:**

```json
{
  "message": "item deleted"
}
```

Error if not found:

```json
{
  "error": "item not found"
}
```

---

## 🧠 Code Explanation

### 1. App Setup

```python
from flask import Flask, jsonify, request

app = Flask(__name__)
```

* Import Flask and create the app instance.

---

### 2. Root Route

```python
@app.route('/')
def index():
    return jsonify({"message" : "Learning CRUD in FLASK"})
```

* Returns a welcome message when visiting the root URL.

---

### 3. In-Memory Database

```python
items = [
    {"id": 1, "name": "Rust"},
    {"id": 2, "name": "TypeScript"},
    {"id": 3, "name": "Java"}
]
```

* Using a list to store item data without a database.

---

### 4. Read All Items

```python
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)
```

---

### 5. Read Single Item

```python
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    ...
```

---

### 6. Create Item

```python
@app.route('/items', methods=['POST'])
def create_item():
    ...
```

---

### 7. Update Item

```python
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    ...
```

---

### 8. Delete Item

```python
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    ...
```

---
