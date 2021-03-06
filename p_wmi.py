#!/usr/bin/env python
#coding:utf-8


import wmi
import sys,time,platform

def get_system_info(os):
    """
    獲取操作系統版本。
    """
    print
    print("Operating system:")
    if os == "Windows":
        c = wmi.WMI ()
        for sys in c.Win32_OperatingSystem():
            print('\t' + "Version :\t%s" % sys.Caption.encode("UTF-8"))
            print('\t' + "Vernum :\t%s" % sys.BuildNumber)

def get_memory_info(os):
    """
    獲取物理內存和虛擬內存。
    """
    print
    print("memory_info:")
    if os == "Windows":
        c = wmi.WMI ()
        cs = c.Win32_ComputerSystem()
        pfu = c.Win32_PageFileUsage()
        MemTotal = int(cs[0].TotalPhysicalMemory)/1024/1024
        print('\t' + "TotalPhysicalMemory :" + '\t' + str(MemTotal) + "M")
        #tmpdict["MemFree"] = int(os[0].FreePhysicalMemory)/1024
        SwapTotal = int(pfu[0].AllocatedBaseSize)
        print('\t' + "SwapTotal :" + '\t' + str(SwapTotal) + "M")
        #tmpdict["SwapFree"] = int(pfu[0].AllocatedBaseSize - pfu[0].CurrentUsage)

def get_disk_info(os):
    """
    獲取物理磁盤信息。
    """
    print
    print("disk_info:")
    if os == "Windows":
        tmplist = []
        c = wmi.WMI ()
        for physical_disk in c.Win32_DiskDrive():
            if physical_disk.Size:
                print('\t' + str(physical_disk.Caption) + ' :\t' + str(int(physical_disk.Size)/1024/1024/1024) + "G")

def get_cpu_info(os):
    """
    獲取CPU信息。
    """
    print
    print("cpu_info:")
    if os == "Windows":
        tmpdict = {}
        tmpdict["CpuCores"] = 0
        c = wmi.WMI ()
        for cpu in c.Win32_Processor():
            tmpdict["CpuType"] = cpu.Name
        try:
            tmpdict["CpuCores"] = cpu.NumberOfCores
        except:
            tmpdict["CpuCores"] += 1
            tmpdict["CpuClock"] = cpu.MaxClockSpeed
        print('\t' + 'CpuType :\t' + str(tmpdict["CpuType"]))
        print('\t' + 'CpuCores :\t' + str(tmpdict["CpuCores"]))


def get_network_info(os):
    """
    獲取網卡信息和當前TCP連接數。
    """
    print
    print("network_info:")
    if os == "Windows":
        tmplist = []
        c = wmi.WMI ()
        for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
                tmpdict = {}
                tmpdict["Description"] = interface.Description
                tmpdict["IPAddress"] = interface.IPAddress[0]
                tmpdict["IPSubnet"] = interface.IPSubnet[0]
                tmpdict["MAC"] = interface.MACAddress
                tmplist.append(tmpdict)
        for i in tmplist:
            print('\t' + i["Description"])
            print('\t' + '\t' + "MAC :" + '\t' + i["MAC"])
            print('\t' + '\t' + 'IPAddress :' + '\t' + i["IPAddress"])
            print('\t' + '\t' + "IPSubnet :" + '\t' + i["IPSubnet"])
        for interfacePerfTCP in c.Win32_PerfRawData_Tcpip_TCPv4():
                print('\t' + 'TCP Connect :\t' + str(interfacePerfTCP.ConnectionsEstablished))

    return
    
if __name__ == "__main__":
    os = platform.system()
    get_system_info(os)
    get_memory_info(os)
    get_disk_info(os)
    get_cpu_info(os)
    get_network_info(os)