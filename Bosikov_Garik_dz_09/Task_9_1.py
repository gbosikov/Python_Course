from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = ''

    def running(self):
        while True:
            self.__color = 'red'
            print(f'{self.__color} 4 sec')
            sleep(4)

            self.__color = 'yellow'
            print(f'{self.__color} 3 sec')
            sleep(2)

            self.__color = 'green'
            print(f'{self.__color} 2 sec')
            sleep(3)


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
