import sistema as st
import customtkinter as tk
G1 = st.Cronograma()

def lista_bd():
    dados = G1.mostrar_lista()
    for tarefas in dados:
        ID, Nome_da_tarefa, Descricao, Status = tarefas
        resultado_b1 = tk.CTkLabel(gt, text=f"{tarefas}")
        resultado_b1.pack()
#base do menu
menu_text = [("Ver tarefas", lista_bd), 
             ("Cadastrar tarefas", G1.cadastrar_inf),
             ("Excluir tarefas", G1.excluir_tarefa),
             ("Modificar tarefas", G1.modificador),
             ("Atualizar status", G1.atualizar_status)
             ]
print("\n")

#tema do programa
tk.set_appearance_mode("Dark")
#Criação da janela
gt = tk.CTk()
gt.title("Gerenciador de tarefas")
gt.geometry("500x500")
#criação do label / botões de interação
for text, func in menu_text:
    organizar = tk.CTkFrame(gt, fg_color="transparent")
    organizar.pack(anchor="w", pady=3, padx= 20)
    
    gt_label = tk.CTkLabel(organizar, text=f"{text}",width=150, anchor="w")
    gt_label.pack(anchor = "w", side= "left", padx=20)
    
    botao = tk.CTkButton(organizar, text= "ver", width=80, command= func)
    botao.pack(side="left", padx=10)
    
    resul_button = tk.CTkLabel(gt, text="")
    resul_button.pack()    
    
    #função do botão
    if botao == G1.mostrar_lista:
        resul_button.configure(text=f"{G1.mostrar_lista()}")
        resul_button.pack(pady=10)



gt.mainloop()