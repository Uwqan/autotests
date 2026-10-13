from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}$")

@app.route("/")
def index():
    return render_template("contact.html")


@app.route("/api/contact", methods=["POST"])
def contact():
    data = request.get_json() or {}
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    message = (data.get("message") or "").strip()
    subject = (data.get("subject") or "").strip()

    errors = {}

    if not name:
        errors["name"] = "Имя обязательно для заполнения"
    elif len(name) < 2:
        errors["name"] = "Имя должно содержать минимум 2 символа"
    elif len(name) > 50:
        errors["name"] = "Имя не должно превышать 50 символов"

    if not email:
        errors["email"] = "Email обязателен для заполнения"
    elif not EMAIL_RE.match(email):
        errors["email"] = "Некорректный формат email"

    if not subject:
        errors["subject"] = "Тема обязательна для заполнения"
    elif len(subject) < 3:
        errors["subject"] = "Тема должна содержать минимум 3 символа"

    if not message:
        errors["message"] = "Сообщение обязательно для заполнения"
    elif len(message) < 10:
        errors["message"] = "Сообщение должно содержать минимум 10 символов"
    elif len(message) > 1000:
        errors["message"] = "Сообщение не должно превышать 1000 символов"

    if errors:
        return jsonify({"errors": errors}), 400

    return jsonify({"ok": True, "message": "Спасибо! Ваше сообщение отправлено."})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)