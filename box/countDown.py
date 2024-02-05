import time

def countDown (t):
    while t:
        mins,secs = divmod(t,60)
        timer = '{:02}:{:02}'.format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        t -= 1
    print("Tempo esgotado!!")

t = input('Informe o tempo (em segundos):')
countDown(int(t))