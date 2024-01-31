from flask import Flask, request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app2.db'
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    messages = Message.query.all()
    html_content = "<h1>Welcome to App2</h1><ul>"
    for message in messages:
        html_content += f"<li>{message.content}</li>"
    html_content += "</ul>"
    return html_content

@app.route('/add_message', methods=['POST'])
def add_message():
    content = request.form.get('content')
    new_message = Message(content=content)
    db.session.add(new_message)
    db.session.commit()
    return 'Message added successfully!'

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')

