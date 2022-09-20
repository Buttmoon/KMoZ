import json
from random import randint

class View:
    portraitWidth: int
    landscapeWidth:int
    name: str
    def __init__(self, data:dict) -> None:
        self.portraitWidth =  data["portraitWidth"]
        self.landscapeWidth =  data["portraitWidth"]
        self.name =  data["name"]
        pass
class Viewport:
    all = []
    def __init__(self) -> None:
        jsonfile =  open("./viewport/__viewports__.json", encoding="UTF-8")
        list = json.load(jsonfile)
        self.all = [list[i] for i in list]
        pass
    def get_random_mobile(self) -> View:
        rand_index = randint(0, len(self.all)) 
        return View(self.all[rand_index])