# homework

原始字符串如下：

```
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
```

## 1. 使用正则表达式找出所有的接口名称，interface name, 也就是Vlan8, Vlan9, Vlan10, ........

## 2. 使用正则表达式找出所有的IP地址， 也就是255.255.255.240， 255.255.255.252， 255.255.255.248

## 3. 使用正则表达式找出所有的IP掩码， 也就是192.168.3.50， 192.168.3.66， 192.168.3.582， ......

## 4. 使用正则表达式找出所有的接口名称和它的IP地址以及掩码，

result like

```
{'name': 'Vlan8', 'ip': '192.168.3.50', 'mask': '255.255.255.240'}
{'name': 'Vlan9', 'ip': '192.168.3.66', 'mask': '255.255.255.240'}
{'name': 'Vlan10', 'ip': '192.168.3.82', 'mask': '255.255.255.240'}
{'name': 'Vlan25', 'ip': '192.168.3.211', 'mask': '255.255.255.240'}
{'name': 'Vlan26', 'ip': '192.168.3.227', 'mask': '255.255.255.240'}
{'name': 'Vlan99', 'ip': '192.168.1.2', 'mask': '255.255.255.252'}
{'name': 'Vlan100', 'ip': '192.168.192.2', 'mask': '255.255.255.248'}
```

