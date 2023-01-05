contato_shrieker = '12,Shrieker,shrieker@shrieker.com.br\n'
contato_khyria = '13,Khyria,khyria@khyria.com.br\n'

with open('Data/contatos-concorrencia.csv', encoding='latin_1', mode='w') as arquivo1:
    arquivo1.write(contato_shrieker)

with open('Data/contatos-concorrencia.csv', encoding='latin_1', mode='a') as arquivo2:
    arquivo2.write(contato_khyria)