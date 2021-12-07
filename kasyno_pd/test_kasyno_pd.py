import pytest
from kasyno import Casino, Player, PersonNotPlayerError, DuplicatePlayersNotAllowed


def smart_mock(value_to_return):
    def smart_mock_wrapper(*args, **kwargs):
        return value_to_return

    return smart_mock_wrapper


def test_default_Player_name():
    test_player = Player()
    assert test_player._name == "Anonim"


def test_Player_name():
    test_player = Player("Name")
    assert test_player._name == "Name"


def test_Player_name_number():
    test_player = Player(1)
    assert test_player._name == "1"
    assert str(test_player) == "1 haven't yet rolled any dice"


def test_points_only_even(monkeypatch):
    player1 = Player("Alaska")
    monkeypatch.setattr(
        "kasyno.Player.roll_dice",
        smart_mock({1: 2, 2: 0, 3: 1, 4: 0, 5: 1, 6: 0}),
    )
    player1.throw_dice()
    assert player1.points_only_even() == 0
    assert player1.points_only_odd() == 13


def test_points_only_odd(monkeypatch):
    player1 = Player("Alaska")
    monkeypatch.setattr(
        "kasyno.Player.roll_dice",
        smart_mock({1: 0, 2: 1, 3: 0, 4: 2, 5: 0, 6: 1}),
    )
    player1.throw_dice()
    assert player1.points_only_even() == 18
    assert player1.points_only_odd() == 0


def test_pairs_1():
    player1 = Player("Alaska")
    player1.dice_dict = {1: 2, 2: 0, 3: 1, 4: 0, 5: 1, 6: 0}
    assert player1.points_pairs(1) == 2
    assert player1.points_pairs(2) == 0
    assert player1.points_pairs(3) == 0
    assert player1.points_pairs(4) == 0
    assert player1.points_pairs(5) == 0
    assert player1.points_pairs(6) == 0


def test_pairs_2():
    player1 = Player("Alaska")
    player1.dice_dict = {1: 2, 2: 0, 3: 1, 4: 4, 5: 1, 6: 0}
    assert player1.points_pairs(1) == 2
    assert player1.points_pairs(2) == 0
    assert player1.points_pairs(3) == 0
    assert player1.points_pairs(4) == 4 * 6
    assert player1.points_pairs(5) == 0
    assert player1.points_pairs(6) == 0


def test_pairs_3():
    player1 = Player("Alaska")
    player1.dice_dict = {1: 2, 2: 0, 3: 1, 4: 2, 5: 3, 6: 0}
    assert player1.points_pairs(1) == 2
    assert player1.points_pairs(2) == 0
    assert player1.points_pairs(3) == 0
    assert player1.points_pairs(4) == 4 * 2
    assert player1.points_pairs(5) == 5 * 4
    assert player1.points_pairs(6) == 0


def test_get_points(monkeypatch):
    monkeypatch.setattr("kasyno.Player.throw_dice", smart_mock(None))
    player1 = Player("Alaska")
    player1.dice_dict = {1: 2, 2: 0, 3: 1, 4: 0, 5: 1, 6: 0}
    player1.get_points()
    assert (
        str(player1)
        == "Alaska, rolled: {1: 2, 2: 0, 3: 1, 4: 0, 5: 1, 6: 0}, has 13 points"
    )
    player2 = Player("Bokser")
    player2.dice_dict = {1: 0, 2: 2, 3: 0, 4: 1, 5: 0, 6: 1}
    player2.get_points()
    assert (
        str(player2)
        == "Bokser, rolled: {1: 0, 2: 2, 3: 0, 4: 1, 5: 0, 6: 1}, has 16 points"
    )


def test_select_winner():
    playera = Player("Alan")
    playerb = Player("Borys")
    playera._points = 10
    playerb._points = 11
    vegas = Casino([playera, playerb])
    vegas.winning_points = 11
    assert vegas.select_winner() == playerb


def test_casino_take_players():
    player1 = Player("Alan")
    player2 = Player("Bartek")
    Vegas = Casino([player1, player2])
    assert Vegas.players_inside == [player1, player2]


def test_casino_round(monkeypatch):
    monkeypatch.setattr("kasyno.Player.throw_dice", smart_mock(None))
    # turns off die throwing. lets set manual dice_dict for the players
    player1 = Player("Alan")
    player2 = Player("Bartek")
    player1.dice_dict = {1: 2, 2: 0, 3: 1, 4: 0, 5: 1, 6: 0}
    player2.dice_dict = {1: 0, 2: 2, 3: 0, 4: 1, 5: 0, 6: 1}
    Vegas = Casino([player1, player2])
    Vegas.round()
    assert player1._points == 13
    assert player2._points == 16


def test_casino_add():
    player1 = Player()
    player2 = Player("Bajtek")
    player3 = Player("Kajtek")
    Vegas = Casino()
    Vegas.add_players([player1, player2, player3])
    assert Vegas.players_inside == [player1, player2, player3]


def test_casino_kick():
    player1 = Player()
    player2 = Player("Bajtek")
    player3 = Player("Kajtek")
    Vegas = Casino([player1, player2, player3])
    Vegas.kick_players([player1, player2])
    assert Vegas.players_inside == [player3]


def test_casino_duplicate_add():
    player1 = Player()
    player2 = Player("Bajtek")
    player3 = Player("Kajtek")
    Vegas = Casino([player1, player2, player3])
    with pytest.raises(DuplicatePlayersNotAllowed):
        Vegas.add_players([player1])


def test_Not_player_add():
    Vegas = Casino()
    with pytest.raises(PersonNotPlayerError):
        Vegas.add_players("Bend")


def test_Not_player_kick():
    Vegas = Casino()
    with pytest.raises(PersonNotPlayerError):
        Vegas.kick_players("Bend")


def test_Casino_kick_error():
    Vegas = Casino([Player()])
    with pytest.raises(ValueError):
        Vegas.kick_players([Player()])
