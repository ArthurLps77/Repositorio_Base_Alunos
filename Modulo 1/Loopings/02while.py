bombons = 10

while bombons > 0: # enquanto bombons > 0 o while continua executando
    print(f'Eu tenho {bombons} bombons.')
    bombons -= 1 # diminui um bombom
    print(f'Comi 1 e fiquei com {bombons} bombons.') # informa a quantidade
    if bombons == 0:
        print('Acabaram os bombons')