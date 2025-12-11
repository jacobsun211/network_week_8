# from core.output_string import format_input_ip,format_subnet_mask,format_network_address




def get_ip():
    ip = input('please enter valid ip: ')
    return ip


def get_mask():
    mask = input('please enter valid mask: ')
    return mask




def ip_validation(ip):
    octets = ip.split('.') # octets is now a list: ['x', 'x', 'x', 'x']

    if len(octets) != 4:
        print('not enough .')
        return False
    for octet in octets:
        if int(octet) < 0 or int(octet) > 255:
            print('value must be between 0 - 255')
            return False
    return True


def mask_validation(mask):
    if ip_validation(mask): 
        octets = mask.split('.')
        past_255 = False
        for octet in octets:
            if octet != "255":
                past_255 = True
            elif past_255: # checks if the mask is looking like this: 255.142.255.255, returns False if it does
                print('please enter VALID mask')
                return False
        return True
    return False

def decimal_to_binary(decimal_num, length = 8):
    decimal_num = int(decimal_num)
    if decimal_num < 0 or decimal_num >= 2 ** length:
        return None
    
    if decimal_num == 0:
        result = "0"
    else:
        result = ""
        n = decimal_num
        while n > 0:
            result = str(n % 2) + result
            n //= 2
    
    return result.zfill(length)


def binary_to_decimal(binary_str):
    value = 0
    for bit in binary_str:
        value = value * 2 + int(bit)
    return value


def subnet_range(ip,mask): # this func search for the first octet that isnt 255 so we know where the host starts
    octets = mask.split('.')
    for index,octet in enumerate(octets):
        if octet != '255':
            ip = ip.split('.')
            octet_ip = ip[index]
            return [octet_ip,octet,index]



def network_address_calc(binary_ip, binary_mask):
    binary_ip,binary_mask = str(binary_ip),str(binary_mask)
    binary_network = ''
    for bit in range(8):
        if binary_ip[bit] == '1' and binary_mask[bit] == '1':
            binary_network += '1'
        else:
            binary_network += '0'
    network = binary_to_decimal(binary_network)
    return network

def assamble_network(ip,octet,index): # this func replace the old ip with the calculated with AND to build the ip of the network
    ip_as_list = ip.split('.')
    ip_as_list[index] = octet

    network_ip = ''
    for octet in ip_as_list:
        network_ip += str(octet)
        network_ip += '.'
    network_ip = network_ip[:-1]
    return network_ip


def format_input_ip(ip_str):
    return f"Input IP: {ip_str}\n"


def format_subnet_mask(mask_str):
    return f"Subnet Mask: {mask_str}\n"

def format_network_address(network_address):
    return f"Network Address: {network_address}\n"



def print_all(ip,mask,network_address):
    ip = format_input_ip(ip)
    mask = format_subnet_mask(mask)
    network_address = format_network_address(network_address)
    print(ip,mask,network_address)
    return [ip,mask,network_address]


def add_to_file(ip,mask,network_address):
    report = print_all(ip,mask,network_address)
    with open(f'subnet_info_{str(ip)}_325606481.txt','a')as file:
        file.write(report[0])
        file.write(report[1])
        file.write(report[2])













