export PYTHONPATH='.'
export PYTHONENV='test'


export MONGODB_URI='mongodb://localhost:27017'
export MONGODB_NAME='chat_app'

clear
echo "test start with PYTHONPATH=${PYTHONPATH} and PYTHONENV=${PYTHONENV}"
echo "And MONGODB_URI=${MONGODB_URI} and MONGODB_NAME=${MONGODB_NAME}"
sleep 2
pytest -s -vvvv $1 $2
