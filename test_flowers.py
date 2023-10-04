import pytest
from flowers import *
from helper import is_one_of_instance_of
from markdown_writter import *

#python -m pytest test_flowers.py

@pytest.fixture
def doc(scope="module"):
    doc = MarkdownWritter()
    yield doc
    doc.dump_in_file("documentation/test_flowers.md")


class Test_red_rose_next_to_another_red_rose:

    def test_it_can_produce_pink_rose_or_black_rose(self, doc):
        f1 = RedRose()
        f2 = RedRose()

        doc.log(f"given {doc.img(f1.image)} and {doc.img(f2.image)}")
        
        possibilities = hybridize(f1, f2)

        doc.log(f"- it can gives {'or'.join([doc.img(image) for image in possibilities.images()])}")

        assert 2 == len(possibilities.possibilities)
        assert 1 == len([f for f in possibilities.possibilities if isinstance(f.flower, PinkRose)])
        assert 1 == len([f for f in possibilities.possibilities if isinstance(f.flower, BlackRose)])

    
    def test_both_two_roses_produced_have_25_percent_chance(self):
        possibilities = hybridize(RedRose(), RedRose())

        possibilities.possibilities[0].percent = 25
        possibilities.possibilities[1].percent = 25

    def test_produce_ramdomly_return_a_flower_based_on_possibilities_percent(self):
        possibilities = hybridize(RedRose(), RedRose())

        flower = possibilities.produce()
        assert is_one_of_instance_of(flower, [PinkRose, BlackRose, None])


