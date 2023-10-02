import pytest
from typing import List
from random import random


class Flower:
    pass

class Rose(Flower):
    pass

class RedRose(Rose):
    pass

class PinkRose(Rose):
    pass

class BlackRose(Rose):
    pass

class Possibility():
    flower:Flower
    percent:int

    def __init__(self, flower, percent) -> None:
        self.flower = flower
        self.percent = percent

class Possibilities():
    flowers:List[Possibility]

    def __init__(self, flowers:List[Possibility]) -> None:
        self.flowers = flowers

    def produce(self):
        rand = random()
        percent_cumul = 0
        winner_flower = None
        for flower_probabilty in self.flowers:
            percent_cumul += flower_probabilty.percent
            #print(f"VVV is random {rand} < {percent_cumul / 100}")
            if rand < (percent_cumul / 100):
                #print(f"VVV Flower {flower_probabilty.flower.__class__.__name__} win !")
                winner_flower = flower_probabilty.flower
                break
        
        return winner_flower


def hybridize(flower1, flower2):
    if isinstance(flower1, RedRose) and isinstance(flower2, RedRose):
        #print("VVV Both flowers are Roses")
        return Possibilities([Possibility(PinkRose(), 25) , Possibility(BlackRose(), 25)])

class Test_red_rose_next_to_another_red_rose:

    def test_it_can_produce_pink_rose_and_black_rose(self):
        possibilities = hybridize(RedRose(), RedRose())

        assert 2 == len([f for f in possibilities.flowers if is_one_of_instance_of(f.flower, [PinkRose, BlackRose])])

    def test_both_two_roses_produce_have_25_percent_chance(self):

        possibilities = hybridize(RedRose(), RedRose())

        possibilities.flowers[0].percent = 25
        possibilities.flowers[1].percent = 25

    def test_produce_randomly_return_a_flower_based_on_possibilities_percent(self):

        possibilities = hybridize(RedRose(), RedRose())

        flower = possibilities.produce()
        print(f"VVV Flower {flower.__class__.__name__} win !")
        assert is_one_of_instance_of(flower, [PinkRose, BlackRose, None])


################### HELPERS ###################

def test_is_one_of_instance_of():
    assert is_one_of_instance_of(RedRose(), [RedRose, PinkRose])
    assert is_one_of_instance_of(RedRose(), [PinkRose, RedRose])
    assert not is_one_of_instance_of(RedRose(), [PinkRose, BlackRose])

def is_one_of_instance_of(obj:object, types:list):
    instance_found = False
    for type in types:
        if obj == type or isinstance(obj, type):
            instance_found = True
            break

    return instance_found


