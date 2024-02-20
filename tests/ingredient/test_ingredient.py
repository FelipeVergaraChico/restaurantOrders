from src.models.ingredient import Ingredient, Restriction


# Req 1
def test_ingredient():
    sushi = Ingredient("sushi")
    s2 = Ingredient("sushi")
    temaki = Ingredient("temaki")
    salmon = Ingredient("salmão")

    assert sushi.name == "sushi"
    assert sushi.restrictions == set()
    assert salmon.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }

    assert hash(sushi) == hash(s2)
    assert hash(sushi) != hash(temaki)

    assert sushi == s2
    assert sushi != temaki

    assert sushi.__repr__() == "Ingredient('sushi')"
