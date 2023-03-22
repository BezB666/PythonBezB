import googletrans

# Пользователь вводит любое слово и затем пытается угадать язык, на который оно переведено
startWord = input('Введите любое одно слово для перевода: ')
countAll = 4
countRight = 0

transWord = googletrans.Translator().translate(startWord, dest = 'en').text
print('Перевод слова: ' + transWord)
print('''Какой это язык? Введите цифру:
    #1 - английский
    #2 - французский
    #3 - немецкий
    #4 - испанский''')
userReply = input()

if userReply == '1':
    countRight += 1
    print('Правильно')
else:
    print('Неправильно')
print('Следующий язык!')

transWord = googletrans.Translator().translate(startWord, dest = 'de').text
print('Перевод слова: ' + transWord)
print('''Какой это язык? Введите цифру:
    #1 - английский
    #2 - французский
    #3 - немецкий
    #4 - испанский''')
userReply = input()

if userReply == '3':
    countRight += 1
    print('Правильно')
else:
    print('Неправильно')
print('Следующий язык!')

transWord = googletrans.Translator().translate(startWord, dest = 'fr').text
print('Перевод слова: ' + transWord)
print('''Какой это язык? Введите цифру:
    #1 - английский
    #2 - французский
    #3 - немецкий
    #4 - испанский''')
userReply = input()

if userReply == '2':
    countRight += 1
    print('Правильно')
else:
    print('Неправильно')
print('Следующий язык!')

transWord = googletrans.Translator().translate(startWord, dest = 'es').text
print('Перевод слова: ' + transWord)
print('''Какой это язык? Введите цифру:
    #1 - английский
    #2 - французский
    #3 - немецкий
    #4 - испанский''')
userReply = input()

if userReply == '4':
    countRight += 1
    print('Правильно')
else:
    print('Неправильно')


print('Ты ответил правильно на ' + str(countRight) + ' из ' + str(countAll) + ' вопросов')
