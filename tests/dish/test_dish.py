from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    with pytest.raises(ValueError):
        Dish("sushi", -1)

    with pytest.raises(TypeError):
        Dish("sushi", "sushi")

    sushi_ss = Dish("sushi", 10)
    s2_ss = Dish("sushi", 10)
    salmoon_ss = Dish("salmão", 15)

    assert sushi_ss.name == "sushi"
    assert sushi_ss.__repr__() == "Dish('sushi', R$10.00)"
    assert sushi_ss == s2_ss
    assert sushi_ss != salmoon_ss
    assert hash(sushi_ss) == hash(s2_ss)
    assert hash(sushi_ss) != hash(salmoon_ss)
    assert sushi_ss.get_restrictions() == set()
    sushi_ss.add_ingredient_dependency("arroz", 2)
    assert sushi_ss.get_ingredients() == {"arroz"}
