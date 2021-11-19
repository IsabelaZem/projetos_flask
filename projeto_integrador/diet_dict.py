from flask import pandas as pd
from diet_dict import diet_dict

diet_dict = {"w2": "CAFE ALMOCO JANTA"}


def get_token():
    token = input("Digite o numero de usuario: ")
    return token

def get_days(token):
    
    query = "SELECT dias FROM contagem WHERE identificador = %s"%(token)
    data = pd.read_sql(query, database)
    return data.iloc[0]['dias']

def get_diet(days):
    if (days/7) > 1:
        diet_ref = "w2"
    return diet_ref

def main():
    token = get_token()
    days = get_days(token)
    diet = get_diet(days)
    print(diet_dict[diet])

if __name__ == "__main__":
    main()

import mysql.connector as sql

def entry():
    name = input("Digite seu nome: ")
    last_name = input("Digite seu sobrenome: ")
    age = input("Digite sua idade: ")
    age = int(age)
    id = getid(name, last_name, age)
    user_entry = (id, name, last_name, age)
    return user_entry

def getid(name, last_name, age):
    id = (len(name) + len(last_name)) * age
    return id

def insert(user_entry):
    database = sql.connect(host = "localhost", user = "root", passwd = "345435", database = "projeto_integrador")

    query = "INSERT INTO base_pessoas (identificador, nome, sobrenome, idade) VALUES (%s, %s, %s, %s)"
    values = user_entry
    cursor = database.cursor()
    cursor.execute

def entry():
    name = input("Digite seu nome: ")
    last_name = input("Digite seu sobrenome: ")
    age = input("Digite sua idade: ")
    age = int(age)
    id = getid(name, last_name, age)
    user_entry = (id, name, last_name, age)
    return user_entry

def getid(name, last_name, age):
    id = (len(name) + len(last_name)) * age
    return id

def insert(user_entry):
    database = sql.connect(host = "localhost", user = "root", passwd = "345435", database = "projeto_integrador")

    query = "INSERT INTO base_pessoas (identificador, nome, sobrenome, idade) VALUES (%s, %s, %s, %s)"
    values = user_entry
    cursor = database.cursor()
    cursor.execute(query, values)
    database.commit()

    query = "INSERT INTO contagem (identificador, dias) VALUES (319, 9)"
    cursor.execute(query)
    database.commit()

def main():
    user_entry = entry()
    insert(user_entry)
    print("Usuario inserido com sucesso.")

if __name__ == "__main__":
    main()