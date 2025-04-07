import pywifi
import time
import json
import datetime
import msvcrt


def wifi_scan():
    now = datetime.datetime.now()
    wifi = pywifi.PyWiFi()
    iface =wifi.interfaces()[0]
    iface.scan()
    time.sleep(2)
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
    BUPT_wifi = "BUPT_networks1.json"
    while True:
        networks = wifi_scan()
        all_networks.append(networks)
        with open(BUPT_wifi, "w", encoding="utf-8") as file:
            json.dump(all_networks, file, ensure_ascii=False, indent=4)
        
        print("目前的校园网络：")
        for net in networks:
            print(f"SSID: {net['ssid']}, BSSID: {net['bssid']}, 信号强度: {net['signal']}")
        
        print("\n按 Enter 继续扫描，按 Backspace 撤销上一次记录并继续")
        key = msvcrt.getch()
        # Enter 键通常返回 b'\r'
        if key == b'\r':
            # 等待后续循环
            continue
        # Backspace 键返回 b'\x08'
        elif key == b'\x08':
            if all_networks:
                all_networks.pop()
                with open(BUPT_wifi, "w", encoding="utf-8") as file:
                    json.dump(all_networks, file, ensure_ascii=False, indent=4)
                print("已撤销上一次记录。")
            else:
                print("无可撤销的记录。")
        
        # 增加一个短暂延时，以避免连续按键带来的问题
        time.sleep(0.5)

if __name__ == '__main__':
   main()
