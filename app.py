from flask import Flask, render_template_string, render_template

from routes import main_bp


app = Flask(__name__)
app.jinja_env.auto_reload = True

# Регистрируем маршруты в приложении
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)