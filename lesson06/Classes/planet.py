import random


class Planet:
    def __init__(
        self,
        name: str,
        coordinates: tuple[float, float, float],
        danger: float,
        resources: float,
        atmosphere: str,
    ):
        self.name = name
        self.coordinates = coordinates
        self.danger = danger
        self.resources = resources
        self.atmosphere = atmosphere
        # Maximum missions allowed: fewer for higher danger
        self.max_missions = max(1, 4 - int(self.danger))
        self.missions_done = {}

    def __str__(self):
        return (
            f"{self.name} - Coordinates: ({self.coordinates[0]}, {self.coordinates[1]}, {self.coordinates[2]}), "
            f"Danger: {self.danger}, Resources: {self.resources}, Atmosphere: {self.atmosphere}"
        )

    def __sub__(self, other):
        diff = tuple(x - y for x, y in zip(self.coordinates, other.coordinates))
        return (diff[0] ** 2 + diff[1] ** 2 + diff[2] ** 2) ** 0.5

    def can_do_mission(self, player_name):
        return self.missions_done.get(player_name, 0) < self.max_missions

    def record_mission(self, player_name):
        self.missions_done[player_name] = self.missions_done.get(player_name, 0) + 1

    def mission_success(self):
        chance = max(0.2, 1.0 - 0.15 * self.danger)
        roll = random.random()
        if roll < chance:
            return "success", self.resources
        elif roll < chance + 0.2:
            return "partial", self.resources // 2
        else:
            return "fail", 0
