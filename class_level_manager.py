from class_level_one import LevelOne
from class_level_two import LevelTwo
from class_level_three import LevelThree

class LevelManager:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.levels = {1:LevelOne, 2:LevelTwo, 3:LevelThree}
    
    def get_levels(self, name_level):
        return self.levels[name_level](self.screen)
