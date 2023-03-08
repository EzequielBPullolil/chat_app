export PYTHONPATH='.'
export PYTHONENV='test'


export MONGODB_URI='mongodb://localhost:27017'
export MONGODB_NAME='chat_app'
pytest -s -vvvv $1 $2
