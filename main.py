import pymssql
  
def connection():
    cursor.execute('SELECT [numeroContrato],[titularContrato],[StatusContrato],[idPlan],[idAfiliado],[rowversion] FROM [dbo].[ContratoSeguroSalud] WHERE [StatusContrato] = \'En Curso\'')
    consulta = cursor.fetchall()
    return consulta

def newvalue(titular, status):
    cursor.execute('UPDATE [dbo].[ContratoSeguroSalud] SET [StatusContrato] = \'' + status + '\' WHERE [numeroContrato] =\''+ titular + '\' and [StatusContrato] = \'En Curso\'' )
    conn.commit()
    print('Ejecutado')

conn = pymssql.connect(server='miservidorsqlbayteq.database.windows.net', user='paul.penafiel', password='Bayteq123.', database='BaseSegurosEjemplo')  
cursor = conn.cursor() 