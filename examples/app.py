import sqlite3


def setup_db():
    conn = sqlite3.connect("usuarios.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, username TEXT, senha TEXT)"
    )
    cur.execute("DELETE FROM usuarios")
    cur.execute("INSERT INTO usuarios (username, senha) VALUES ('admin', '123456')")
    conn.commit()
    conn.close()


def login(username, senha):
    conn = sqlite3.connect("usuarios.db")
    cur = conn.cursor()
    # VULNERÁVEL: a query é montada concatenando diretamente o que o usuário digitou.
    query = "SELECT * FROM usuarios WHERE username = '" + username + "' AND senha = '" + senha + "'"
    cur.execute(query)
    resultado = cur.fetchone()
    conn.close()
    return resultado is not None


if __name__ == "__main__":
    setup_db()
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if login(usuario, senha):
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha inválidos.")
