
class CapitalCity:
    def show_city(self, cityname):
        print("The Capital City name is ",cityname)
    

class MetropolitanCity(CapitalCity):
    def __init__(self, cityname):
        super().show_city(cityname)

    def show_city(self, cityname):
        print("The Metropolitan City name is ",cityname)


obj=MetropolitanCity("Bangalore")
obj.show_city("Delhi")