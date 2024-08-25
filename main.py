# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def submit_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    
    email = request.form.get('email')
    coment = request.form.get('text')
        
    if email and coment:
        with open('form.txt', 'a') as f:
            f.write(email + '/')
            f.write(coment + '----')
        
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html, button_db=button_db, email=email, coment=coment)
    
    
    
if __name__ == "__main__":
    app.run(debug=True)
