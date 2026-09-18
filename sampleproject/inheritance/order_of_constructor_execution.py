class AA:
    def __init__(self):
        print("It is AA class Constructor!!")

class BB(AA):
    def __init__(self):
        super().__init__()
        print("It is BB class Constructor!!")

class CC(BB):
    def __init__(self):
        super().__init__()
        print("It is CC class Constructor!!")

obj=CC()