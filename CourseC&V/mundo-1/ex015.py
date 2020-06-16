km = float(input('How many kilometers do you walked? Km '))
days = int(input('How many days do you rented? '))
totValueDays = days * 60
totValueKms = km * 0.15
total = totValueKms + totValueDays
print('Days with car: {}\nKilometers performed: {:.1f}km\nPrice per day: {:.2f}\nPrice per km: {:.2f}\n'
      'Total: R${:.2f}'.format(days, km, totValueDays, totValueKms, total))