import os

from pathlib import Path

from cxm.builder_config import BuilderConfig
from cxm.utils.module_importer import ModuleImporter

def main():
    builder_config = BuilderConfig(Path(os.getcwd()))
    builder_config.module_importer = ModuleImporter(builder_config)

    print(f"Hello World: {builder_config.cwd}")
    builder_config.module_importer.find_all_modules()



if __name__ == "__main__":
    main()
