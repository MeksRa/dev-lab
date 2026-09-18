# Developer`s Cheat Sheet

## Hot Keys Vs Code
* `Ctrl + Shift + P` - Command Palette
* `Shift + Alt + F` - Auto-formatting `Ruff`
* `Ctrl + ,` - Settings
* `Shift + Numpad+` - Increase font size
* `Shift + Numpad-` - Decrease font size
* `Numpad/` - Run a file
* `F2` - Rename all selected words

## Terminal
* `cls` - Clear the terminal
* `ctrl + C` - Stop the program
* `Ctrl + Backtick` - Open the Terminal

## Win Hot keys
* `win + .` - Windows Emoji

## Git Commands
* `git status`
* `git branch`
* `git add .`
* `git commit -m ""`
* `git push`
* `git mv old_name.py new_name.py`
* `git checkout -- file.py`
* `git log --oneline -n 3` - show the last 3 commits, each on a single line

## Git Undo Operations
* `git revert commit_hash` - Safely undoes a commit by creating a new commit (history stays intact) ==> after push
* `git reset --soft HEAD~1` -Undo last commit, keep changes staged in your workspace ==> before push
* `git reset --hard HEAD~1` - Undo last commit and DISCARD all changes 
(cannot be easily undone) ==> before push
* `git commit --amend -m "text"` - Change the last commit message
* `git restore --staged file_name` - Unstage file

## Git Connection
* `git config --global user.name 'username'`
* `git config --global user.email 'user.email@'`
* `git config user.name 'username'` => local
* `git config user.email 'user.email@'` => local
* `git config user.name` => check
* `git config user.email` => check
* `git config --list` => View all current Git configurations
* `git init`
* `git remote add origin https://github.com/login/repo-name.git` => Link local repo to GitHub
* `git remote -v` => Check remote repository status
* `git remote set-url origin https://github.com/login/repo-name.git` => Corrections if you're mistaken
* `git branch -M main` => Rename current branch to 'main' (GitHub standard)
* `git push -u origin main` => First push to main branch
* `git push` => Upload local commits to GitHub
* `git pull` => Download latest commits from GitHub

## .venv
* `git clone`
* `python -m venv .venv` - Create venv
* `.\.venv\Scripts\Activate.ps1` - Activate venv
* `deactivate`
* `pip install <smth>`
* `pip freeze > requirements.txt` - Create requirements
* `pip install -r requirements.txt` - Download requirements

## Commits
* `feat:` - A new feature
* `fix:` - A bug fix
* `docs:` - Documentation changes only
* `style:` - Code formatting, missing semi-colons
* `refactor:` - Code changes that neither fix a bug nor add a feature
* `chore:` - Maintenance tasks, updating dependencies, repository configs
* `test:` - Adding missing tests or correcting existing tests

## Commit Examples
* `feat: add module 02 numbers and operators`
* `fix: correct division by zero error`
* `docs: update cheat sheet with git config commands`
* `style: format 01_variables_and_types with ruff`
* `refactor: simplify variable assignment logic`
* `chore: update .gitignore and vscode settings`