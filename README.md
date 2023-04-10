<h1>Github auto-message-commit</h1>

Create auto-message-commit app.


<h1>Logic</h1>
Checking all files changed by git add *.

If new file:
-	find all functions and name + arguments + return + comment on first lines after definition

If updated file:

-	if new function:
	name + arguments + return + comment on first lines after definition
-    if updated function:
	check name + arguments + return + comment on first lines after definition what changed or content of function changed
-    if deleted function:

If deleted file:
-    name of file + names of functions


<h1>TODO:</h1>
- [ ] Check what git commands use
- [ ] Check what status of edits of files exists on git (new, modified, deleted)
- [ ] How to get context of git commands in python
- [ ] Create script for adding *, commiting and pushing if commit message != old one
- [X] How to commit using file or other way - git commit -F <file>
 


<h1>git commit</h1>

        [-a | --interactive | --patch] [-s] [-v] [-u<mode>] [--amend]

        [--dry-run] [(-c | -C | --squash) <commit> | --fixup [(amend|reword):]<commit>)]
        [-F <file> | -m <msg>] [--reset-author] [--allow-empty]
        [--allow-empty-message] [--no-verify] [-e] [--author=<author>]
        [--date=<date>] [--cleanup=<mode>] [--[no-]status]
        [-i | -o] [--pathspec-from-file=<file> [--pathspec-file-nul]]
        [(--trailer <token>[(=|:)<value>])…​] [-S[<keyid>]]
        [--] [<pathspec>…​]


        --template=<file>
        When editing the commit message, start the editor with the contents in the given file. The commit.template configuration variable is often used to give this option implicitly to the command. This mechanism can be used by projects that want to guide participants with some hints on what to write in the message in what order. If the user exits the editor without editing the message, the commit is aborted. This has no effect when a message is given by other means, e.g. with the -m or -F options.


<h2>Git status after creating file and add tracking to it:</h2>
On branch main
Your branch is up to date with 'origin/main'.


Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   test_file

<h2>Git status after creating python_testing_for-status.py, changing README.md and deleting test_file:</h2>
On branch main
Your branch is up to date with 'origin/main'.


Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md
	modified:   test.txt
	deleted:    test_file


Untracked files:
  (use "git add <file>..." to include in what will be committed)
	python_testing_for_status.py


no changes added to commit (use "git add" and/or "git commit -a")


<h2>Git status after adding tracking of changes by git add *:</h2>
On branch main
Your branch is up to date with 'origin/main'.


Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   README.md
	new file:   python_testing_for_status.py
	modified:   test.txt


Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	deleted:    test_file
