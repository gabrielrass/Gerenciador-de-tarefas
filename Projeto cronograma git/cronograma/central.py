import sistema
print("Bem-Vindo ao sistema de gerenciamento de tarefas!!!")
interface = ("Ver tarefas", "Cadastrar tarefas", "Excluir tarefas", "Modificar tarefas", "Sair")
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
    
    if user == 5:
        usuario = str(input("Deseja sair? S/N ").upper().strip())
        if usuario in "S":
            print("FINALIZANDO...")
            break
        else:
            print("Vamos continuar os trabalhos!!!")