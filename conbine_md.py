import os

def consolidate_markdown_files(folders, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for folder in folders:
                if not os.path.isdir(folder):
                    print(f"Error: {folder} is not a valid directory.")
                    continue
                for filename in os.listdir(folder):
                    if filename.endswith(".md"):
                        file_path = os.path.join(folder, filename)
                        try:
                            with open(file_path, 'r', encoding='utf-8') as infile:
                                outfile.write(infile.read())
                                outfile.write("\n---\n")
                        except UnicodeDecodeError:
                            print(f"UnicodeDecodeError: Skipping file {file_path} due to encoding issues.")
                        except Exception as e:
                            print(f"Error reading file {file_path}: {e}")
        print(f"Files successfully consolidated into {output_file}")
    except Exception as e:
        print(f"Error writing to output file {output_file}: {e}")

# List of folders to consolidate
folders = [
    "Energy",
    "Materials",
    "Industrials",
    "Consumer Discretionary",
    "Consumer Staples",
    "Health Care",
    "Financials",
    "Information Technology",
    "Communication Services",
    "Utilities",
    "Real Estate"
]

# Output file name
output_file = "consolidated_output.md"

# Consolidate markdown files
consolidate_markdown_files(folders, output_file)
