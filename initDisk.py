import paramiko
import yaml
# import socket

ip="192.168.253.130"
user="root"
password="211314"
hostname="wwt"

# paramiko.util.log_to_file('./log.log')

param={"path":"/dev/sdb","patition":{"name":"/dev/sdb1","size":"500M"}}
def getParams():
    with open(r'./initDisk.yaml') as f:
        params=yaml.load(f)
    print(params)


def login(ip,user,password,port):
    try:
        # trans=paramiko.Transport((ip,22))
        # trans.connect(username=user,password=password)
        ssh=paramiko.SSHClient()
        # ssh._transport=trans
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,user,password)
        
        return ssh
    except Exception as e:
        print(e)
        exit(0)
    # ssh.connect(ip,22,user,password)
    # chan=ssh.get_transport().open_session()
    # chan.get_pty()
    # f=chan.makefile()

def sftpToRemote(conn):
    sftp=conn.open_sftp()
    # put(localpath,remotepath)
    # get(remotepath,localpath)
    sftp.put('./log.log','/home/wwtfly/log.log')
    sftp.close()

def modHostname(conn,cmd):
    print("hostname is modify to %s ..." %hostname)
    try:
        stdin,stdout,stderr=conn.exec_command('hostnamectl set-hostname %s\n' %hostname)
        # conn.send('%s\n' %password)
        # stdin.write('%s\n' %password)
        # stdin.flush()
        if stdout.read() is None:
            print("modify done!")
    except Exception as e:
        print(e)
    conn.close()

def modDisk(conn,param,cmd):
    # channel=conn.invoke_shell()
    # interactive.interactive_shell(channel)
    print("create disk patition :%s ..." %param["path"])
    
    stdin,stdout,stderr=conn.exec_command(cmd)
    # if stderr != None:
    #     for i in stderr.read().splitlines():
    #         print(i.decode('utf-8'))
    #     exit(0)
    # stdin.write('%s\n' %password)
    # channel.send('df -h\r')
    # buff=''
    # x=u(channel.recv(1024))
    stdin.write('%s\n' %password)
    # s=stdout.channel.recv(1024)
    # print(s)
    # stdin.channel.send('m\n')
    # stdin.write('m\n')
    # stdin.flush()
    for i in stdout.read().splitlines():
        print(i.decode('utf-8'))

    # sys.stdout.write(x)   # 写入缓冲区
    # sys.stdout.flush()    # 刷新，将缓冲区内容显示出来




# ssh=login(ip,user,password,22)
# stdin,stdout,stderr=ssh.exec_command('sudo -S %s\n' %cmd)
# stdin.write('%s\n' %password)
# stdin.write('m')
# for i in stdout.read().splitlines():
#     print(i.decode('utf-8'))
# ssh.close()

if __name__ == "__main__":
    conn=login(ip,user,password,22)
    # cmd="bash /home/wwtfly/formatDisk.sh /dev/sdb +100M sdb2 /dev/sdb2"
    # cmd="df -h"
    # modHostname(conn,cmd)
    # for i in range(3):
    #     cmd="bash /home/wwtfly/formatDisk.sh /dev/sdb +100M sdb%d /dev/sdb%d" %(i+1,i+1)
    #     # cmd="df -h"
    #     print(cmd)
    #     modDisk(conn,param,cmd)
    sftpToRemote(conn)
    conn.close()