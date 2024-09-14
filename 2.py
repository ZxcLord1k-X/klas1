class Title():
    def __init__(self, title_text, x_num, y_num):
        self.title = title_text
        self.x = x_num
        self.y = y_num
        self.appearance = True
    def hide(self):
        self.appearance = False
        print(self.title, 'приховано')

    def show(self):
        self.appearance = True
        print(self.title, 'показано')
    def print_status(self):
        print('Інформація про напис:')
        print('Текст:', self.title)
        print('координати:', self.title, self.x, self.y)
        print('видимість', self.appearance)


ok_button = Title('ok', 150, 50)
ok_button.print_status()
ok_button.hide()
ok_button.print_status()
ok_button.show()
