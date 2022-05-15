import sqlite3

connection = sqlite3.connect('data/database.db')

with open('data/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Post DevOps', 'DevOps (junção das palavras “desenvolvimento” e “operação”) é um modelo que combina filosofias culturais, práticas e ferramentas que aumentam a capacidade de uma empresa distribuir seus serviços em alta velocidade.')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Post Microsservicos', 'Microsserviços são uma abordagem arquitetônica e organizacional do desenvolvimento de software na qual o software consiste em pequenos serviços independentes que se comunicam usando APIs bem definidas. Esses serviços pertencem a pequenas equipes autossuficientes.')
            )

connection.commit()
connection.close()