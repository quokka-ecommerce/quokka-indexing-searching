#!/usr/bin/env bash

solr_name="solr-5.4.0"
current_dir=`pwd`
base_dir=${current_dir}/quokka_solr
solr_conf_location=${base_dir}/${solr_name}/server/solr/quokka-search/conf/

# download solr
mkdir quokka_solr
mkdir ${base_dir}/tmp


#curl -O http://apache.mirrors.lucidnetworks.net/lucene/solr/5.4.0/solr-5.4.0.zip ./tmp
pwd
cp ~/Documents/asana/solr-5.4.0.zip ${base_dir}/tmp
unzip ${base_dir}/tmp/solr-5.4.0.zip -d ${base_dir}/

# start solr
${base_dir}/${solr_name}/bin/solr start

# create new core
${base_dir}/${solr_name}/bin/solr create -c quokka-search -p 8983

# copy config and lib
cp -R ${current_dir}/conf/solr_conf/* ${base_dir}/${solr_name}/server/solr/quokka-search/conf/
cp -R ${current_dir}/lib/* ${base_dir}/${solr_name}/server/ex_lib/
cp -R ${current_dir}/lib/* ${base_dir}/quokka_solr/${solr_name}/server/solr-webapp/webapp/WEB-INF/ex_lib/




