# Python Knowledge Share

Topic coverage.

## Code Design Patterns

- VIM demos
- Jupyter demos
- Script / Py File / Module / Package / setup.py / Installable
- Code style guides
- Structuring Scripts

## Python Development Environments

- Dependency isolation
- Developer tooling
	- Pyflakes checker
	- pycodestyle checker
	- Automated testing (later)
- IDE Choice
- Jupyter
	- Creating Python files for use in Jupyterhub Notebooks
		- Google Drive local synchronizing
		- Uploading to Google Drive
		- Choosing a working folder
	- Manual reloading
		- `from importlib import reload` - Gives you a reload function
		- `reload(modulename)` - Loads latest code from filesystem
	- Autoreloading
		- `%load_ext autoreload` - Enable autoreload extension
		- `%autoreload 2` - Reload everything all the time
	- Using Jupyter magic to make life easier
		- Jupyter magic cell at the top of the notebook
	- Using Kernel Restart & Run All
		- Simulates script execution
		- Slower than just a Run All
		- Clears all `%magic` not in your Jupyter profile
		- Gives clean runtime environment and namespaces
		- Binding to Restart & Run All to keyboard shortcut
	- Adding 3rd party packages to a running Server
		- Opening a new Terminal
		- `pip install <packagename>`
		- Package lifetime
		- Saving package list for reusing

