import json
import shutil
from pathlib import Path
from typing import Any, Final

CONFIG_FILENAME: Final[str] = "config.json"


def load_config(config_path: Path) -> dict[str, Any]:
    """Loads the configuration from a JSON file."""
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def clean_cache(root_dir: Path, target_dirs: set[str]) -> int:
    """Recursively finds and deletes target cache folders.
    Returns the number of deleted folders."""

    removed_count = 0
    for target in target_dirs:
        # '.rglob()' recursively searches for everything with the specified name
        for path in root_dir.rglob(target):
            # '.is_dir()' checks whether it's a directory(folder) or not
            if path.is_dir():
                try:
                    # 'shutil.rmtree()' Recursively delete a directory tree.
                    shutil.rmtree(path)
                    print(f"[Deleted]: {path}")
                    removed_count += 1
                except (
                    OSError
                ) as e:  # Catch a specific system error instead of a generic Exception
                    print(f"[Error while deleting {path}]: {e}")

    return removed_count


def main() -> None:
    print("=== Python Cache Cleaner ===")

    # __file__ -> absoulte path to main.py
    # .parent -> cuts off 'main.py', leaving only ../cache_cleaner/
    script_dir = Path(__file__).parent
    # confing_file -> ../cache_cleaner/confing.json
    config_file = script_dir / CONFIG_FILENAME

    try:
        config = load_config(config_file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"[Config Error]: {e}")
        return

    target_path = Path(config.get("target_project_path", ""))
    target_dirs = set(config.get("target_dirs", []))

    if not target_path.exists():
        print(f"[Error]: Target path from config does not exist: {target_path}")
        return

    # '.resolve()' guarantees a clear, absolute path
    print(f"Target directory: {target_path.resolve()}")
    print(f"Target dirs to clean: {target_dirs}")
    print("Scanning and cleaning...\n")

    # We pass both arguments, as required by the function signature
    removed = clean_cache(target_path, target_dirs)

    print(f"\nCleanup complete! Cache folders removed: {removed}")


if __name__ == "__main__":
    main()
