

playerZ, roundZ = 'Not defined' , 'Not defined'
c = list()

class Conditions():
    def __init__(self, jugadores, rounds):
        self.q_players = int(jugadores)
        self.q_rounds = int(rounds)
    
    def __str__(self):
        return 'Cantidad de jugadores: ' + str(self.q_players) + ', cantidad de rounds: '  + str(self.q_rounds)

def q_cond(p, r):
    if p == 1:
        global playerZ
        
        try:
            global playerZ
            playerZ = int(input('Ingrese un numero de JUGADORES: '))
        except Exception:
            print('\nValor ingresado no valido.')
            q_cond(1,0)
        else:
            playerZ = int(playerZ)
            try:
                if playerZ <= 0: # en caso SER numerico, verifica qe sea mayor a 0
                    0/0
            except Exception:
                print('\nValor ingresado no valido.')
                q_cond(1,0)
            else:
                print('yay!')
                c.append(int(playerZ))
    elif r == 1:
        global roundZ
        
        try:
            global roundZ
            roundZ = int(input('Ingrese un numero de RONDAS: '))
        except Exception:
            print('\nValor ingresado no valido.')
            q_cond(0,1)
        else:
            roundZ = int(roundZ)
            try:
                if roundZ <= 0: # en caso SER numerico, verifica qe sea mayor a 0
                    0/0
            except Exception:
                print('\nValor ingresado no valido.')
                q_cond(0,1)
            else:
                print('yay!')
                c.append(int(roundZ))

def set_conditions():
    q_cond(1, 0)
    q_cond(0, 1)
