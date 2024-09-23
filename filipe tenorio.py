import funcao
import mysql.connector

connection = mysql.connector.connect(  #DB= ouvidoria  TABLE = clientes  COLUMNS = id , texto , tipo. KEY = ID 
    host='localhost',
    user='root',
    password='root',
    database='ouvidoria'
)

cursor = connection.cursor()



print(' Ouvidoria XYZ ! Seja Bem Vindo !')

Q = 0

novo = funcao.Ouvidoria()

while Q != 4:                 
    
    Q = 0
    
    print('\n -MENU- \n')
    Q = int(input(""" Você deseja ? 
        [1]  Registrar ocorrência, critica ou elogio.
        [2]  Listar as ocorrências, criticas e elogios.
        [3]  Remover ocorrências, criticas ou elogios.
        [4]  Sair \n"""))
    
    if Q == 1:
        
        escolher = input('Critica digite 1.  Elogio digite 2. Ocorrencia digite 3.')
        if escolher =='1':
            regist = input('Diga aqui sua critica:\n R: ')
            novo.registro(regist,escolher)

        
        if escolher == '2':
            regist = input('Diga aqui seu elogio:\n R:  ')
            novo.registro(regist,escolher)

        if escolher == '3':
            regist = input('Diga aqui sua ocorrência:\n R:  ')
            novo.registro(regist,escolher)

    
    if Q == 2:
        
        escolha = int(input(' Listar tudo [0], Listar Apenas Ocorrencia [1] , Apenas Elogio [2], Apenas Critica [3]'))
        novo.listar(escolha)

    if Q == 3:
        escolha = int(input('Se quiser remover tudo digite 0. Ocorrencia 1.  Elogio digite 2. Critica digite 3 \n R: '))
        
        if escolha == 0:
            novo.apagartudo()

        else:
            novo.listar(escolha)
            x = int(input('Qual deseja remover ?\nR:'))
            novo.apagarespecifico(x)
    


print(' Ok !  Obrigado pela visita. ')
    