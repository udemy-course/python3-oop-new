import re


raw_string = """
interface Vlan8
 ip address 192.168.3.50 255.255.255.240
 no ip redirects
 no ip unreachables
 no ip proxy-arp
!
interface Vlan9
 ip address 192.168.3.66 255.255.255.240
 no ip redirects
 no ip unreachables
 no ip proxy-arp
!
interface Vlan10
 ip address 192.168.3.82 255.255.255.240
 no ip redirects
 no ip unreachables
 no ip proxy-arp
!
interface Vlan25
 ip address 192.168.3.211 255.255.255.240
 no ip redirects
 no ip unreachables
 no ip proxy-arp
!
interface Vlan26
 ip address 192.168.3.227 255.255.255.240
 no ip redirects
 no ip unreachables
 no ip proxy-arp
!
interface Vlan99
 bandwidth 10000000
 ip address 192.168.1.2 255.255.255.252
 no ip redirects
 no ip unreachables
 no ip proxy-arp
!
interface Vlan100
 ip address 192.168.192.2 255.255.255.248
 no ip redirects
 no ip unreachables
 no ip proxy-arp
"""


interface_descriptions = re.finditer(
    r"^interface (?P<int_name>\w+)\n"
    r"( .*\n)*"
    r" ip address (?P<ip>\S+) (?P<mask>\S+)\n",
    raw_string,
    re.MULTILINE)

for part in interface_descriptions:
    print(part.groupdict())
    # print(part.group('int_name'), part.group('ip'), part.group('mask'))


"""
PS C:\Users\Peng Xiao\python3-oop-new\ch16-regex> python .\homework.py
{'int_name': 'Vlan8', 'ip': '192.168.3.50', 'mask': '255.255.255.240'}
{'int_name': 'Vlan9', 'ip': '192.168.3.66', 'mask': '255.255.255.240'}
{'int_name': 'Vlan10', 'ip': '192.168.3.82', 'mask': '255.255.255.240'}
{'int_name': 'Vlan25', 'ip': '192.168.3.211', 'mask': '255.255.255.240'}
{'int_name': 'Vlan26', 'ip': '192.168.3.227', 'mask': '255.255.255.240'}
{'int_name': 'Vlan99', 'ip': '192.168.1.2', 'mask': '255.255.255.252'}
{'int_name': 'Vlan100', 'ip': '192.168.192.2', 'mask': '255.255.255.248'}
"""

