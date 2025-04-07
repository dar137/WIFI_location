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

def main():
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

if __name__ == '__main__':
   main()
