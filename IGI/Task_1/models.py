"""
Data models: Team, TeamTable, StatisticsMixin.
Lab 4, Task 1, Variant 6.
Version: 1.0
Developer: Ivan Leuchyshyn
Date: 2026-04-23
"""

from typing import List, Dict, Optional
from functools import total_ordering


class StatisticsMixin:
    """Mixin that adds statistical methods to a table."""

    def get_first_place(self):
        """Return the team(s) with maximum points."""
        if not self._teams:
            return None
        max_points = max(t.points for t in self._teams)
        return [t for t in self._teams if t.points == max_points]

    def get_sorted_by_rank(self):
        """Return teams sorted by points descending, then by name."""
        return sorted(self._teams, key=lambda t: (-t.points, t.name))


@total_ordering
class Team:
    """Represents a sports team with name and points."""

    _instance_count = 0

    def __init__(self, name: str, points: int):
        self._name = name
        self._points = points
        Team._instance_count += 1
        self._id = Team._instance_count

    @property
    def name(self) -> str:
        """Team name (read-only after creation)."""
        return self._name

    @property
    def points(self) -> int:
        return self._points

    @points.setter
    def points(self, value: int) -> None:
        """Setter with validation."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Points must be a non-negative integer")
        self._points = value

    @property
    def id(self) -> int:          
        """Unique identifier (read-only)."""
        return self._id

    def __str__(self) -> str:
        """Human-readable representation."""
        return f"{self.name}: {self.points} pts"

    def __repr__(self) -> str:    
        return f"Team('{self.name}', {self.points})"

    def __eq__(self, other):
        if not isinstance(other, Team):
            return NotImplemented
        return self.name == other.name and self.points == other.points

    def __lt__(self, other) -> bool:
        if not isinstance(other, Team):
            return NotImplemented
        if self.points != other.points:
            return self.points > other.points
        return self.name < other.name

    def to_dict(self) -> Dict[str, str]:
        return {"name": self.name, "points": str(self.points)}

    @classmethod                         
    def from_dict(cls, data: Dict[str, str]) -> 'Team':
        """Create Team from dictionary (used during deserialization)."""
        return cls(data["name"], int(data["points"]))

    @classmethod
    def get_instance_count(cls) -> int:
        """Static method returning number of created teams."""
        return cls._instance_count


class TeamTable(StatisticsMixin):
    """Collection of teams with CRUD operations."""

    def __init__(self, teams: Optional[List[Team]] = None):
        self._teams = teams if teams is not None else []

    def add_team(self, team: Team) -> None:
        """Add a single team."""
        self._teams.append(team)

    def remove_team(self, name: str) -> bool:
        """Remove team by name. Return True if removed."""
        for i, t in enumerate(self._teams):
            if t.name.lower() == name.lower():
                del self._teams[i]
                return True
        return False

    def find_team(self, name: str) -> Optional[Team]:
        """Find team by name (case-insensitive)."""
        for t in self._teams:
            if t.name.lower() == name.lower():
                return t
        return None

    def get_all_teams(self) -> List[Team]:   
        return self._teams.copy()

    def to_dict_list(self) -> List[Dict[str, str]]:
        """Convert all teams to list of dicts for serialization."""
        return [t.to_dict() for t in self._teams]

    @classmethod
    def from_dict_list(cls, data: List[Dict[str, str]]) -> 'TeamTable':
        """Reconstruct TeamTable from list of dicts."""
        teams = [Team.from_dict(item) for item in data]
        return cls(teams)

    def __len__(self) -> int:
        return len(self._teams)

    def __getitem__(self, index: int) -> Team:
        return self._teams[index]