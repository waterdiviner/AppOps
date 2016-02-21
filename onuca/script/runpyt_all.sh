export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(pwd)/../lib
export PYTHONPATH=$PYTHONPATH:$(pwd)/../pylib

#debug/release/publish
export QTS_APP_PY_VERSION=publish
#Debug/Release/.
export QTS_VERSION=.
#set trade date
#export QTS_TRADE_DATE=`date +%Y%m%d`

export QTS_REPLAY_PATH=$(pwd)/../market
export QTS_BASE_PATH=$(pwd)/..

#set data folder
#export QTS_DATA_APP_FOLDER=
#set cfg folder
#export QTS_CFG_APP_FOLDER=

cd $(pwd)/../cfg/$QTS_CFG_APP_FOLDER/entry

python entrydt_all.py

if [ -z $QTS_CFG_APP_FOLDER ]; then
	cd $(pwd)/../../script
else
	cd $(pwd)/../../../script
fi