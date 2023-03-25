from os import system, remove
from ipaddress import ip_address


def get_ip_address():
    tmp = 'tmp'

    command = f"wmic path win32_networkadapterconfiguration where \"IPEnabled=True\" get caption,ipaddress > {tmp}"

    system(command)

    with open(f"{tmp}", encoding='utf-16') as f:
        lines = f.read().strip().split('\n')[1:]
        for line in lines:
            line = ''.join(line.strip().split(']')[1:])
            left, right = line.split('{')
            adapter = left.strip()
            address = right.strip().replace('"', '').replace('}', '')
            print(f"adapter:{adapter}, address:{address}")
        f.close()
    remove(tmp)


def check_ip(address: str):
    try:
        return ip_address(address)
    except:
        return None


if __name__ == '__main__':
    get_ip_address()
