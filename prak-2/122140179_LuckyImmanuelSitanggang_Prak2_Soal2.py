def uppercase_decorator (function):
    def wrapper(self):
        func = function(self)
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

class MOBA:

    #Konstruktor
    def __init__(self,id,rank,diamond) :
        self.id = id
        self.rank = rank
        self.diamond = diamond

    def output (self):
        print (f"ID Player : {self.id} ")
        print (f"Rank saat ini : {self.rank}")
        print (f"Total Diamond : {self.diamond}")

    #Dekorator
    @uppercase_decorator
    def showrank (self):
        return f"{self.rank}"
    
    #Destruktor
    def __del__ (self):
        print(f"objek {self.id} dihapus")


player1 = MOBA(2104,"Mythic",20000)

player1.output()

rank_plyr1 = MOBA.showrank

print(player1.showrank())