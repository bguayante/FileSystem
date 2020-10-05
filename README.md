# In-Memory File System

## Description

The In-Memory File System simulates a hierarchical physical storage structure without writing to the disk. All files and directories created are lost when the program is terminated.

## Functionality

Users of this program may use commands similar to Bash to manipulate files in the system. `ls`, `cd`, `mkdir`, and `touch` commands are included. The `cd`, `mkdir`, and `touch` commands require arguments, though `ls` does not.

## Limitations

An area in which this program and Bash differ, however, is that this program processes commands in discrete steps and would be inappropriate for scripting. Commands such as `touch` and `mkdir` accept one and only one argument and ignore all others. The command `touch file1 file2` would create `file1` in the current directory, but not `file2`. To create both files, it is necessary to use the `touch` command twice, such as `touch file1` and `touch file2`. Similarly, `cd` can only be done in discrete steps relative to the current directory, so that moving from `root` to `root/dir1/dir2` requires using `cd dir1` and then `cd dir2`, beginning at the root.

## Going Forward

I would like to add the ability to concatenate commands with && to allow for scripting. This could be done by parsing the command by the && symbol and passing the included commands and arguments recursively to the command prompt so that they are executed in order and without limit. I would of course also like to address the argument limit discussed above, which could be similarly parsed (by an empty space in this case) and then passed sequently to the command prompt to be passed to the relevant function.

## Running the Program and Tests

To run the program, simply fork and clone this repository. Navigate to the program's directory and run the command `python3 filesystem.py`. To test, run the command `python3 test.py`.
