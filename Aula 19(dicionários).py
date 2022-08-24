pessoas={'nome':'Gabriel','idade':'20','estuda':'unifacs'}
#print(pessoas.keys()
#print(pessoas.values())
#print(pessoas.items())
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos e estuda na {pessoas["estuda"]}')
#for k,v in pessoas.items():
    #print(f'{k}={v}')
estado={}
brasil=[]
for c in range(0,3):
    estado['uf']=str(input('unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem valor {v}')
