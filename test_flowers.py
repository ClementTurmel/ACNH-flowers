import pytest
from flowers import *
from helper import is_one_of_instance_of
from markdown_writter import *

#python -m pytest test_flowers.py

@pytest.fixture(scope="module")
def doc():
    doc = MarkdownWritter()
    yield doc
    doc.dump_in_file("documentation/test_flowers.md")


@pytest.fixture(scope="module")
def hybridization(doc):
    f1 = RedRose()
    f2 = RedRose()
    doc.log(f"given {doc.img(f1.image)} and {doc.img(f2.image)}")
    return hybridize(f1, f2)

def test_it_can_produce_pink_rose_or_black_rose(hybridization, doc):

    doc.log(f"it can gives {'or'.join([doc.img(image) for image in hybridization.images()])}")

    assert 2 == len(hybridization.possibilities)
    assert 1 == len([f for f in hybridization.possibilities if isinstance(f.flower, PinkRose)])
    assert 1 == len([f for f in hybridization.possibilities if isinstance(f.flower, BlackRose)])


def test_both_two_roses_produced_have_25_percent_chance(hybridization, doc):

    hybridization.possibilities[0].percent = 25
    hybridization.possibilities[1].percent = 25
    doc.log(f"with probability {','.join([f'{doc.img(possibility.flower.image)}{possibility.percent}%' for possibility in hybridization.possibilities])}")

def test_produce_ramdomly_return_a_flower_based_on_possibilities_percent(hybridization):

    flower = hybridization.produce()
    assert is_one_of_instance_of(flower, [PinkRose, BlackRose, None])


