from pathlib import Path
import shutil
import re

# Get the script's directory (./Scripts/)
SCRIPT_DIR = Path(__file__).parent.resolve()

# Navigate to project root (one level up from Scripts/)
ROOT_DIR = SCRIPT_DIR.parent

OLD_FILE_NAME = "SpotifyToYouTubeMusicTransfer"
NEW_FILE_NAME = "SpotifyWebAPI_Intro"


def rename_files(
    root: Path,
    old_name: str,
    new_name: str,
    dry_run: bool = False,
    verbose: bool = True
    ) -> None:
        renamed_count = 0
        for file in root.rglob("*"):
                pattern = re.compile(rf"\b{old_name}\b")
                try:
                    if pattern.search(str(file)):
                        new_file = file.with_stem(file.stem.replace(old_name, new_name))
                        if verbose:
                            print(f"Renaming: {file.name} → {new_file.name}")
                        if not dry_run:
                            shutil.move(str(file.resolve()), str(new_file.resolve()))
                            renamed_count += 1
                except Exception as e:
                    if verbose:
                        print(f"Error renaming {file.name}: {str(e)}")
        if verbose:
            print(f"\nTotal files renamed: {renamed_count}")



def count_files(root_dir: Path, search_name: str) -> int:
    return sum(1 for file in root_dir.rglob("*") 
           if file.is_file() and search_name in file.stem)


if __name__ == "__main__":
    rename_files(
        root=ROOT_DIR,
        old_name=OLD_FILE_NAME,
        new_name=NEW_FILE_NAME,
        dry_run=False,
        verbose=False
    )
    
    file_count = count_files(ROOT_DIR, NEW_FILE_NAME)
    print(f"Total files containing '{NEW_FILE_NAME}': {file_count}")
    