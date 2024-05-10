import random

def pedra_papel_tesoura() :
  user = input("escolha pedra,papel,tesoura")
  computer = random.choice(['pedra','papel','tesoura'])
  print(f"josebot escolheu {computer}")

  if user==computer:
   return "empate"

  elif (user == 'pedra' and computer=='tesoura' or (user == 'papel' and computer =="pedra")) or (user == 'tesoura' and computer=="papel"):
    return 'você ganhou!'

  else:
    return "vc perdeu"

print(pedra_papel_tesoura()) 