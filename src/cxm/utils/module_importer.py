import os

from pathlib import Path

from cxm.builder_config import BuilderConfig


class Module:
    path: Path
    loaded: bool = False

    def __init__(self, path: Path):
        self.path = path


class ModuleImporter:
    builder_config: BuilderConfig
    modules : list[Module]

    def __init__(self, builder_config: BuilderConfig):
        self.builder_config = builder_config
        self.modules = []

    def find_all_modules(self):
        for root, dirs, files in os.walk(self.builder_config.cwd):
            for file in files:
                if file.endswith('.Module.py'):
                    module = Module(Path(os.path.join(root, file)))
                    self.modules.append(module)
                    print(module.path)
