phrase = str(input('Type your phrase: ').upper().strip())
print('The letter "A" is in the phrase {} times.'.format(phrase.count('A')))
print('The letter "A" pops up through the first time in the position {} on the phrase.'.format(phrase.find('A') + 1))
print('The letter "A" pops up through the last time in the position {} on the phrase.'.format(phrase.rfind('A') + 1))
