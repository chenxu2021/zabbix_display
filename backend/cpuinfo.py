
from pyzabbix import ZabbixAPI
import time

def get_cpuinfo():
    # 安装zabbix server的服务器ip
    ZABBIX_SERVER = 'http://192.168.2.144/zabbix'

    zapi = ZabbixAPI(ZABBIX_SERVER)

    zapi.login('Admin', 'zabbix')

    hostname_list = []
    hostid_list = []
    icmpvalue_list = []
    m = 0
    # host_info = {"name": []*2, "status": []*2, "address": []*2}

    cpu_info = {"name": []*3, "date": []*3, "value": []*3}


    # 获取主机
    host_list = zapi.host.get(
        output="extend",
        )
    # print(host_list[0])

    # print(host_list)
    for i in range(len(host_list)):
        hostname_list.append(host_list[i]["host"])
        hostid_list.append(host_list[i]["hostid"])

    # print(hostname_list)
    # print(hostid_list)

    # 获取触发器
    # triggers = zapi.trigger.get(
    #     output="extend",
    #     selectHosts=['host'],
    # )

    # 获取应用
    application_list = zapi.application.get(
        hostids='',
        output="extend",
    )

    for hostid in hostid_list:
        application_list = zapi.application.get(
            hostids=hostid,
            output="extend",
        )
        # print(application_list)
        # print("++++++++++++++++++++++++++++++++")
        # print()
        # print()
        # 获取监控项
        item_list = zapi.item.get(
            hostids=hostid,
            applicationids=application_list[0]["applicationid"], # 'system.cpu.load[percpu,avg5]
            output="extend",
        )

        # print(item_list)
        # print("++++++++++++++++++++++++++++++++")
        # print()
        # print()
        # print(item_list)
        cpuvalue = item_list[3]["lastvalue"]
        lastclock = item_list[3]["lastclock"]
        cpu_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(lastclock)))
        

        cpu_info["name"].append(host_list[m]["host"])
        cpu_info["date"].append(cpu_time)
        cpu_info["value"].append(cpuvalue)
        m = m + 1
    cpu_info_list = [{}]*m
    for n in range(m):
            cpu_info_list[n] = {"name":cpu_info["name"][n],"date":cpu_info["date"][n],"value":cpu_info["value"][n]}


    cpuInfo = {"data":cpu_info_list}
    return cpuInfo

if  __name__  ==  '__main__':
    
    get_cpuinfo()
    






