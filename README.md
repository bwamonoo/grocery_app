Got it 👍 — here’s a complete **Markdown version** of the `README.md` you can copy directly:

```markdown
# Grocery App 🛒  

A very simple **Flask web app** to manage a grocery list.  
You can **add, view, edit, and delete** items.  
The data is stored in a local `data.json` file, so no database setup is required.  

---

## 🚀 Features
- Add grocery items with an optional quantity  
- View all groceries or a single item  
- Edit existing items  
- Delete items  
- Data persists in `data.json` (simple file-based storage)  
- Minimal **HTML + CSS** for a clean interface  

---

## 📂 Project Structure
```

grocery\_app/
├─ app.py              # Flask application
├─ data.json           # File where groceries are stored (auto-created)
├─ templates/          # HTML templates
│  ├─ index.html
│  └─ edit.html
└─ static/             # CSS styling
└─ style.css

````

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/bwamonoo/grocery_app.git
cd grocery_app
````

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows
```

### 3. Install dependencies

```bash
pip install flask
```

### 4. Run the app

```bash
python app.py
```

By default, the app will start on:
👉 `http://127.0.0.1:5000/`

On Raspberry Pi, it runs on `http://0.0.0.0:5000/` so other devices in your network can access it.

---

## 🖥️ Usage

1. Open the app in your browser.
2. Use the **form** at the top to add grocery items (name + optional quantity).
3. Use **View** to see an item, **Edit** to modify it, or **Delete** to remove it.
4. The list is saved in `data.json` automatically.

---

## 🔧 Customization

* Change styles in `static/style.css`
* Update HTML templates in `templates/`
* Extend `app.py` to add more features (categories, done/undone items, etc.)

---

## 📜 License

This project is for learning and personal use. Feel free to modify and extend it.
