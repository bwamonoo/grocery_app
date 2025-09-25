from flask import Flask, render_template, request, redirect, url_for, abort
import os, json, tempfile

app = Flask(__name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")

# Ensure data file exists
def ensure_data_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)

def load_items():
    ensure_data_file()
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            items = json.load(f)
            if not isinstance(items, list):
                return []
            return items
        except json.JSONDecodeError:
            return []

def save_items(items):
    # atomic write: write to temp file then replace
    dirpath = os.path.dirname(DATA_FILE) or "."
    fd, tmp_path = tempfile.mkstemp(dir=dirpath)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as tmp:
            json.dump(items, tmp, indent=2)
            tmp.flush()
            os.fsync(tmp.fileno())
        os.replace(tmp_path, DATA_FILE)
    finally:
        if os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except OSError:
                pass

def next_id(items):
    if not items:
        return 1
    return max(item.get("id", 0) for item in items) + 1

@app.route("/", methods=["GET", "POST"])
def index():
    items = load_items()
    if request.method == "POST":
        name = request.form.get("name","").strip()
        qty = request.form.get("qty","").strip()
        if name:
            items.insert(0, {"id": next_id(items), "name": name, "qty": qty})
            save_items(items)
        return redirect(url_for("index"))
    return render_template("index.html", items=items)

@app.route("/item/<int:item_id>")
def view_item(item_id):
    items = load_items()
    item = next((it for it in items if it["id"] == item_id), None)
    if not item:
        return abort(404, "Item not found")
    return render_template("edit.html", item=item, view_only=True)

@app.route("/edit/<int:item_id>", methods=["GET", "POST"])
def edit_item(item_id):
    items = load_items()
    idx = next((i for i, it in enumerate(items) if it["id"] == item_id), None)
    if idx is None:
        return abort(404, "Item not found")
    if request.method == "POST":
        name = request.form.get("name","").strip()
        qty = request.form.get("qty","").strip()
        if name:
            items[idx]["name"] = name
            items[idx]["qty"] = qty
            save_items(items)
        return redirect(url_for("index"))
    return render_template("edit.html", item=items[idx], view_only=False)

@app.route("/delete/<int:item_id>", methods=["POST"])
def delete_item(item_id):
    items = load_items()
    new_items = [it for it in items if it["id"] != item_id]
    save_items(new_items)
    return redirect(url_for("index"))

if __name__ == "__main__":
    ensure_data_file()
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting app on 0.0.0.0:{port}", flush=True)
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)