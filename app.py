from flask import Flask 

app= Flask(__name__)

@app.route('/')
def home():
    return "¡Hola mundo!"

@app.route('/saludo')
def saludo():
    return "Bienvenido a mi primera App"

@app.route('/saludo/<nombre>')
def saludo_personalizado(nombre):
    return f"Hola, {nombre}"

if __name__=='__main__':
    app.run(debug=True)
