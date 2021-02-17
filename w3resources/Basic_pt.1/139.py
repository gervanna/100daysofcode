#Write a Python program to valid an IP address.

#02_16_21

import ipaddress

test1 = ipaddress.ip_address('192.0.2.1')
test2 = ipaddress.ip_address('2001:db8::1')
test3 = "loki"
test4 = [676767, 9, "l"]

def check_IPv(address):
    try:
        address_version = address.version
        if address_version == 4:
            print(f"Valid IPv{address_version} address.")
        elif address_version == 6:
            print(f"Valid IPv{address_version} address.")
        return address_version
    except AttributeError:
        print("Not a valid IPv4 address.")
        
check_IPv(test1)
check_IPv(test2)
check_IPv(test3)
check_IPv(test4)

#can also import and use socket