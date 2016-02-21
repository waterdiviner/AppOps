base_dir=..
echo ${base_dir}

backup_dir=${base_dir}/backup
echo ${backup_dir}
if [ -d "${backup_dir}" ]; then
	rm -rf ${backup_dir}
fi

log_dir=${base_dir}/log
echo ${log_dir}
if [ -d "${log_dir}" ]; then
	rm -rf ${log_dir}
fi