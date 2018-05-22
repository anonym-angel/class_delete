import math


class Distribution:
    input_of_numbers = input('Введите количество чисел, через пробел (max 3): ')
    form_input_of_numbers = input_of_numbers.split(' ')

    def draw(self):
        if len(self.form_input_of_numbers) == 1:
            one = BuildSquare()
            one.build_sq()

        elif len(self.form_input_of_numbers) == 2:
            two = BuildTriangle()
            two.build_tr()
        elif len(self.form_input_of_numbers) == 3:
            three = BuildRectangle()
            three.build_re()


class BuildSquare(Distribution):
    def build_sq(self):
        print("""
            ------------
            |          |
            |          |
            |          |
            |          |
            ------------
        """)
        transformation = [int(item) for item in self.form_input_of_numbers]
        area_of_the_figure = transformation[0] ** 2
        perimeter = 4 * transformation[0]
        print('Площадь квадрата = {}'.format(area_of_the_figure))
        print('Периметр квадрата = {}'.format(perimeter))


class BuildTriangle(Distribution):
    def build_tr(self):
        print("""
            ---------------------
            |                   |
            |                   |
            |                   |
            ---------------------
        """)
        transformation = [int(item) for item in self.form_input_of_numbers]
        area_of_the_figure = transformation[0] * transformation[1]
        perimetr = (transformation[0] + transformation[1]) * 2
        print('Площадь прямоугольника = {}'.format(area_of_the_figure))
        print('Периметр прямоугольника = {}'.format(perimetr))


class BuildRectangle(Distribution):
    def build_re(self):
        print("""        
                 /\.
                /  \.
               /    \.
              /      \.
             /        \.
            /          \.
            ------------
        """)
        transformation = [int(item) for item in self.form_input_of_numbers]
        perimetr = transformation[0] + transformation[1] + transformation[2]
        area_of_the_figure = math.sqrt(perimetr*(perimetr - transformation[0])*
                                       (perimetr - transformation[1])*(perimetr - transformation[2]))
        print('Площадь треугольника по формуле Герона = {}'.format(area_of_the_figure))
        print('Периметр треугольника = {}'.format(perimetr))


if __name__ == '__main__':
    a = Distribution()
    a.draw()
