from core.utils import get_ip,ip_validation,get_mask,mask_validation,subnet_range,decimal_to_binary,network_address_calc,assamble_network,print_all,add_to_file


def main():
    while True:
        ip = get_ip()
        if not ip_validation(ip):
            continue
        mask = get_mask()
        if not mask_validation(mask):
            continue
        break
    octets = subnet_range(ip,mask)
    binary_ip = decimal_to_binary(octets[0])
    binary_mask = decimal_to_binary(octets[1])
    network_octet = network_address_calc(binary_ip, binary_mask)
    network_address = assamble_network(ip,network_octet,octets[2] ) # octets[2] is the index of the octet that needs to be replaced
    print(print_all(ip,mask,network_address))
    add_to_file(ip,mask,network_address)


if __name__ == '__main__':
    main()