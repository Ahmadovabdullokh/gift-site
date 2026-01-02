# app.py
# ПОДАРОЧНЫЙ МНОГОСТРАНИЧНЫЙ САЙТ ДЛЯ ДЕВУШКИ (Flask)
# ИСПРАВЛЕННАЯ И УПРОЩЁННАЯ СТАБИЛЬНАЯ ВЕРСИЯ

from flask import Flask, render_template_string, request, session
import random
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "super_secret_key_123"

# ===================== НАСТРОЙКИ =====================
SITE_NAME = "💖 Для тебя 💖"
ADMIN_PASSWORD = "admin123"

# ===================== ДАННЫЕ =====================
COMPLIMENTS = [
    "Ты делаешь этот мир красивее просто тем, что ты есть",
    "Рядом с тобой всегда спокойно и тепло",
    "Ты невероятно милая",
    "Твоя улыбка делает день лучше",
    "Ты особенная, и это чувствуется",
    "С тобой хочется быть лучше",
    "Ты — настоящее чудо",
    "Ты умеешь делать счастливыми одним взглядом",
    "В тебе удивительно сочетаются нежность и сила",
    "Ты как тёплый вечер после долгого дня",
    "Ты вдохновляешь меня даже тогда, когда молчишь",
    "Ты красивая так, что это невозможно не заметить",
    "С тобой хочется строить планы и мечтать",
    "Ты делаешь обычные моменты особенными",
    "Ты — та, о ком думаешь перед сном",
    "Твоё присутствие уже подарок",
    "Ты умеешь быть собой — и это самое прекрасное",
    "Ты светишься изнутри",
    "Ты именно такая, какая нужна этому миру",
    "Ты заставляешь сердце биться быстрее"
]

FLIRTS = [
    "Кажется, этот сайт в тебя влюбился",
    "Если бы это было свидание, я бы не хотел, чтобы оно заканчивалось",
    "Ты украла моё внимание полностью",
    "Каждый раз, когда ты здесь — мне становится теплее",
    "Осторожно, ты слишком привлекательна",
    "Если бы у меня был выбор — я бы выбрал тебя снова",
    "Этот момент был бы идеальным, если бы ты была рядом",
    "Ты умеешь быть опасно очаровательной",
    "Кажется, я улыбаюсь, просто думая о тебе",
    "Ты выглядишь так, будто знаешь, что сводишь с ума",
    "Я бы хотел читать тебя, как любимую книгу",
    "Ты — та самая причина, по которой день становится лучше",
    "Если это флирт — то очень искренний",
    "Ты слишком хороша для случайных людей",
    "С тобой хочется говорить даже без слов"
]

COMFORT_TEXTS = [
    "Ты в безопасности",
    "Здесь можно просто быть собой",
    "Всё будет хорошо",
    "Ты не обязана быть сильной всегда",
    "Тебя здесь понимают",
    "Можно просто выдохнуть",
    "Ты заслуживаешь покоя и тепла",
    "Этот момент — только для тебя",
    "Ты не одна",
    "Можно остановиться и отдохнуть",
    "Ты ценна просто потому, что ты есть",
    "Здесь тебя принимают такой, какая ты есть"
]

# ===================== ШАБЛОН =====================
BASE_PAGE = """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<title>{{ title }} | {{ site_name }}</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body {background: linear-gradient(135deg,#ff9a9e,#fad0c4);font-family:Arial;color:#fff;margin:0}
nav {background:rgba(0,0,0,.3);padding:15px;text-align:center}
nav a {color:#fff;margin:0 10px;text-decoration:none;font-weight:bold}
.container {max-width:800px;margin:40px auto;background:rgba(0,0,0,.25);padding:30px;border-radius:20px}
button {padding:12px 22px;border:none;border-radius:20px;cursor:pointer}
textarea {width:100%;padding:10px;border-radius:10px;border:none}
</style>
</head>
<body>
<nav>
<a href="/">Главная</a>
<a href="/compliments">Комплименты</a>
<a href="/flirt">Флирт</a>
<a href="/comfort">Уют</a>
<a href="/message">Сообщение</a>
<a href="/admin">Админ</a>
</nav>
<div class="container">{{ content|safe }}</div>
</body>
</html>
"""

# ===================== СТРАНИЦЫ =====================
@app.route("/")
def index():
    quote = random.choice(COMPLIMENTS)
    today = datetime.now().strftime('%d.%m.%Y')
    content = f"""
    <h1>Этот сайт — только для тебя 💗</h1>
    <p style='font-style:italic'>«{quote}»</p>
    <p>Сегодня: {today}</p>
    <p>Здесь можно улыбаться, флиртовать и просто чувствовать тепло 💕</p>
    """
    return render_template_string(BASE_PAGE, title="Главная", site_name=SITE_NAME, content=content)

@app.route("/compliments")
def compliments():
    return render_template_string(BASE_PAGE, title="Комплименты", site_name=SITE_NAME,
        content=f"<h2>Комплимент</h2><p>{random.choice(COMPLIMENTS)}</p><a href='/compliments'><button>Ещё</button></a>")

@app.route("/flirt")
def flirt():
    return render_template_string(BASE_PAGE, title="Флирт", site_name=SITE_NAME,
        content=f"<h2>Флирт</h2><p>{random.choice(FLIRTS)}</p><a href='/flirt'><button>Продолжить</button></a>")

@app.route("/comfort")
def comfort():
    return render_template_string(BASE_PAGE, title="Уют", site_name=SITE_NAME,
        content=f"<h2>Уют</h2><p>{random.choice(COMFORT_TEXTS)}</p>")

@app.route("/message", methods=["GET","POST"])
def message():
    info = ""
    if request.method == "POST":
        text = request.form.get("text")
        if text:
            with open("messages.txt","a",encoding="utf-8") as f:
                f.write(f"[{datetime.now().strftime('%d.%m.%Y %H:%M')}] {text}\n")
            info = "<p>Сообщение сохранено ❤️</p>"

    return render_template_string(BASE_PAGE, title="Сообщение", site_name=SITE_NAME,
        content=f"<h2>Сообщение для меня</h2><form method='post'><textarea name='text' required></textarea><br><br><button>Отправить</button></form>{info}")

@app.route("/admin", methods=["GET","POST"])
def admin():
    if request.method == "POST" and request.form.get("password") == ADMIN_PASSWORD:
        session["admin"] = True

    if not session.get("admin"):
        return render_template_string(BASE_PAGE, title="Админ", site_name=SITE_NAME,
            content="<h2>Вход администратора</h2><form method='post'><input type='password' name='password'><br><br><button>Войти</button></form>")

    try:
        with open("messages.txt","r",encoding="utf-8") as f:
            messages = f.read().replace("\n","<br>")
    except FileNotFoundError:
        messages = "Сообщений пока нет"

    return render_template_string(BASE_PAGE, title="Сообщения", site_name=SITE_NAME,
        content=f"<h2>Её сообщения 💌</h2><div style='text-align:left'>{messages}</div>")

# ===================== ЗАПУСК =====================
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
