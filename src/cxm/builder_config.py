from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pathlib import Path
    from cxm.utils.module_importer import ModuleImporter


class BuilderConfig:
    cwd: Path
    module_importer: ModuleImporter

    def __init__(self, cwd: Path):
        self.cwd = cwd

