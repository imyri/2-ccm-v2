import os

# 1. Folders we DO NOT want to read (keeps the file size tiny)
IGNORE_DIRS = {
    '.git', 'node_modules', 'venv', 'env', '__pycache__', 
    '.next', 'backtest_results', 'data_store', 'logs'
}

# 2. File types we DO want to read (your actual code blueprints)
ALLOWED_EXTENSIONS = {'.py', '.js', '.jsx', '.ts', '.tsx', '.md'}

# 3. The name of the final file we will generate
OUTPUT_FILE = 'bot_code_for_ai.txt'

def pack_code():
    print("Starting to pack your codebase...")
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk('.'):
            # Tell the script to completely ignore the heavy junk folders
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            
            for file in files:
                # Only grab the file if it matches our allowed extensions
                if any(file.endswith(ext) for ext in ALLOWED_EXTENSIONS):
                    
                    # Skip the script itself so we don't create an infinite loop
                    if file == 'pack_for_ai.py':
                        continue

                    file_path = os.path.join(root, file)
                    
                    # Write a clear header so I know exactly which file I am reading
                    outfile.write(f"\n\n{'='*60}\n")
                    outfile.write(f"FILE: {file_path}\n")
                    outfile.write(f"{'='*60}\n\n")
                    
                    # Read the code and append it to our master file
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                            outfile.write(infile.read())
                    except Exception as e:
                        outfile.write(f"[Error reading file: {e}]\n")

    print(f"Done! Your entire codebase has been securely packed into: {OUTPUT_FILE}")

if __name__ == '__main__':
    pack_code()