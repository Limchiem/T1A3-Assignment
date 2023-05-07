# !/bin/bash
# Check if python is installed
[[ "$(python3 -V)" =~ "Python 3" ]] && echo "Python 3 is installed"

echo "go to https://www.python.org/downloads/ if not installed."

# check if venv exist
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "No VIRTUAL_ENV set"
else
    echo "VIRTUAL_ENV is set"
fi