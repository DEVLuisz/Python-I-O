import contatos_utils

try:
    # contatos = contatos_utils.csv_para_contatos('Data/contatos.csv')
    # contatos_utils.contatos_para_pickle(contatos, 'Data/contatos.p')
    # contatos = contatos_utils.pickle_para_contatos('Data/contatos.p')
    # contatos_utils.contatos_para_json(contatos, 'JSON/contatos.json')
    contatos = contatos_utils.json_para_contatos('JSON/contatos.json')

    for contato in contatos:
        print(f'{contato.id} -{contato.nome} -{contato.email}')

except FileNotFoundError:
    print('Arquivo não encontrado!')
except PermissionError:
    print('Sem permissão de escrita!')