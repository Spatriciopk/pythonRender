from flask import Flask, render_template, request,redirect,url_for,flash
import main as m
app = Flask(__name__)
listClients=[]
contrato = 0

def cargarDatos():
    data = m.connection()
    global listClients
    listClients=[] 
    for x in data:
        cliente ={
    'intContrato':x[0],
    'strNombre':x[1].rstrip(),
    'strIdplan':x[3],
    'strStatus':x[2]
    }
        listClients.append(cliente)


@app.route('/')
def index():
    global listClients
    cargarDatos()
    return render_template('index.html', dicData=listClients)


@app.route('/modal/<id>')
def modal(id):
    global listClients
    global contrato
    cargarDatos()
    contrato = id
    print(contrato)
    return render_template('modal.html', dicData=listClients,contrato=contrato)


@app.route('/enviar' ,methods=['POST'])
def submit():
    global listClients
    if request.method == 'POST':
        name = request.form['plan']
        listData = name.split("|");
        m.newvalue(listData[1],listData[0]);
    return redirect('/')
  

if __name__== '__main__':
    app.run(debug=True)