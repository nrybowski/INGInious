from dataclasses import dataclass, field
import gettext
import os

from inginious import get_root_path
from inginious.common.agents import Capabilities

_ = gettext.gettext

@dataclass(frozen=True)
class DockerAgentCapabilities(Capabilities):

    def __post_init__(self):
        # Load the capabilities translations from disk.
        translations = {"en": gettext.NullTranslations()}
        trad_path = os.path.join(get_root_path(), 'agent/docker_agent/i18n')
        available = [
            lang for lang in os.listdir(trad_path) if os.path.isdir(os.path.join(trad_path, lang))
        ]
        translations.update({
            lang: gettext.translation('messages', trad_path, [lang]) for lang in available
        })
        object.__setattr__(self, '__translations__', translations)
    
    """ Indicates whether the Agent supports GPUs. """
    gpu: bool = field(doc=_("The task requires a GPU."))
    """ Indicates whether the Agent supports running student code as root. """
    run_as_root: bool = field(doc=_("The task requires the student code to be ran as root. (EXPERIMENTAL)"))
    """ Indicates whether the Agent supports SSH proxying to student container. """
    ssh: bool = field(doc=_("The tasks requires providing access to the student container through SSH."))
