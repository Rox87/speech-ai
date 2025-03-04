import os
from pathlib import Path

def clean_folder(folder_path: str):
    """Safely delete all files in specified folder"""
    try:
        # Convert to Path object
        path = Path(folder_path)
        
        # Validate path
        if not path.exists():
            print(f"Error: Path '{folder_path}' does not exist")
            return
            
        if not path.is_dir():
            print(f"Error: '{folder_path}' is not a directory")
            return
            
        # Get all files (excluding subdirectories)
        files = [f for f in path.iterdir() if f.is_file()]
        
        if not files:
            print("No files found to delete")
            return
            
             
        # Delete files
        deleted_count = 0
        for file in files:
            try:
                os.unlink(file)
                print(f"Deleted: {file.name}")
                deleted_count += 1
            except Exception as e:
                print(f"Error deleting {file.name}: {str(e)}")
                
        print(f"\nSuccessfully deleted {deleted_count}/{len(files)} files")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    clean_folder("temp")
