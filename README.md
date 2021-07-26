# Project
This project is an aplication web that changes data with Zabbix software through Zabbix's API in order to add other specific commands to the server monitoring which makes access control management easier and more practical to improve efficiency and rapidity.
####################################################################
######prerequisite#####
# cofiguration of zabbix_agentd.conf INSTALLED IN MASTER SERVER
In the file we locate the UserParameters attributes and we set them to create our specific command
  UserParameter=run[*],python3 /home/mahmoud/PycharmProjects/pythonProject4/$1
  UserParameter=version.pkg[*],dpkg --status $1 | grep -E '^(Version|Package)'
  UserParameter=size[*],du -sh $1
  UserParameter=subsize[*],du -h $1
  UserParameter=rm[*],sudo rmdir  $1
  UserParameter=mk[*],sudo mkdir  $1
  UserParameter=top[*],top -b -n1| grep $1
 # add a specific zabbix item
 ####################################################################
 Run Project.py
  
