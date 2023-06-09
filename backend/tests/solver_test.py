import pytest

from models.field import Field
from services.field_factory import FieldFactory
from services.solver import Solver


def test_try_line_with_small_example():
    field = FieldFactory.create_small_example()
    Solver.try_line(field, 0, True)
    assert field.is_complete()


@pytest.mark.skip(reason="no way of currently testing this")
def test_try_line_with_mouse_example():
    field = FieldFactory.create_mouse_example()
    Solver.try_line(field, 0, True)
    assert field.is_complete()


@pytest.mark.skip(reason="no way of currently testing this")
def test_try_line_with_default_example():
    field = FieldFactory.create_default_example()
    Solver.try_line(field, 0, True)
    assert field.is_complete()


def test_try_line_with_2x2():
    field = Field(2, {
        'rows': [[1], [1]],
        'cols': [[1], [1]]
    })
    Solver.try_line(field, 0, True)
    assert field.solution_count() == 2


def test_try_line_with_3x3():
    field = Field(3, {
        'rows': [[1], [1], [1]],
        'cols': [[1], [1], [1]]
    })
    Solver.try_line(field, 0, True)
    assert field.solution_count() == 3
