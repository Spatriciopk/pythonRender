from flask import Flask, render_template, request,redirect,url_for,flash
import main as m
app = Flask(__name__)
listClients=[]
datalist = []
informacion =   {
        'numContrato' :  "",
        'strNombre' :  "",
        'strStatus' :  "",
        'strTipoPlan' :  "",
        'strCedula' :  ""
        }
datalist=[informacion]

def cargarDatos():
    data = m.connection()
    global listClients
    global datalist
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
    return render_template('index.html', dicData=listClients,contrato=datalist)


@app.route('/modal/<id>')
def modal(id):
    global listClients
    global datalist
    data = m.searchdata(id)
    informacion =   {
        'numContrato' :  data[0][0],
        'strNombre' :  data[0][1],
        'strStatus' :  data[0][2],
        'strTipoPlan' :  data[0][3],
        'strCedula' :  data[0][4]
        }
    datalist=[informacion]
    cargarDatos()
    return render_template('modal.html', dicData=listClients,contrato=datalist)


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