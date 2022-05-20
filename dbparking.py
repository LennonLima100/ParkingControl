from sqlite3 import connect, Error


class DbParking():

    def __init__(self):
        
        self.conn = connect('usuario.db')

    def disconnect(self):
        self.conn.close()

    def autocommit(self):
        self.conn.commit()

    def usuario(self):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT * FROM usuario")
            retorno = cur.fetchall()
        except Error as e:
            print(e)
            retorno = False
            pass

        return retorno
        
    def IncluirUsuario(self, usuario, nome, senha, adm):
        cur = self.conn.cursor()
        try:
            cur.execute(f"INSERT INTO usuario VALUES('{usuario}',{nome},{senha},{adm})")
            retorno = True
        except Error as e:
            print(e)
            retorno = False

        return retorno