arquivo_contatos = open('Data/contatos-escrita.csv', encoding='latin_1', mode='a+')

contatos = ['13,Ny,ny@gmail.com.br\n',
            '14,Khyria,khyria@gmail.com.br\n',
            '15,GiSASS,giscss@gmail.com.br\n'
            '16,Felipe,feliper@gmail.com.br\n']

for contato in contatos:
    arquivo_contatos.write(contato)

arquivo_contatos.flush()

arquivo_contatos.seek(22)
arquivo_contatos.write('14,Khyria,khyria@gmail.com.br\n'.upper())
arquivo_contatos.flush()
arquivo_contatos.seek(0)

for linha in arquivo_contatos:
    print(linha)


input('Pressione Enter para encerrar o programa!')

