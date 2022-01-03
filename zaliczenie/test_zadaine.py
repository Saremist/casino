import pytest
from zadanie import (
    Menager,
    Developer,
    Project,
    OverWorkLimitError,
    NoDeveloperError,
    NoMenagerError,
)


# negative projects
# over 3 projects
# no name emploee
# no menager


def test_negative_projects():
    with pytest.raises(ValueError):
        Karol = Menager("karol", 5, -1)
    with pytest.raises(ValueError):
        Borys = Developer("B", 50, -10, "python")


def test_over_limit():
    with pytest.raises(OverWorkLimitError):
        Karol = Menager("Karol", 5, 3)


def test_add_third_project():
    Ja = Developer("Milan", 5, 2, "python")
    with pytest.raises(OverWorkLimitError):
        Ja.set_project_count(3)


def test_noname():
    with pytest.raises(ValueError):
        Karol = Menager("", 5, 1)


def test_create_project():
    King = Menager("King", 5, 0)
    Me = Developer("My_Name", 10, 0, "python")
    first_project = Project("First", {"python": 1})
    assert first_project._developer_list == [Me]
    assert first_project._head_menager == King


def test_nodev_found():
    King = Menager("King", 5, 0)
    Me = Developer("My_Name", 10, 0, "python")
    with pytest.raises(NoDeveloperError):
        first_project = Project("First", {"java": 1})


def test_nomenager_found():
    King = Menager("King", 5, 2)
    Me = Developer("My_Name", 10, 0, "java")
    with pytest.raises(NoMenagerError):
        first_project = Project("First", {"java": 1})


# def test_two_languages():
# out of time :(
