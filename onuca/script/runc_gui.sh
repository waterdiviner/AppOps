#ulimit -c unlimited

#debug/release/publish
export QTS_APP_PY_VERSION=publish
#Debug/Release/.
export QTS_VERSION=.
#set trade date
#export QTS_TRADE_DATE=`date +%Y%m%d`

#set data folder
#export QTS_DATA_APP_FOLDER=
#set cfg folder
#export QTS_CFG_APP_FOLDER=

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:../thirdpart/mysql:../thirdpart/boost:../thirdpart/sqlite:../thirdpart/rabbitmq:../lib:../gui:../thirdpart/python
if [ $1 == "gdb" ]; then
	gdb -args  ../bin/QGGui --envfile=$(pwd)/../cfg/$QTS_CFG_APP_FOLDER/entry/main_gui.qts
else
	../bin/QGGui --envfile=$(pwd)/../cfg/$QTS_CFG_APP_FOLDER/entry/main_gui.qts
fi
