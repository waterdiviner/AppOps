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
#$1 --cmd   btox  or xtob
#$2 --type  1  record 
#			2  position
#			3  account
#			4  working
#$3 --source   source path and file
#$4 --target   target path and file

if [ $1 == "gdb" ]; then
	gdb -args  ../bin/QGOnuca --envfile=$(pwd)/../cfg/$QTS_CFG_APP_FOLDER/entry/main_convert.qts $2 $3 $4 $5
else
	../bin/QGOnuca --envfile=$(pwd)/../cfg/$QTS_CFG_APP_FOLDER/entry/main_convert.qts $1 $2 $3 $4
fi