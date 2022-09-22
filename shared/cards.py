class Card(object):
    def __init__(self):
        self.id = -1
        self.power = -1
        self.name = "Invalid"
        self.description = "Invalid"
        
    def played(self, player):
        pass
    
    def discarded(self, player):
        pass
    
    def answer(self, player, answer):
        pass
    
class Assassin(Card):
    def __init__(self):
        super().__init__()
        self.id = 0
        self.power = 0
        self.name = "Assassin"
        self.description = "If a player targets you with a Guard, you eliminate them and discard this card."
    
    def played(self, player):
        pass

    def discarded(self, player):
        pass

    def answer(self, player, answer):
        pass
    
class Guard(Card):
    def __init__(self):
        super().__init__()
        self.id = 1
        self.power = 1
        self.name = "Guard"
        self.description = "Guess a player's non guard card. If you are correct, that player is eliminated."
        
    def played(self, player):
        target = player.select_player(False)
        return "!GUARD$" + str(target) + "$" + str(player.player_id)
    
    def discarded(self, player):
        pass
    
    def answer(self, player, answer):
        if str(answer) == "!CORRECT":
            return True
        else:
            return False
    
class Priest(Card):
    def __init__(self):
        super().__init__()
        self.id = 2
        self.power = 2
        self.name = "Priest"
        self.description = "Look at another player's card."
        
    def played(self, player):
        target = player.select_player(False)
        return "!PRIEST$" + str(target) + "$" + str(player.player_id)
    
    def discarded(self, player):
        pass
    
    def answer(self, player, answer):
        return answer
    
class Baron(Card):
    def __init__(self):
        super().__init__()
        self.id = 3
        self.power = 3
        self.name = "Baron"
        self.description = "Compare hands with another player. The player with the least power is eliminated."
        
    def played(self, player):
        target = player.select_player(False)
        return "!BARON$" + str(target) + "$" + str(player.player_id)
    
    def discarded(self, player):
        pass
    
    def answer(self, player, answer):
        outcome = str(answer).split("$")[1]
        
        if(outcome == "!LOSE"):
            player.lost()
            
        return answer


card_dict = {
            #0: {"card": Assassin, "count": 1, "image": "./images/guard.jpg"},
            1: {"card": Guard, "count": 5, "image": "./images/guard.jpg"},
            #2: {"card": Priest, "count": 2, "image": "./images/baron.jpg"},
            3: {"card": Baron, "count": 2, "image": "./images/baron.jpg"},
        }