con = sqlite3.connect('dados_cadastro.db')

cursor = con.cursor()

 

cursor.execute('''CREATE TABLE "PLAYERS" (

               "nome" TEXT,

               "idade" INTEGER,

               "email" TEXT,

               "score" INTEGER

              

);''')

con.commit()
