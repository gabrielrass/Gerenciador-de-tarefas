from rich import print
from datetime import date
import sqlite3
from rich.panel import Panel

class Cronograma:
    def __init__(self, nome = "not", assunto = "Not", status = True):
        self.Nome_tarefa = nome
        self.descricao = assunto
        self.status = status
        
    #CRIA E SALVA O BANCO DE DADOS...
    def dados(self):
        banco_de_dados = sqlite3.connect("tarefas.db")
        bd = banco_de_dados.cursor()

        bd.execute("""CREATE TABLE IF NOT EXISTS tarefas (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome_da_tarefa TEXT NOT NULL,
        Descricao TEXT NOT NULL,
        Status BOOLEAN NOT NULL
        )
        """)
        banco_de_dados.commit()#salvar alteração na tabela
        banco_de_dados.close() #fecha a tabela com a alteração
    
    def cadastrar_inf(self):
        
        banco_de_dados = sqlite3.connect("tarefas.db")
        bd = banco_de_dados.cursor()
        bd.execute("""INSERT INTO tarefas 
            (Nome_da_tarefa,
            Descricao,
            Status) VALUES (?,?,?)
            """, (self.Nome_tarefa, self.descricao, self.status))
        
        banco_de_dados.commit()#salvar alteração na tabela
        banco_de_dados.close() #fecha a tabela com a alteração
        
        
    #MOSTRA AS TAREFAS JÁ CADASTRADAS
    
    def mostrar_lista(self):
        banco_de_dados = sqlite3.connect("tarefas.db")
        bd = banco_de_dados.cursor()
        bd.execute("""SELECT * FROM  tarefas""")
        for tarefas in bd.fetchall():
            Id, Nome_da_tarefa, Descricao, Status = tarefas
            print(f"""Id: {Id}
            Nome da tarefa: {Nome_da_tarefa}
            Descrição: {Descricao}
            Status: {Status}""")
            print("\n")
        
        
    def excluir_tarefa(self, user):
        banco_de_dados = sqlite3.connect("tarefas.db")
        bd = banco_de_dados.cursor()
        #excluir IDs...
        bd.execute("""DELETE FROM tarefas
                   WHERE ID = ?
                   """, (user,))
        
        if bd.rowcount == 0:
            print("ID NÃO EXISTE!!!")
        else:
            print("ID excluido com sucesso!!!")
            
        banco_de_dados.commit()
        
    def modificador(self, id_inf, novo_nome = '', nova_desc = ''):
        banco_de_dados = sqlite3.connect("tarefas.db")
        bd = banco_de_dados.cursor()
        print(f"ID informado = {id_inf}")
        bd.execute("""
                   UPDATE tarefas
                   SET Nome_da_tarefa = ?,
                   Descricao = ?
                   WHERE ID = ?
                   """, (novo_nome, nova_desc, id_inf
                         ))
        
        if bd.rowcount == 0:
            print("ID não existe!!!")
        else:
            banco_de_dados.commit()
            print("ID editado com sucesso!!!")