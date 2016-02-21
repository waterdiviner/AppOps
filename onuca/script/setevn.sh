if [ -z $1 ]; then
	src_dir=/home/jack/Develop/thirdpart/linux/lib/
	cur_dir=/home/jack/Develop/build/Debug/dist/
else
	src_dir=$1/thirdpart/linux/lib/
	cur_dir=$1/build/Debug/dist/
fi
echo ${src_dir}
echo ${cur_dir}

############################################################
cd "${src_dir}""boost"
sudo chmod 777 compileenv.sh
./compileenv.sh

cd "${src_dir}""python"
sudo chmod 777 compileenv.sh
./compileenv.sh

cd "${src_dir}""rabbitmq"
sudo chmod 777 compileenv.sh
./compileenv.sh

cd "${src_dir}""sqlite"
sudo chmod 777 compileenv.sh
./compileenv.sh

cd "${src_dir}""mysql"
sudo chmod 777 compileenv.sh
./compileenv.sh

cd "${cur_dir}"