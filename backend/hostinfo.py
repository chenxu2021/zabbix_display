
from pyzabbix import ZabbixAPI


def get_hostinfo():
    # 安装zabbix server的服务器ip
    ZABBIX_SERVER = 'http://192.168.2.144/zabbix'

    zapi = ZabbixAPI(ZABBIX_SERVER)

    zapi.login('Admin', 'zabbix')

    hostname_list = []
    hostid_list = []
    icmpvalue_list = []
    m = 0
    host_info = {"name": []*2, "status": []*2,"address":[]*2}

    
    # 获取主机
    host_list = zapi.host.get(
        output="extend",
    )
    print(host_list[0])

    # print(host_list)
    for i in range(len(host_list)):
        hostname_list.append(host_list[i]["host"])
        hostid_list.append(host_list[i]["hostid"])
    
    # print(hostname_list)
    # print(hostid_list)

    # 获取触发器
    triggers = zapi.trigger.get(
        output="extend",
        selectHosts=['host'],
    )

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
        # 获取监控项
        item_list = zapi.item.get(
            hostids=hostid,
            applicationids=application_list[-2]["applicationid"],
            output="extend",
        )
        print(item_list[0])
        icmpvalue = item_list[0]["lastvalue"]
        icmpvalue_list.append(icmpvalue)
    # print(icmpvalue_list)

        
        host_info["name"].append(host_list[m]["host"])
        host_info["address"].append(host_list[m]["name"])
        host_info["status"].append(item_list[0]["lastvalue"])
        m = m + 1
    # print(host_info_list)
    host_info_list = [{}]*m

    for n in range(m):
        host_info_list[n] = {"name":host_info["name"][n],"status":host_info["status"][n],"address":host_info["address"][n]}
    # host_info_list[0] = {"name":host_info["name"][0],"status":host_info["status"][0]}
    # print(host_info_list)
    # host_info_list[1] = {"name":host_info["name"][1],"status":host_info["status"][1]}
    # print(host_info["name"][1])
    # print(host_info["status"][1])
    # print(host_info_list)
    hostinfo = {"data":host_info_list}
    # print(hostinfo)
    return hostinfo
        # print(m)
        # print(host_info_list)
        # host_info_list.append(host_info)
        
    # hostinfo = dict(zip(hostname_list,icmpvalue_list))
        
        
    # print(host_info_list)
    # print(hostinfo)
    # return hostinfo


if  __name__  ==  '__main__':
    
    get_hostinfo()



 

 
# # 获取模板
# template = zapi.template.get(
#     output="extend",
# )

