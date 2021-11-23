import sys
import wmi
import socket

def fnt_internet(host, port, timeout): 
    try: 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, int(port)))
        return True 
    except Exception as ex: 
        print(ex) 
        return False 


# Obtain network adaptors configurations
nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

for i in range(len(nic_configs)):
    #print(i+1, "번째 어댑터, ", nic_configs[i])
    print(i+1, "번째 어댑터, ", nic_configs[i].wmi_property("Description").value, "\n", nic_configs[i].wmi_property("IPAddress").value)

selection = input("어탭터 번호를 입력해주세요\n")

if not selection.isnumeric():
    print('잘못된 입력 값입니다')
    sys.exit()

selected_index = int(selection) - 1

# sys.exit()

# First network adaptor
nic = nic_configs[selected_index]

ip = input('시작할 IP주소를 입력해주세요\n')
subnetmask = input('설정할 서브넷마스크를 입력해주세요\n')
gateway = input('설정할 게이트웨이를 입력해주세요\n')

print('작업을 시작합니다\n')

splitIp = ip.split('.')
startIpEnd = splitIp[3]

for i in range(int(startIpEnd), 256):
    splitIp[3] = str(i)
    combinedIp = '.'.join(splitIp)
    print('시도중...', combinedIp)

    # nic.EnableStatic(IPAddress=[combinedIp], SubnetMask=[subnetmask])
    # nic.SetGateways(DefaultIPGateway=[gateway])

    result = fnt_internet("google.com", 80, 10)
    print(result)
    if result == True:
        break

print('종료')
print('마지막으로 설정한 IP주소는', '.'.join(splitIp), '입니다')

# IP address, subnetmask and gateway values should be unicode objects
# ip = '192.168.0.11'
# subnetmask = '255.255.255.0'
# gateway = '192.168.0.1'

# Set IP address, subnetmask and default gateway
# Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
# nic.EnableStatic(IPAddress=[ip], SubnetMask=[subnetmask])
# nic.SetGateways(DefaultIPGateway=[gateway])
