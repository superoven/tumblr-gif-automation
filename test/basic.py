from src.process import output, fifo
from subprocess import call
import pytest

valid_input_values = [
    (1, 1.2),
    (0, 2),
    (0.12, 1.312),
    (4.2, 5)
]

invalid_input_values = [
    (6, 4.3),
    (-1, 0),
    (2.9, 0),
]


@pytest.mark.parametrize('inputs', valid_input_values)
def test_working_cases(inputs):
    with open(fifo, "r") as f:
        ret, filename = output(inputs[0], inputs[1], f)
        assert ret == 0
        call(["rm", "-f", filename])


@pytest.mark.parametrize('inputs', valid_input_values)
def test_failing_cases(inputs):
    with open(fifo, "r") as f:
        ret, filename = output(inputs[0], inputs[1], f)
        assert ret == 1