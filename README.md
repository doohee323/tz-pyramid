# tzpyramid

tzpyramid
========

export VENV=~/env
python3 -m venv $VENV
$VENV/bin/pip install "pyramid==1.9.1"
brew install cookiecutter
cookiecutter gh:Pylons/pyramid-cookiecutter-starter --checkout 1.9-branch

Getting Started
---------------

- Change directory into your newly created project.

    cd tzpyramid

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini
    
- in Eclipse
	add /tzpyramid/env/lib/python3.4/site-packages in PYTHONPATH
	run /tzpyramid/env/bin/pserve /Users/dhong/Documents/workspace/python/tzpyramid/development.ini
    
- Test
	http://localhost:6543
	http://localhost:6543/home2
	http://localhost:6543/rest
