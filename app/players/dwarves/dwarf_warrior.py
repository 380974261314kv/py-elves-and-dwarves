from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(
        self,
        nickname: str,
        favourite_dish: str,
        hummer_level: int
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self.nickname = nickname
        self._favourite_dish = favourite_dish
        self._hummer_level = hummer_level

    def get_rating(self) -> int:
        return self._hummer_level + 4

    def player_info(self) -> str:
        name = self.nickname
        lv = self._hummer_level
        return f"Dwarf warrior {name}. {name} has a hummer of the {lv} level"