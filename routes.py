
from flask import Blueprint, render_template_string, render_template

from models.user_model import UserRepository
from views.user_view import format_users_forview

# Создаем Blueprint. 
# 'main' — это уникальное имя чертежа, __name__ указывает на текущий модуль
main_bp = Blueprint('main', __name__)


# Главная страница
@main_bp.route('/')
def home():
    return render_template("index.html")

# вторая страница
@main_bp.route('/two')
def home2():
    return render_template("second_page.html")

# реализация MVC - модель, вид, контроллер
@main_bp.route("/users")
def show_users():
    #Controller_logic
    repo = UserRepository()
    users = repo.get_all_users()

    formated_users = format_users_forview(users)
    return render_template("users.html", users=formated_users)
