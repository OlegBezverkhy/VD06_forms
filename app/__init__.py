from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ArosaupalanalapuasorA'


from app import routes
