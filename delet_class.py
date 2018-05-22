maximum_capacity_recbin = 70
maximum_capacity_package = 35
locate_inside = []


class RecycleBin:
    print('Памяти в корзине на данный момент: {}'.format(maximum_capacity_recbin))

    def delete_recbin(self, entered_by_user):
        global maximum_capacity_recbin
        if type(entered_by_user) == int:
            if (maximum_capacity_recbin - 10) <= 0:
                print('Место в корзине закончилось')
                return True
            else:
                maximum_capacity_recbin -= 10

        if type(entered_by_user) == str:
            if (maximum_capacity_recbin - 15) <= 0:
                print('Место в корзине закончилось')
                return True
            else:
                maximum_capacity_recbin -= 15
        print('Осталось {} памяти,'.format(maximum_capacity_recbin))


class Package:
    print('Памяти в пакете на данный момент: {}'.format(maximum_capacity_package))

    def delete_package(self, entered_by_user):
        global maximum_capacity_package
        if type(entered_by_user) == int:
            if (maximum_capacity_package - 10) <= 0:
                print('Место в пакете закончилось')
                return True
            else:
                maximum_capacity_package -= 10

        if type(entered_by_user) == str:
            if (maximum_capacity_package - 15) <= 0:
                print('Место в пакете закончилось')
                return True
            else:
                maximum_capacity_package -= 15
        print('Осталось {} памяти,'.format(maximum_capacity_package))


class SeizedWords:
    def locate(self, entered_by_user):
        locate_inside.append(entered_by_user)


def main():
    sorting = input('Введите куда положить ваше слово либо цифру (корзина / пакет): ')
    if sorting.lower() == 'корзина':
        while True:
            input_recycle_bin = input('Введите то, что надо удалить (слово / цифру): ')
            two = SeizedWords()
            two.locate(input_recycle_bin)
            if input_recycle_bin.isdigit():
                input_recycle_bin = int(input_recycle_bin)
            one = RecycleBin()
            if one.delete_recbin(input_recycle_bin):
                return

    if sorting.lower() == 'пакет':
        while True:
            input_package = input('Введите то, что надо положить в пакет (слово / цифру): ')
            two = SeizedWords()
            two.locate(input_package)
            if input_package.isdigit():
                input_package = int(input_package)
            one = Package()
            if one.delete_package(input_package):
                return


def conclusion():
    print('Изъятые слова / цифры: ', locate_inside)


if __name__ == '__main__':
    main()
    conclusion()
