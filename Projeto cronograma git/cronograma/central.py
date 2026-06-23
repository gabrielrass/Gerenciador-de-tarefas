import sistema
print("Bem-Vindo ao sistema de gerenciamento de tarefas!!!")
interface = ("Ver tarefas", "Cadastrar tarefas", "Excluir tarefas", "Modificar tarefas")
TG = sistema.Cronograma()
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
        TG.excluir_tarefa_tarefas(user_admin)
    
    if user == 4:
        id_inf = int(input("ID que será editado: "))
        novo_nome = str(input("Novo nome da tarefa: "))
        nova_desc = str(input("Nova descrição: "))
        
        TG.modificador(id_inf, novo_nome, nova_desc)
    break