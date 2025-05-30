from pathlib import Path
import shutil




def rename_files(
    root: Path,
    old_name: str,
    new_name: str,
    ext_list: list[str],
    dry_run: bool = False,
    verbose: bool = True
    ) -> int:
        """
            Recursively renames files containing old_name to new_name.
            
            Args:
                root: Root directory to search
                old_name: Text to replace in filenames
                new_name: New text
                ext_list: File extensions to process (e.g., [".cs", ".txt"])
                dry_run: If True, only preview changes
                verbose: If False, suppress output
            
            Returns:
                Number of successfully renamed files
        """
        renamed_count = 0
        
        for ext in ext_list:
            for file in root.rglob(f"*{ext}"):
                if file.exists():
                    if old_name in file.stem:
                        new_file = file.with_stem(file.stem.replace(old_name, new_name))
                        try:
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
        return renamed_count
    
    
    
    
if __name__ == "__main__":

    rename_files(
    root=Path(__file__).resolve().parent,
    old_name="SpotiMusic",
    new_name="SpotifyWebAPI_Intro",
    ext_list=[".cs", ".csproj", ".csproj.user", ".sln"],
    dry_run=True,  # Just preview
    verbose=False
)