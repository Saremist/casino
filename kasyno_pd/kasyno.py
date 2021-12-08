from random import randint


class PersonNotPlayerError(Exception):
    def __init__(self, person) -> None:
        super().__init__(f"{person} is not a Player")


class DuplicatePlayersNotAllowed(Exception):
    def __init__(self, person) -> None:
        super().__init__(f"{person._name} is already inside of this casino")


class Casino:
    def __init__(self, players_list=None) -> None:
        self.players_inside = []
        if players_list:
            self.players_inside = players_list
        self.winner = None

    def __str__(self):
        if self.winner:
            return f"The winner in last round was {self.winner._name} by scoring {self.winning_points} points"
        else:
            return "Draw! There is no winner selected"

    def add_players(self, players: list) -> None:
        for player in players:
            if player in self.players_inside:
                raise DuplicatePlayersNotAllowed(player)
            if isinstance(player, Player):
                self.players_inside.append(player)
            else:
                raise PersonNotPlayerError(player)

    def kick_players(self, players_list: list) -> None:
        for player in players_list:
            if not isinstance(player, Player):
                raise PersonNotPlayerError(player)
            self.players_inside.remove(player)

    def get_winning_points(self):
        """
        Needs to have dice_dict to work
        """
        round_points = []
        for player in self.players_inside:
            player.get_points()
            round_points.append(player._points)
        self.winning_points = max(round_points)

    def roll_player_dices(self):
        for player in self.players_inside:
            player.throw_dice()

    def select_winner(self):
        """logick behind selecting a winner
        sets winner to none and returns it to stop shearching for a winner
        if two or more players have max points
        """
        self.winner = None
        for player in self.players_inside:
            if player._points == self.winning_points:
                if not self.winner:
                    self.winner = player
                    continue
                if self.winner:
                    self.winner = None
                    break
        return self.winner

    def round(self):
        """
        This metod plays a round of dice and returns winner of the round
        Each player has his own dices saved in Player.dice_dict
        """
        self.roll_player_dices()
        self.get_winning_points()
        self.select_winner()
        return self.winner


class Player:
    def __init__(self, name_of_player=None) -> None:
        if not name_of_player:
            self._name = "Anonim"
        else:
            self._name = str(name_of_player)
        self._points = 0

    def __str__(self):
        """
        self._dice_dict is created only after throwing dices
        str() describes players adn if has thrown any dice prints his dice combination
        """
        try:
            return f"{self._name}, rolled: {self.dice_dict}, has {self._points} points"
        except AttributeError:
            return f"{self._name} haven't yet rolled any dice"

    def roll_dice(self):
        """
        throw_dice creates dict with results of how many times each side of dice was counted.
        """
        dices = [randint(1, 6) for _ in range(4)]
        temp_dice_dict = {}
        for number in range(1, 7):
            temp_dice_dict[number] = dices.count(number)
        return temp_dice_dict

    def throw_dice(self):
        self.dice_dict = self.roll_dice()

    def get_points(self) -> int:
        """
        counts how many pionts Player has based on sub metods for pairs and only odd/even rules
        sets and returns self._points being maximum of above rules
        """
        points = []
        points.append(self.points_only_even())
        points.append(self.points_only_odd())
        for number_on_dice in range(1, 7):  # check fo prair triples and qarets
            points.append(self.points_pairs(number_on_dice))
        self._points = max(
            points
        )  # returns maximum of all rules considered in dice game

    def count_dots(self):
        points = 0
        for i in self.dice_dict:
            points += i * self.dice_dict[i]
        return points

    def points_only_even(self) -> int:
        """
        counts points if dices show only odd numbers
        """
        for i in (1, 3, 5):
            if self.dice_dict[i] != 0:
                return 0
        return self.count_dots() + 2

    def points_only_odd(self) -> int:
        """
        counts points if dices show only odd numbers
        """
        for i in (2, 4, 6):
            if self.dice_dict[i] != 0:
                return 0
        return self.count_dots() + 3

    def points_pairs(self, number):
        if self.dice_dict[number] == 2:
            return number * 2
        elif self.dice_dict[number] == 3:
            return number * 4
        elif self.dice_dict[number] == 4:
            return number * 6
        return 0


def main():
    """
    plays example round in vegas casino
    5 players with one anonim
    prints str of casino that shows resoult in that round
    and prints str of each player that incloude their name and dice_dict and final score
    """
    player1 = Player()
    player2 = Player("Bajtek")
    player3 = Player("Kajtek")
    player4 = Player("Orc")
    player5 = Player("Hydra")

    Vegas = Casino([player1, player2, player3, player4, player5])
    Vegas.round()
    print(str(Vegas))
    for p in Vegas.players_inside:
        print(str(p))


if __name__ == "__main__":
    main()
