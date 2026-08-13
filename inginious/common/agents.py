from dataclasses import dataclass
from enum import StrEnum

class AgentType(StrEnum):
    OCI = "docker"
    MCQ = "mcq"

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
