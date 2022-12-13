import pymssql  
def connection():
    conn = pymssql.connect(server='miservidorsqlbayteq.database.windows.net', user='paul.penafiel', password='Bayteq123.', database='BaseSegurosEjemplo')  
    cursor = conn.cursor()  
    cursor.execute('SELECT * FROM dbo.ContratoSeguroSalud;')  
    row = cursor.fetchall()
    return row 