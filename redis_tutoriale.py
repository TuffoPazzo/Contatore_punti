import redis 

r = redis.Redis(
  host='redis-17800.c55.eu-central-1-1.ec2.cloud.redislabs.com',
  port=17800,
  password='R0xoNRNdiq8KTklL7Y4mfzeOVq40btc4')

r.set('Piastrellisti_team', 0)
r.set('Idraulici_team', 0)

partita = True 

while partita:

  squadra = int(input('Che squadra ha segnato? [Inserisci 0 per: Piastrellisti_Team / Inserisci 1 per: Idraulici_team]'))
  punto = int(input('come ha segnato? [Tiro libero: 0; Normale: 1; Da 3: 2]'))
  stato_partita = input('La partita è finita? [si/no]')
  if squadra == 0:
    if punto == 0:
      r.incr('Piastrellisti_team')
    elif punto == 1:
      r.incrby('Piastrellisti_team', 2)
    elif punto == 2:
      r.incrby('Piastrellisti_team', 3)
  else:
    if punto == 0:
      r.incr('Idraulici_team')
    elif punto == 1:
      r.incrby('Idraulici_team', 2)
    elif punto == 2:
      r.incrby('Idraulici_team', 3)
  if stato_partita == 'si':
    partita = False 


print('Piastrellisti_team: ' + r.get('Piastrellisti_team').decode('utf-8'))
print('Idraulici_team: ' + r.get('Idraulici_team').decode('utf-8'))

