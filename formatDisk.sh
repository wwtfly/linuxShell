#! /bin/bash
diskname=$1
disksize=$2
name=$3
partitionname=$4

/usr/bin/expect <<!
#set timeout -1
spawn fdisk $diskname
expect "m for help"
exec sleep 0.5
send "n\r"
expect "Select (default p)"
send "p\r"
expect "Partition number*"
send "\r"
expect "First sector*"
send "\r"
expect "Last sector*"
send "$disksize\r"
expect "m for help"
exec sleep 0.5
send "t\r"
send "\r"
expect "Hex code (type L to list all codes)*"
send "8e\r"
expect "m for help"
exec sleep 0.5
send "w\r"
send "q\r"
expect eof
!


pvcreate ${partitionname}
vgcreate -s 8M ${name}_vg $partitionname
fs=`vgdisplay ${name}_vg|grep Free*|awk '{print $5}'|sed s/[[:space:]]//g`
lvcreate -l $fs -n ${name}_lvm ${name}_vg
#mkfs.ext4 $diskname
