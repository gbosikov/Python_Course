class Warehouse():
    def __init__(self):
        self.store = dict()

    def add(self, **kwargs):
        a = {
            self.last_id + 1: {
                'name': kwargs['name'],
                'count': kwargs['count']
            }
        }
        self.store.update(a)

    def use(self, name, to_department):
        for idx, val in self.store.items():
            if name == val['name']:
                val['user'] = to_department

    def show(self):
        print(self.store)

    @property
    def last_id(self):
        if not self.store:
            return 0
        else:
            return sorted(self.store.items(), key=lambda x: x[0])[-1][0]


class Equipment():
    """Оргтехника"""
    pass


class Printer(Equipment):
    """принтер"""
    pass


class Scanner(Equipment):
    """сканер"""
    pass


class Xerox(Equipment):
    """ксерокс"""
    pass
