import pytest


def content_weight(bottle_weight, scale):
    parts = int(scale.split()[0])
    return bottle_weight / (parts + 1) * parts if 'larger' in scale else bottle_weight / (parts + 1)




print(content_weight(500, "9 times larger"))

print(content_weight(1000, "4 times smaller"))
print(content_weight(1000, "49 times larger"))


@pytest.mark.parametrize("bottle_weight, scale, result",
                [
                    (500, "9 times larger", 450),
                    (1000, "999 times larger", 999),
                    (10000, "999 times smaller", 10),
                    (300, "2 times smaller", 100)
                ]
                         )
def test_content_weight(bottle_weight, scale, result):
    assert content_weight(bottle_weight, scale) == result
