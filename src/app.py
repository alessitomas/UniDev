from flask_login import LoginManager
from flask import Flask, request, jsonify
from flask_admin import Admin


app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='biblioteca', template_mode='bootstrap3')
admin.add_view(ModelView(AlunoMode, db.sessionl))
admin


login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def hello_world():
    return 'hello wrld'

if __name__ == "__main__":
    app.run(debug=True)