from typing import List
from random import random

RED_ROSE_IMAGE_URL =    "https://dodo.ac/np/images/2/24/Red_Roses_NH_Inv_Icon.png"
PINK_ROSE_IMAGE_URL =   "https://dodo.ac/np/images/0/0c/Pink_Roses_NH_Inv_Icon.png"
BLACK_ROSE_IMAGE_URL =  "https://dodo.ac/np/images/0/01/Black_Roses_NH_Inv_Icon.png"


class Flower:
    pass

class Rose(Flower):
    pass

class RedRose(Rose):
    image:str = RED_ROSE_IMAGE_URL

class PinkRose(Rose):
    image:str = PINK_ROSE_IMAGE_URL

class BlackRose(Rose):
    image:str = BLACK_ROSE_IMAGE_URL

class Possibility():
    flower:Flower
    percent:int

    def __init__(self, flower, percent) -> None:
        self.flower = flower
        self.percent = percent


class Possibilities(): #TODO find a better name ? Hybridization ?
    flowers:List[Possibility] 

    def __init__(self, flowers:List[Possibility]) -> None:
        self.flowers = flowers

    def images(self):
        return [possibility.flower.image for possibility in self.flowers]

    
    def produce(self):
        rand = random()
        percent_cumul = 0
        winner_flower = None
        for flower_probabilty in self.flowers:
            percent_cumul += flower_probabilty.percent
            if rand < (percent_cumul / 100):
                winner_flower = flower_probabilty.flower
                break
        
        return winner_flower


def hybridize(flower1, flower2):
    if isinstance(flower1, RedRose) and isinstance(flower2, RedRose):
        return Possibilities([
            Possibility(flower=PinkRose(),  percent=25), 
            Possibility(flower=BlackRose(), percent=25)
        ])