# Раздел 3
# Условие задачи:
# Написать приложение, цель которого — считать содержимое файла и подсчитывать количество уникальных буквенных слов
# (то есть слов, состоящих только из букв) в файлах, названия которых может вводить пользователь.
# Требования к программной реализации:
# При запуске приложения из консоли пользователь должен получать строку ввода для команды.
# Ему должны быть доступны следующие команды:
# 1) load filename.txt — загрузить слова из файла filename.txt;
# 2) wordcount червяк — отобразить число раз, которое программа встретила слово «червяк» в загруженных файлах;
# 3) clear-memory — очистить все данные о прочитанных словах из памяти.

class App:
    words = {}
    command_exit = False

    def __init__(self):
        words = {}

    def greet(self):
        print('Подсчет уникальных слов в текстовых файлах.\n'
              'Комманды:\n'
              '1) load filename.txt — загрузить слова из файла filename.txt;\n'
              '2) wordcount червяк — отобразить число раз, которое программа встретила слово «червяк» в загруженных файлах;\n'
              '3) clear-memory — очистить все данные о прочитанных словах из памяти.\n'
              '4) exit - для выхода из программы')

    def loop(self):
        while not self.command_exit:
            command = input('Введите комманду: ')
            cmd = command.split(' ')
            if 'load' in cmd:
                if cmd[1][-4:] == '.txt':
                    self.load_file(cmd[1])
                else:
                    print(f'Файл "{cmd[1]}" не является именем txt файла\n'
                          f'Убедитесь, что в имени файла нет пробелов и введите его корректно в формате "filename.txt"')
            elif 'wordcount' in cmd:
                self.word_count(cmd[1])
            elif 'clear-memory' in cmd:
                self.clear()
            elif 'exit' in cmd:
                self.command_exit = True
            elif 'help' in cmd:
                self.greet()
            else:
                print(f'Комманда не распознана')
                self.greet()

    def load_file(self, filename):
        words = self.words
        with open(filename, 'r', encoding='UTF-8') as file:
            content = file.read()
            lst = list(content.split(' '))
            for word in lst:
                if word.isalpha():
                    try:
                        words[word.lower()] += 1
                    except KeyError:
                        words[word.lower()] = 1
        print(self.words)
        print(f'Слова из файла {filename} добавлены')

    def word_count(self, word):
        print(f'Слово {word} встречается {self.words[word]} раз.')

    def clear(self):
        self.words = {}
        print(f'Данные очищены')

    def start(self):
        self.greet()
        self.loop()


app = App()
app.start()
