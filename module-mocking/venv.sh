if [[ -d "./.venv" ]]; then
    echo "Updating package install..."
    if [[ -e "./.venv/Scripts/activate" ]]; then
        source ./.venv/Scripts/activate
    elif [[ -e "./.venv/bin/activate" ]]; then
        source ./.venv/bin/activate
    else
        echo "Cannot find activation script"
        exit 2
    fi
    echo "Updating project dependencies to latest constraint levels defined in 'pyproject.toml'"
    poetry update
    echo "Listing all outdated dependencies regardless of constraint level"
    poetry show -o
else
    echo "Installing tool dependencies..."
    pip install tox poetry
    echo "Creating virtual environment..."
    python -m venv --upgrade-deps ./.venv

    if [[ -e "./.venv/Scripts/activate" ]]; then
        source ./.venv/Scripts/activate
    elif [[ -e "./.venv/bin/activate" ]]; then
        source ./.venv/bin/activate
    else
        echo "Cannot find activation script"
        exit 2
    fi

    echo "Python being used at $(which python)"
    echo "Upgrading pip"
    python -m pip install --upgrade pip

    echo "Installing project dependencies..."
    poetry install
    echo "Listing all outdated dependencies regardless of constraint level"
    poetry show -o
fi