print('An annoying questionaire.')
print('-------------------------')
print()
a = input('What are you interested in?: ')
print()
if a.lower() == 'music':
  b = input('What Type of Music do you enjoy?: ')
  if b.lower() == 'gospel':
    print()
    c = input('What type of gospel music do you enjoy?: ')
    print()
elif a.lower() == 'food':
  b = input('Do you mind telling me your favourite food?: ')
  print()
  if b.lower() == 'rice':
    c = input('Do you prefer stew or jollof?: ')
    print()
    if c.lower() == 'stew':
      print('\033[32mYou are a bad guy no cap😂\033[0m')
      print()
    elif c.lower() == 'jollof':
      print('\033[33mOmoh! you sabi better thing no cap!\033[0m')
      print()
    else:print('Goodbye block head!')
else:
  print('Why do you not want to talk? ')
      
    