print('Bem vindo ao calculador de gorgeta.')
bill = float(input("Qual foi o total da conta? $"))
tip = int(input("Quanto de gorgeta você deseja dar? 10, 12 ou 15? "))
people = int(input("Em quantas pessoas você deseja dividir a conta? "))
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Cada pessoa terá que pagar ${final_amount}")

