import re

def add_new_contact(agenda):
    print("\nAdicionar Contato:")
    name = input("Nome: ")
    telephone = input("Telefone: ")
    while not re.match(r'^\d{11}$', telephone):
        print("Número de telefone inválido. O número deve conter 11 dígitos.")
        telephone = input("Telefone: ")
    email = input("Email: ")
    while not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        print("Email inválido.")
        email = input("Email: ")
    favorite = input("Favorito (S/N): ").upper()

    if favorite == 'S':
        favorite = True
    else:
        favorite = False

    contact = {
        'Nome': name,
        'Telefone': telephone,
        'Email': email,
        'Favorito': favorite
    }

    agenda.append(contact)
    print("Contato adicionado com sucesso!")

def list_contacts(agenda):
    print("\nLista de Contatos:")
    if not agenda:
        print("A agenda está vazia.")
    else:
        for i, contact in enumerate(agenda, start=1):
            print(f"Contato: {i}:")
            print(f"Nome: {contact['Nome']}")
            print(f"Telefone: {contact['Telefone']}")
            print(f"Email: {contact['Email']}")
            print(f"Favorito: {'Sim' if contact['Favorito'] else 'Não'}")
            print()

def list_favorite_contacts(agenda):
    print("\nLista de Contatos Favoritos:")
    favorite_contacts = [contact for contact in agenda if contact['Favorito']]
    
    if not favorite_contacts:
        print("Não há contatos favoritos.")
    else:
        for i, contact in enumerate(favorite_contacts, start=1):
            print(f"Contato {i}:")
            print(f"Nome: {contact['Nome']}")
            print(f"Telefone: {contact['Telefone']}")
            print(f"Email: {contact['Email']}")
            print()

def edit_contact(agenda):
    if not agenda:
        print("Não há contatos para editar.")
        return

    print("\nEditar Contato:")
    list_contacts(agenda)
    index = int(input("Digite o número do contato que deseja editar: ")) - 1

    if index < 0 or index >= len(agenda):
        print("Índice de contato inválido.")
        return

    contact = agenda[index]

    print("\nEditar Detalhes do Contato:")
    name = input(f"Novo Nome ({contact['Nome']}): ")
    telephone = input("Telefone: ")
    while not re.match(r'^\d{11}$', telephone):
        print("Número de telefone inválido. O número deve conter 11 dígitos.")
        telephone = input("Telefone: ")
    email = input("Email: ")
    while not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        print("Email inválido.")
        email = input("Email: ")
    is_favorite = contact['Favorito']
    favorite = input(f"Marcar como favorito? ({'Sim' if is_favorite else 'Não'} - S/N): ").upper()

    if favorite == 'S':
        favorite = True
    else:
        favorite = False

    contact['Nome'] = name if name else contact['Nome']
    contact['Telefone'] = telephone if telephone else contact['Telefone']
    contact['Email'] = email if email else contact['Email']
    contact['Favorito'] = favorite

    print("Contato editado com sucesso!")

def remove_contact(agenda):
    if not agenda:
        print("Não há contatos para remover.")
        return

    print("\nRemover Contato:")
    list_contacts(agenda)
    index = int(input("Digite o número do contato que deseja remover: ")) - 1

    if index < 0 or index >= len(agenda):
        print("Índice de contato inválido.")
        return

    removed_contact = agenda.pop(index)
    print(f"Contato '{removed_contact['Nome']}' removido com sucesso!")

def show_options_list():
        print("Bem-vindo a AGENDA! Escolha uma opção:")
        print("1- Lista de contatos")
        print("2- Adicionar contato")
        print("3- Editar contato")
        print("4- Lista de contatos favoritos")
        print("5- Remover contato")


def main():
    agenda = []  # aqui se armazena os contatos da agenda sem haver um banco de dados

    while True:
        show_options_list()
        case = input("Digite o número da opção desejada: ")

        if case == '1':
            list_contacts(agenda)
        elif case == '2':
            add_new_contact(agenda)
        elif case == '3':
            edit_contact(agenda)
        elif case == '4':
            list_favorite_contacts(agenda)
        elif case == '5':
            remove_contact(agenda)
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
