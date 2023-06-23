import random

print("Juego de piedra, papel o tijera")
opciones = ("tijera", "papel", "piedra")

computer_wins = 0
user_wins = 0

rounds = 1

while True:

  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)

  print('computer_wins', computer_wins)
  print('user_wins', user_wins)

  o_user = input('Piedra, Papel, Tijera: ')
  o_user = o_user.lower()

  if not o_user in opciones:
    print("Esa opción no es valida")
    continue

  o_pc = random.choice(opciones)
  o_pc = o_pc.lower()

  # Juego
  print("Usuario: " + o_user)
  print("pc: " + o_pc)

  turnos = 0

  if o_user == o_pc:
    print('Empate!')
  elif (o_user == "tijera" and o_pc == "piedra") or (
      o_user == "papel" and o_pc == "tijera") or (o_user == "piedra"
                                                  and o_pc == "papel"):
    computer_wins += 1
    print('Perdiste! :(')
  else:
    user_wins += 1
    print('Ganaste! :)')

  print()
  if computer_wins == 2:
    print('"El ganador es la computadora"')
    break
  if user_wins == 2:
    print('"El ganador es el Usuario"')
    break
  rounds += 1
