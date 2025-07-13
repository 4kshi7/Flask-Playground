```markdown
# Simple Flask CRUD API

This is a basic **Flask API** project that demonstrates full **CRUD** (Create, Read, Update, Delete) operations using an **in-memory list**. 

---

## Project Structure

```

.
├── app.py         # Main Flask application
└── README.md      # Project documentation

````

---

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/flask-crud-api.git
cd flask-crud-api
````

### 2. Set up a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
# OR
source venv/bin/activate  # For macOS/Linux
```

### 3. Install Flask

```bash
pip install Flask
```

### 4. Run the app

```bash
python app.py
```

Open your browser or Postman and go to:
**[http://localhost:5000](http://localhost:5000)**

---

##  API Endpoints & Logic

### `/` → **GET**

* Returns a welcome message.

```json
{ "message": "Learning CRUD in FLASK" }
```

---

### `/items` → **GET**

* Returns all items from the in-memory list.

```json
[
  { "id": 1, "name": "Rust" },
  { "id": 2, "name": "TypeScript" },
  { "id": 3, "name": "Java" }
]
```

---

### `/items/<id>` → **GET**

* Returns a specific item by ID.
* If not found, returns 404 with custom error.

```json
{ "error": "cant find bro" }
```

---

### `/items` → **POST**

* Creates a new item.
* Requires JSON body like:

```json
{ "name": "Go" }
```

* Automatically assigns a new `id`.
* Returns the new item with `201 Created`.

---

### `/items/<id>` → **PUT**

* Updates an existing item by ID.
* Requires JSON body like:

```json
{ "name": "Updated Name" }
```

* Returns updated item or 404 if not found.

---

### `/items/<id>` → **DELETE**

* Deletes an item by ID.
* Returns success message or 404 if item doesn't exist.

---

## How It Works (Logic Flow)

* Data is stored in a **list of dictionaries**, simulating a simple in-memory database.
* Each route:

  * Uses Flask route decorators (`@app.route`)
  * Parses data using `request.get_json()` for POST/PUT
  * Uses Python’s `next()` to find items by ID
  * Sends back JSON using `jsonify()`

```

