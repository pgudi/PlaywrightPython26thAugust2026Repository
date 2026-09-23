import pytest

@pytest.mark.parametrize(
    "num1, num2, result",
    [(10,20,30), (30,40, 70), (4, 6, 10), (15, 30 ,45)]
)

def test_numberdata_params(num1,num2,result):
    assert (num1 + num2 ) == result