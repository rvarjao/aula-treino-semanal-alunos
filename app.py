from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

def get_connection():
    conn = sqlite3.connect("treinos.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()

    # TODO 1:
    # Ler o arquivo schema.sql e executar o script SQL para criar a tabela.
    # Dica: use with open(...) e conn.executescript(...)

    conn.commit()
    conn.close()

@app.route("/")
def index():
    conn = get_connection()

    # TODO 2:
    # Buscar os treinos no banco de dados.
    # A variável precisa se chamar: treinos
    #
    # Dica de consulta:
    # SELECT * FROM treino_semanal ORDER BY id DESC
    #
    # Exemplo esperado:
    # treinos = conn.execute("...").fetchall()

    conn.close()

    html = """
    <html>
    <head>
        <meta charset="utf-8">
        <title>Treino Semanal</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>Programa Semanal de Treino</h1>
        <p class="mensagem">Cadastre os exercícios da semana e veja a lista abaixo.</p>

        <div class="acoes">
            <a href="/novo">Novo treino</a>
        </div>

        <div class="lista">
    """

    # TODO 3:
    # Percorrer a lista de treinos e mostrar os dados na tela.
    # Cada treino deve mostrar:
    # - dia
    # - grupo
    # - exercicio
    # - carga
    #
    # Dica:
    # for treino in treinos:
    #     html += f"..."

    html += """
        </div>
    </body>
    </html>
    """

    return html

@app.route("/novo", methods=["GET", "POST"])
def novo():
    if request.method == "POST":
        dia = request.form.get("dia")
        grupo = request.form.get("grupo")
        exercicio = request.form.get("exercicio")
        carga = request.form.get("carga")

        conn = get_connection()

        # TODO 4:
        # Inserir os dados na tabela treino_semanal.
        # Campos:
        # dia, grupo, exercicio, carga
        #
        # Dica:
        # conn.execute(
        #     """
        #     INSERT INTO treino_semanal (dia, grupo, exercicio, carga)
        #     VALUES (?, ?, ?, ?)
        #     """,
        #     (dia, grupo, exercicio, carga)
        # )

        conn.commit()
        conn.close()

        return redirect("/")

    return """
    <html>
    <head>
        <meta charset="utf-8">
        <title>Novo treino</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>Novo treino</h1>

        <form method="POST" class="formulario">
            <!-- TODO 5:
                 Você pode trocar os placeholders e melhorar os textos -->
            <input name="dia" placeholder="Ex: Segunda">
            <input name="grupo" placeholder="Ex: Costas">
            <input name="exercicio" placeholder="Ex: Puxada frontal">
            <input name="carga" placeholder="Ex: 35kg">

            <button type="submit">Salvar</button>
        </form>

        <a href="/">Voltar</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    init_db()
    app.run(debug=True)