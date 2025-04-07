import pywifi
import time
import json
import datetime

def wifi_scan():
    now = datetime.datetime.now()
    wifi = pywifi.PyWiFi()
    iface =wifi.interfaces()[0]
    iface.scan()
    results = iface.scan_results()
    BUPT_networks = []
    for network in results:
        ssid = network.ssid
        if ssid.startswith("BUPT"):
            BUPT_networks.append({
                "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
                "ssid": ssid,
                "bssid":network.bssid,
                "signal":network.signal,
            })
    return BUPT_networks
    # fingerprint = {
    #     "data": "BUPT_networks",
    #     "timestamp": time.time()
    # }
    # return fingerprint

def main():
    # now = datetime.datetime.now()
    # BUPT_wifi = "BUPT_networks.json"
    # data_list = []
    # while True:
    #     networks = wifi_scan()
    #     data_list.append(networks)
    #     with open(BUPT_wifi, "w", encoding="utf-8") as file:
    #         json.dump(data_list, file, ensure_ascii=False, indent=4)
    #         time.sleep(2)
    
    all_networks = []
    while True:
        networks = wifi_scan()
        all_networks.append(networks)
        BUPT_wifi = "BUPT_networks.json"
        with open(BUPT_wifi,"w", encoding="utf-8") as file:
            json.dump(all_networks, file, ensure_ascii=False, indent=4)
        print("目前的校园网络：")
        for net in networks:
            print(f"SSID:{net["ssid"]}, BSSID:{net["bssid"]}, 信号强度:{net["signal"]}")
        time.sleep(2)
        # else:
        #     # print("没有发现校园网络")

if __name__ == '__main__':
   main()
