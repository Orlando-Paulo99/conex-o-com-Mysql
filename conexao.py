import mysql.connector

banco=mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="paulo"
)


while True:
    x = input("Digite \n1 para cadaatar\n2 para pesquisar \n 3 para encerrar \n")
    if x =="1":
        nome1 = input("Digite o nome do aluno")
        telefone1 = int(input("Digite o telefone do aluno"))
        cursor = banco.cursor()
        sql = "INSERT INTO ALUNOS (nome,telefone)VALUES(%s, %s)"
        date = (nome1, telefone1)
        cursor.execute(sql, date)
        banco.commit()

    elif x == "2":

        meucursor = banco.cursor()
        pesquisa = "select * from alunos"
        meucursor.execute(pesquisa)
    # fetchall recebe tudo de pesquisa e retorna atraves de uma tupla
        resultado = meucursor.fetchall()
        for x in resultado:
            print(x[0], x[1],x[2])


    else:

        break
