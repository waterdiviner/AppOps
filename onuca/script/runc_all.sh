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
	gdb -args  ../bin/QGGui --envfile=$(pwd)/../cfg/$QTS_CFG_APP_FOLDER/entry/main_all.qts
else
	#para list: --bg=true(false)      run in background
	#			--tracemessage=true(false)
	#			--tracedebug=true(false)
	#			--traceerror=true(false)
	#			--tracewarning=true(false)
	#			--logmessage=true(false)
	#			--logdebug=true(false)
	#			--logerror=true(false)
	#			--logwarning=true(false)
	../bin/QGGui --envfile=$(pwd)/../cfg/$QTS_CFG_APP_FOLDER/entry/main_all.qts
fi
