import tkinter as tk
from tkinter import filedialog

def remove_duplicates(file_path, output_path=None, ignore_case=False):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Count the total number of lines in the original file
        total_lines = len(lines)

        if ignore_case:
            # Normalize to lower case for case-insensitive comparison
            lines = [line.lower() for line in lines]

        # Remove duplicates by converting to a set and back to a list
        unique_lines = list(set(lines))

        # If case was ignored, we restore the original case by keeping the first occurrence
        if ignore_case:
            unique_lines = sorted(set(lines), key=lambda x: lines.index(x))

        # Calculate stats
        removed_lines = total_lines - len(unique_lines)
        unique_lines_count = len(unique_lines)

        # Save the cleaned lines to a new file if output path is provided
        output_path = output_path or f"cleaned_{file_path.split('/')[-1]}"
        with open(output_path, 'w') as output_file:
            output_file.writelines(unique_lines)

        # Print stats
        print(f"Total lines in original file: {total_lines}")
        print(f"Unique lines after removal: {unique_lines_count}")
        print(f"Lines removed: {removed_lines}")
        print(f"File cleaned and saved as {output_path}")

    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def select_file_and_run():
    # Create a Tkinter root window (it won't appear)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open a file dialog to select a text file
    file_path = filedialog.askopenfilename(title="Select a text file", filetypes=[("Text files", "*.txt")])

    if file_path:  # Proceed if a file is selected
        output_path = filedialog.asksaveasfilename(title="Save cleaned file as", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        
        if output_path:  # Proceed if a save path is selected
            remove_duplicates(file_path, output_path, ignore_case=True)
        else:
            print("No output file selected.")
    else:
        print("No file selected.")

# Run the tool with a file selector
select_file_and_run()
