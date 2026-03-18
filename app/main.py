class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        cost = car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0.0
        for car in cars:
            # Apenas lavamos carros que estão mais sujos do que o poder de lavagem da máquina
            if car.clean_mark < self.clean_power:
                # 1. Calculamos o preço e somamos aos ganhos do dia
                total_income += self.calculate_washing_price(car)
                # 2. Lavamos o carro de facto (atualizamos o nível de limpeza dele)
                self.wash_single_car(car)
        
        # A tarefa pede para retornar o rendimento arredondado a 1 casa decimal
        return round(total_income, 1)

    def rate_service(self, rate: int) -> None:
        # Para calcular a nova média, primeiro descobrimos o valor total dos votos antigos
        total_score = self.average_rating * self.count_of_ratings
        
        # Somamos mais uma pessoa ao total de avaliadores
        self.count_of_ratings += 1
        
        # Calculamos a nova média e atualizamos o atributo (arredondado a 1 casa)
        self.average_rating = round((total_score + rate) / self.count_of_ratings, 1)
