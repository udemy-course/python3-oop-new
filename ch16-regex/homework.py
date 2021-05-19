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
    r"^interface (?P<name>\w+)\n"
    r"( .*\n)*"
    r" ip address (?P<ip>\S+) (?P<mask>\S+)\n",
    raw_string,
    re.MULTILINE)

for part in interface_descriptions:
    print(part.groupdict())
    # print(part.group('int_name'), part.group('ip'), part.group('mask'))


