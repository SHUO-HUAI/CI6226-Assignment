import os


def GetMemory(pid, pyname):
    command = "ps -aux | grep "
    command = command + str(pyname)
    r = os.popen(command)
    info = r.readlines()

    for line in info:
        tmps = str(line).split()
        pid_tmp = tmps[1]
        if pid_tmp == str(pid):
            return int(tmps[5])
