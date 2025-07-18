# Hands-On Exercises: Python `os` and `os.path` Modules

This guide introduces basic file and directory operations using Python's `os` and `pathlib.Path` modules. It mirrors Linux shell operations you may already know, using Python code to accomplish the same tasks.

---
## Hands-On #1

### Exercise 0: Environment Set-up

Clone the repository at `https://github.com/shafe123/AI2C-python-files.git`.

### Exercise 1: Get Current Working Directory

**Goal**: Use Python to print the current working directory.

✅ *Check*: Run the script and confirm it prints the full path of your working directory.

---

### Exercise 2: Change Directory

**Goal**: Change into a directory named `projects`.

✅ *Check*: Ensure that you are now in the `projects` directory. Create it first if it doesn't exist.

---

### Exercise 3: List Directory Contents

**Goal**: List all files and directories in the current directory.

✅ *Check*: Compare the output to the `ls` command in your terminal.

---

### Exercise 4: Create a Directory

**Goal**: Create a directory named `data`.

✅ *Check*: Verify the directory exists using `pathlib` or by checking in your terminal.

---

### Exercise 5: Create Nested Directories

**Goal**: Create nested directories `a/b/c` in one call.

✅ *Check*: Use `pathlib` to confirm creation.

---

### Exercise 6: Remove a File

**Goal**: Delete a file named `temp.txt`.

✅ *Check*: Use `pathlib` to validate that the file no longer exists.

---

### Exercise 7: Remove an Empty Directory

**Goal**: Delete an empty directory named `old_data`.

✅ *Check*: If the directory is not empty, this will raise an error. Try clearing it first.

---

### Exercise 8: Rename a File

**Goal**: Rename `example.txt` to `renamed_example.txt`.

✅ *Check*: Confirm the new name exists and the old one doesn't.

---

### Exercise 9: Check File or Directory Type

**Goal**: Determine whether `target` is a file or directory.

✅ *Check*: Create a test file or directory and run the script to see the correct output.

## Hands-On #2



## Stretch Goals

**Goal**: Print the size and last modified time of `data.csv`.

✅ *Check*: Match file size with `ls -l` and modification time with `stat` in the terminal.

**Goal**: Gain a deeper understanding of os and Pathlib.

Create a short listing of the overlapping features of os and Pathlib.  Why might one prefer one module over the other?