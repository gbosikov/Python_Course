class Warehouse():
    """Склад оргтехники"""
    def __init__(self):
        self.store = dict()

    def add(self, **kwargs):
        a = {
            self.last_id+1:{
                'name': kwargs['name'],
                'count': self.clear_int_str(kwargs['count'])
            }
        }
        self.store.update(a)

    def use(self, name, to_department):
        for idx, val in self.store.items():
            if name == val['name']:
                val['user'] = to_department

    def show(self):
        """показатьт склад"""
        print(self.store)

    @property
    def last_id(self):
        if not self.store:
            return 0
        else:
            return sorted(self.store.items(), key=lambda x: x[0])[-1][0]

    @staticmethod
    def clear_int_str(str: str = '') -> int:
        try:
            i = int(str)
        except:
            return 0
        return i if i > 0 else 0


class Equipment():
    """Оргтехника"""
    def __init__(self):
        pass


class Printer(Equipment):
    """принтер"""
    def __init__(self):
        super().__init__()
        pass


class Scaner(Equipment):
    """сканер"""
    def __init__(self):
        super().__init__()
        pass


class Xerox(Equipment):
    """ксерокс"""
    def __init__(self):
        super().__init__()
        pass


w = Warehouse()
w.add(name='принтер', count=1)
w.use(name='принтер', to_department='HR')
print(w.last_id)
w.show()
