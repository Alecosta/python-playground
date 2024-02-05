## Teste usando o Codeium

# prepare uma funcao para gerar um despertador
def despertador(hora):
    import time
    while True:
        if time.strftime("%H:%M") == hora:
            print("Hora de despertar!")
            break

# utilize essa funcao passando a hora de despertar como argumento por exemplo 10:40
despertador('10:39')
