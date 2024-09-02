import psycopg2

conectar = None 
try:

    conectar = psycopg2.connect(
        nombre = 'conectar',
        user = 'postgres',
        password = '12345678',
        host = 'localhost',
        port = '5432',
        database = 'conectar'
    
    )

    print ("conectar a postgresSQL")
    cur = conectar.cursor()
    cur.excute ("select * from usuarios")
    for id, nombre, estrato, venta, mes, in cur.fetchall():
        print (id, nombre, estrato, venta, mes)

    cur.close ()

except Exception as e:
    print ("error de conexion a posgresSQL ",e)
    if conectar is None:
        conectar.close()
