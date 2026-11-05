import sqlite3
banco = sqlite3.connect('primeiro_banco.db')
cursor = banco.cursor()
#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")
#cursor = banco.cursor()
cursor.execute("INSERT INTO pessoas VALUES('Fernando', 20,'Fernando@email.com')")

banco.commit()