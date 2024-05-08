import random


catch_to_win = int(input('''Elige una opcion:
1. Muerte suvita, una de una
2. La comun, el que gane 2 de 3
3. El que gane 3 de 5
'''))

wins_to_finish = 0

if catch_to_win == 1:
  wins_to_finish = 1
elif catch_to_win == 2:
  wins_to_finish = 2
else:
  wins_to_finish = 3

# print(type(catch_to_win), catch_to_win)


# print(computer_option)



ronda = 0

  # print('opcion valida:', user_option)

def choose_option():

  options = ('piedra', 'papel', 'tijera')

  computer_option = random.choice(options)

  user_option = input('piedra, papel o tijera?').strip().lower()
  if user_option not in options:
    print('Tu opcion no es valida')
    user_option = input('piedra, papel o tijera?').strip().lower()
  else: 
    print('ronda =>')

  return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    if computer_option == 'piedra':
      if user_option == 'piedra':
        print('Empate, la computadora saco ', computer_option, ' y tu ', user_option)        
      elif user_option == 'papel':
        print('Ganaste a, la computadora saco ', computer_option, ' y tu ', user_option)
        user_wins += 1        
      else:
        print('Perdiste, la computadora saco ', computer_option, ' y tu ', user_option)
        computer_wins += 1
      return user_wins, computer_wins


    elif computer_option == 'papel':
      if user_option == 'papel':
        print('Empate, la computadora saco ', computer_option, ' y tu ', user_option)       
      elif user_option == 'tijera':
        print('Ganaste b, la computadora saco ', computer_option, ' y tu ', user_option)
        user_wins += 1   
      else:
        print('Perdiste, la computadora saco ', computer_option, ' y tu ', user_option)
        computer_wins += 1
      return user_wins, computer_wins



    else:
      if user_option == 'tijera':
        print('Empate, la computadora saco ', computer_option, ' y tu ', user_option) 
      elif user_option == 'priedra':
        print('Ganaste c, la computadora saco ', computer_option, ' y tu ', user_option)
        user_wins += 1
      else:
        print('Perdiste, la computadora saco ', computer_option, ' y tu ', user_option)
        computer_wins += 1
    return user_wins, computer_wins


def run_game():
  user_wins = 0
  computer_wins = 0


  while user_wins < wins_to_finish and computer_wins < wins_to_finish:

    user_option, computer_option = choose_option()

    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)


  print('El resultado final fue: Usuario ', user_wins, ', Computadora ', computer_wins)

run_game()