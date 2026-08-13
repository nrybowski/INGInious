from dataclasses import dataclass

@dataclass(frozen=True)
class DockerAgentCapabilities:
    """ Indicates whether the Agent supports GPUs. """
    gpu: bool
    """ Indicates whether the Agent supports running student code as root. """
    run_as_root: bool
    """ Indicates whether the Agent supports SSH proxying to student container. """
    ssh: bool
