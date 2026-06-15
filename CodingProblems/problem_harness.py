import argparse
import subprocess

from pathlib import Path

def find_file_modern(target_filename):
    print(f"Searching for '{target_filename}'...")
    
    # 1. Turn your starting path string into a Path object
    base_dir = Path('.')
    
    # 2. Use rglob to recursively find matches
    # This creates an iterator containing all matching Path objects
    matches = base_dir.rglob(target_filename)
    
    # 3. Loop through the matches (rglob can find multiple files with the same name!)
    found_files = []
    for match in matches:
        # .resolve() gives you the absolute, full path to the file
        full_path = match.resolve()
        found_files.append(full_path)
        
    if not found_files:
        return False
        
    return True

def validate_args():
    if not args.platform or (args.platform.lower() != 'h' and args.platform.lower() != 'l'):
        print('[Warning] Please provide a valid platform to find the problem')
        return False

    if not args.filename:
        print('[Warning] Please provide a valid filename to find the problem')
        return False

    if not find_file_modern(args.filename):
        print('File Not Found: ' + args.filename)
        return False

    return True

def main():
    platform_dict = {'h':'HackerRank', 'l':'LeetCode'}
    process = subprocess.run(["python", platform_dict[args.platform.lower()] + "/"+args.filename], 
                             capture_output=True, 
                             text=True)

    if process.returncode == 0:
        print("----- Process Success -----")
        print(process.stdout.strip())
    else:
        print("----- Process Failed -----")
        print(process.stderr)

    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='Coding Problem Harness',
                    description='Acts as a harness for running coding problems and testing them, printing out results.')

    parser.add_argument('-v','--verbose', action='store_true')
    parser.add_argument('-p', '--platform')
    parser.add_argument('-fn', '--filename')
    args = parser.parse_args()
    
    if validate_args():
        main()
