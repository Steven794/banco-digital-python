import time
class Banco:
  def __init__(self, saldo: float, nome_titular: str):
    self.nome_titular = nome_titular
    self.saldo = saldo
    self.historico_transacao = []
    self.historico_transacao.append(f"Depósito: +R${self.saldo:.2f}")

  def exibir_extrato(self):
    print(f"\n--- Extrato de {self.nome_titular} ---")
    if not self.historico_transacao:
       print("Nenhuma transação realizada.")
    else:
       print("\n".join(f"•{extrato}" for extrato in self.historico_transacao))

  def sacar(self):
     while True:
        print(f"Você possui R$ {self.saldo:.2f} depositado")
        try:
            sacar = float(input("Que valor que você gostaria de sacar? "))
        except ValueError:
            print("❌Entrada Inválida! Digite um valor.")
            continue
        else:
         if sacar > self.saldo:
            print("Infelizmente você não possui saldo suficiente para sacar!")
            continue
         elif sacar <= 0:
            print("❌ Digite um valor maior que zero!")
            continue
         else:
            self.saldo -= sacar
            self.historico_transacao.append(f"Saque: -R${sacar:.2f}")
            print(f"Saldo Atual R$ {conta_banco.saldo:.2f}")
            while True:
               try:
                  escolha2 = int(input("Gostaria de fazer outro saque?\n Se Sim digite (1)\n Se Não digite (2)"))
                  time.sleep(1)
                  if escolha2 == 1:
                     break
                  elif escolha2 == 2:
                     print("Obrigado por usar o Banco Digital Python!")
                     return
                  else:
                     print("Digite 1 para (Sim) ou 2 para (Não)")
                     continue
               except ValueError:
                  print("❌Entrada Inválida! Digite 1 ou 2.")
                  continue
  
  def depositar(self):
    while True:
       print(f"Você possui R$ {self.saldo:.2f} depositado")
       try:
          deposito = float(input("Quanto você gostaria de depositar? "))
       except ValueError:
         print("❌Entrada Inválida! Digite um valor.")
         continue
       else:
         if deposito <= 0:
            print("❌ Digite um valor maior que zero!")
            continue
         else:
            self.saldo += deposito
            self.historico_transacao.append(f"Depósito: +R${deposito:.2f}")
            print(f"Saldo Atual R$ {self.saldo:.2f}")
            while True:
               try:
                  escolha1 = int(input("Gostaria de fazer outro deposito?\n Se Sim digite (1)\n Se Não digite (2)"))
                  time.sleep(1)
                  if escolha1 == 1:
                     break
                  elif escolha1 == 2:
                     print("Obrigado por usar o Banco Digital Python!")
                     return
                  else:
                     print("Digite 1 para (Sim) ou 2 para (Não)")
                     continue
               except ValueError:
                  print("❌Entrada Inválida! Digite 1 ou 2.")
                  continue
    
#=================================
#Fluxo Principal 
#=================================
print("Bem-Vindo ao Banco Digital Python!")
nome = input("\nDigite o nome do titular: ")
while True:
   try:
      deposito_abertura = float(input("\nColoque um valor para o deposito de abertura: "))
      if deposito_abertura <= 0:
         print("❌ O valor de abertura não pode ser negativo e nem zero.")
         continue
      break
   except ValueError:
      print("\n❌Entrada inválida! Digite um valor.")
      continue
conta_banco = Banco(nome_titular=nome, saldo=deposito_abertura)

while True:
   print("\n|[1] Depositar\n|[2] Sacar \n|[3] Ver Extrato \n|[4] Sair")
   time.sleep(1)
   try:
      opcao = int(input("Digite um número conforme as opções: "))
   except ValueError:
      print("❌Entrada inválida! Digite um números descritos nas opções.")
      continue
   
   if opcao == 1:
      conta_banco.depositar()
   
   elif opcao == 2:
      conta_banco.sacar()
   
   elif opcao == 3:
      conta_banco.exibir_extrato()
   else:
      print("Obrigado por usar o Banco Digital Python!")
      break
