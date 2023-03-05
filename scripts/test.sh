export PYTHONPATH='.'
export PYTHONENV='test'
pytest -s -vvvv $1 $2
