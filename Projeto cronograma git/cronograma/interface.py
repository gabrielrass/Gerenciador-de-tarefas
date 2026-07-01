import sistema as st
import customtkinter as tk
G1 = st.Cronograma()
G1.dados()
#mostrar lista de tarefas
def lista_bd():
    dados = G1.mostrar_lista()
    for tarefas in dados:
        ID, Nome_da_tarefa, Descricao, Status = tarefas
        resultado_b1 = tk.CTkLabel(Janela_principal, text=f"{tarefas}")
        resultado_b1.pack()
#cadastrar tarefas
def cadastro():
    janela_de_cadastro = tk.CTkFrame(Janela_principal)
    tk.CTkLabel(janela_de_cadastro, text="Bem vindo a área de cadastro!!!").pack()
    organizar.pack_forget()
    janela_de_cadastro.pack()
    
    usuario_Nome = tk.CTkEntry(janela_de_cadastro, placeholder_text="Nome da tarefa")
    usuario_Nome.pack()
    usuario_desc = tk.CTkEntry(janela_de_cadastro, placeholder_text="Digite a descrição")
    usuario_desc.pack()
    def enviar_resposta():
        cadastro = st.Cronograma(usuario_Nome.get(), usuario_desc.get())
        cadastro.cadastrar_inf()
        
    botao_cadastro = tk.CTkButton(janela_de_cadastro, text="Confirmar", command=enviar_resposta)
    botao_cadastro.pack()
        
#base do menu
menu_text = [("Ver tarefas", lista_bd), 
             ("Cadastrar tarefas", cadastro),
             ("Excluir tarefas", G1.excluir_tarefa),
             ("Modificar tarefas", G1.modificador),
             ("Atualizar status", G1.atualizar_status)
             ]
print("\n")

#tema do programa
tk.set_appearance_mode("Dark")
#Criação da janela
Janela_principal = tk.CTk()
Janela_principal.title("Gerenciador de tarefas")
Janela_principal.geometry("500x500")
#criação do label / botões de interação
for text, func in menu_text:
    organizar = tk.CTkFrame(Janela_principal, fg_color="transparent")
    organizar.pack(anchor="w", pady=3, padx= 20)
    
    gt_label = tk.CTkLabel(organizar, text=f"{text}",width=150, anchor="w")
    gt_label.pack(anchor = "w", side= "left", padx=20)
    
    botao = tk.CTkButton(organizar, text= "ver", width=80, command= func)
    botao.pack(side="left", padx=10)
    
    resul_button = tk.CTkLabel(organizar, text="")
    resul_button.pack()

Janela_principal.mainloop()