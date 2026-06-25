import sistema
print("Bem-Vindo ao sistema de gerenciamento de tarefas!!!")
interface = ("Ver tarefas", "Cadastrar tarefas", "Excluir tarefas", "Modificar tarefas", "Atualizar status", "Sair")
print("\n")
TG = sistema.Cronograma()
TG.dados()
while True:
    print("\n")
    for c, v in enumerate(interface):
        print(f"[{c+1}]  {v} ")
        
    user = int(input("Escolha uma opção: "))
    if user == 1:
        TG.mostrar_lista()
        
    if user == 2:
        nome_tarefa = str(input("Nome da tarefa: "))
        desc = str(input("Sobre a tarefa: "))
        CT = sistema.Cronograma(nome_tarefa, desc, False)
        CT.cadastrar_inf()
        
    if user == 3:
        user_admin = int(input("Digite o ID que será apagado: "))
        TG.excluir_tarefa(user_admin)
    
    if user == 4:
        id_inf = int(input("ID que será editado: "))
        
        TG.modificador(id_inf)
    
    elif user == 5:
        id_mod = int(input("Precisamos do ID: "))
        status_bd = str(input("digite 'v' para mudar o status para completo: ").upper().strip())
        TG.atualizar_status(id_mod, status_bd)
    
    if user == 6:
        usuario = str(input("Deseja sair? S/N ").upper().strip())
        if usuario in "S":
            print("FINALIZANDO...")
            break
        else:
            print("Vamos continuar os trabalhos!!!")