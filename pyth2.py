def kda_counter(kills, deaths, assists):
    if deaths == 0 :
        return "Отличный KDA!"
    return round((kills + assists) / deaths, 2)

class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"Агент {self.name} играет роль {self.role}"

class Duelist(Agent):
    def __init__(self, name):
        super().__init__(name, "Дуэлянт")
    def ultimate(self):
        return f"{self.name} активирует ульту и выигрывает раунд"
    
class Santinel(Agent):
    def __init__(self, name):
        super().__init__(name, "Страж")
    def ultimate(self):
        return f"{self.name} активирует ульту и воскрешает союзника"
    
if __name__ == "__main__":
    jett = Duelist("Джетт")
    print(jett)
    print(jett.ultimate())

    sage = Santinel("Сага")
    print(sage)
    print(sage.ultimate())

kills, deaths, assists = 10, 2, 5
print(f"KDA: {kda_counter(kills, deaths, assists)}")