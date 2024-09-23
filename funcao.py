import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='ouvidoria'
)

cursor = connection.cursor()
recordsAffect = cursor.rowcount


class Ouvidoria:
    

    def registro(self,y,x):
        
        if x == '1':
            x =  'critica'

            
        
        if x == '2':
            x = 'elogio'

        
        if x == '3':
            x = 'ocorrencia'

        
        sql="INSERT INTO clientes (texto, tipo) values (%s, %s)"
        data=(y,x)
        
        cursor.execute(sql, data)
        connection.commit()
            
    
    def listar(self, k):
        if k == 0:
            sql = "SELECT * from clientes where tipo = 'ocorrencia';"
            cursor.execute(sql)   
            listausuarios = cursor.fetchall()  
            print('\nOCORRENCIAS:\n')            
            for clientes in listausuarios:
                print(clientes[0], clientes[1])


                

            sql = "SELECT * from clientes where tipo = 'elogio';"
            
            cursor.execute(sql)   
            
            listausuarios = cursor.fetchall()  
            print('\nELOGIOS:\n')
            for clientes in listausuarios:
                print(clientes[0], clientes[1])


                

            sql = "SELECT * from clientes where tipo = 'critica';"
            
            cursor.execute(sql)   
            
            listausuarios = cursor.fetchall()  
            print('\nCRITICAS:\n')
            for clientes in listausuarios:

                print(clientes[0], clientes[1])      



                
        if k == 1:
            sql = "SELECT * from clientes where tipo = 'ocorrencia';"
            cursor.execute(sql)   
            listausuarios = cursor.fetchall()  
            print('\nOCORRENCIAS:\n')
            for clientes in listausuarios:
                print(clientes[0], clientes[1])
                
        if k == 2:
            sql = "SELECT * from clientes where tipo = 'elogio';"
            
            cursor.execute(sql)   
            
            listausuarios = cursor.fetchall()  
            print('\nELOGIOS:\n')
            for clientes in listausuarios:
                print(clientes[0], clientes[1])
                
        if k == 3:
            sql = "SELECT * from clientes where tipo = 'critica';"
            cursor.execute(sql)   
            listausuarios = cursor.fetchall()  
            print('\nCRITICAS:\n')
            for clientes in listausuarios:
                print(clientes[0], clientes[1])    
            

                
    def apagarespecifico(self,x):
            sql = "DELETE FROM clientes WHERE id = (%s)"
            data = (x,)
            cursor.execute(sql,data)
            connection.commit()
            print(' Apagado com sucesso !')

            
             
    
    def apagartudo(self):
            sql = "TRUNCATE TABLE clientes"
            cursor.execute(sql)
            connection.commit()
            print(' OK ! Tudo foi apagado.')