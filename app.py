from flask import Flask, render_template

class Cancion:
    def __init__(self,titulo,categoria,idioma):
        self.titulo=titulo
        self.categoria= categoria
        self.idioma=idioma

app = Flask(__name__)

@app.route('/')

def index():
    cancion1=Cancion('La guitarra','pop','castellano')
    cancion2=Cancion('para no verte mas','pop','castellano')
    cancion3=Cancion('balada para un gordo','balada','castellano')
    lista=[cancion1,cancion2,cancion3]    
    return render_template('listar.html', titulo='Canciones',musicas=lista)

@app.route('/nuevoregistro')
def nuevoRegistro():
    return render_template('nuevoRegistro.html', titulo='Nueva Canción')
    #return 'estoy en nuevo registro' 


  
app.run(host="0.0.0.0", port=5000)