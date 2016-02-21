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

#command para
#$1 --cmd     query
#$2 --type    1 is complete , 2 is secuinfo , 3 is position , 4 is account
#$3 --file    path and file

export LD_LIBRARY_PATH=../lib
if [ $1 == "gdb" ]; then
	gdb -args  ../bin/QGOnuca --envfile=$(pwd)/../cfg/$QTS_CFG_APP_FOLDER/entry/main_gw.qts $2 $3 $4
else
	../bin/QGOnuca --envfile=$(pwd)/../cfg/$QTS_CFG_APP_FOLDER/entry/main_gw.qts $1 $2 $3
fi