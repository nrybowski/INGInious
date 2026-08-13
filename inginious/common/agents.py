from dataclasses import dataclass
from enum import StrEnum, auto
from abc import ABC

@dataclass(frozen=True)
class Capabilities(ABC):
    """ Agent capabilities. """

    @property
    def _capabilities(self):
        return {c: f.doc for c, f in self.__dataclass_fields__.items()}

class AgentType(StrEnum):
    OCI = auto()
    MCQ = auto()

@dataclass(frozen=True)
class GradingEnvironment:
    """ Environment hash identifier """
    id: str
    """ Creation date in epoch """
    created: int
    """ List of requested ports """
    ports: list[int]
    """ Do not propagate the environment to the frontend """
    advertised: bool = True
