from flask import Flask, render_template, request
import main as m
app = Flask(__name__)

@app.route('/')
def index():
    data = m.connection()
    global cliente 
    cliente = []
    for x in data:
        nContrato = x[0]
        nombre = x[1]
        idplan = x[3]
        status = x[2]
        cliente.append([nContrato, nombre, idplan, status])
    consulta = {'cliente': cliente}
    return render_template('index.html', data=consulta)

@app.route('/enviar' ,methods=['POST'])
def submit():
    #val = request.form.get(str(cliente[0][0]))
    #val = cliente[0][1] + val
    for x in cliente:
        val = request.form.get(str(x[0]))
        print(x[1], len(x[1]), val)
        m.newvalue('\''+x[1]+'\'', '\''+val+'\'')
    return 'Base de datos acutalizada'

if __name__== '__main__':
    app.run()
