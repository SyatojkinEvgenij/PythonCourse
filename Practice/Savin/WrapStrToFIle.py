import tempfile

class WrapStrToFIle:
    def __init__(self):
        self._filepath = tempfile.mkstemp()

    @property
    def content(self):
        try:
            f = open(self._filepath[1])
        except FileNotFoundError:
            print('Файл еще не существует')
        else:
            f.read()
            f.close()

    @content.setter
    def content(self, value):
        f = open(self._filepath[1], 'w')
        f.write(value)

    @content.deleter
    def content(self):
        self._filepath = 'Файл удален'

t = WrapStrToFIle()
t.content