#!/bin/bash
##批量添加用户脚本##
##交互方式读取用户前缀和用户数##
##密码也采用交互输入，用户密码为密码前缀+用户序号
##作者：Barlow##
##最后修改时间：2013-3-18##
#
#建立用户
echo "Please input username:"
read name
echo "Please input number of users:"
read num
n=1
while [ $n -le $num ]
do
/usr/sbin/useradd $name$n > /dev/null
##这里也可以将新建用户加入某个组，如sshd组以让其可以使用ssh登录
/usr/sbin/usermod -G sshd $name$n
n=`expr $n + 1`
done
# 修改密码
echo "Please input the password:"
read passwd
m=1
while [ $m -le $num ]
do
echo $passwd$m | /usr/bin/passwd --stdin $name$m > /dev/null
m=`expr $m + 1`
done
exit
