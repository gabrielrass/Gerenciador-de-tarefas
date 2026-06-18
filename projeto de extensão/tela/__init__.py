#menu do programa
def visor():
    menu = {
        1: "Ver pessoas",
        2: "Cadastrar",
        3: "Buscar pessoas",
        4: "Editar pessoas",
        5: "Excluir pessoas",
        6: "Sair"
    }
    for k, v in menu.items():
        print(f"{k} - {v}")
    user = int(input("Digite sua opcao: "))
    if user in menu.keys():
        print(menu[user])