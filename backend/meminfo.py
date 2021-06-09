
from pyzabbix import ZabbixAPI
import time

def get_meminfo():
    # 安装zabbix server的服务器ip
    ZABBIX_SERVER = 'http://192.168.2.144/zabbix'

    zapi = ZabbixAPI(ZABBIX_SERVER)

    zapi.login('Admin', 'zabbix')

    hostname_list = []
    hostid_list = []
    icmpvalue_list = []
    m = 0
    # host_info = {"name": []*2, "status": []*2, "address": []*2}

    mem_info = {"name": []*3, "date": []*3, "value": []*3}


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
            applicationids=application_list[3]["applicationid"], # 'system.cpu.load[percpu,avg5]
            output="extend",
        )

        print(item_list)
        print("++++++++++++++++++++++++++++++++")
        print()
        print()
        # print(item_list)
        memvalue = item_list[-1]["lastvalue"]
        lastclock = item_list[-1]["lastclock"]
        mem_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(lastclock)))
        

        mem_info["name"].append(host_list[m]["host"])
        mem_info["date"].append(mem_time)
        mem_info["value"].append(memvalue)
        m = m + 1
    mem_info_list = [{}]*m
    for n in range(m):
            mem_info_list[n] = {"name":mem_info["name"][n],"date":mem_info["date"][n],"value":mem_info["value"][n]}


    memInfo = {"data":mem_info_list}
    return memInfo

if  __name__  ==  '__main__':
    
    get_meminfo()
    






