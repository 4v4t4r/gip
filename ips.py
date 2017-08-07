from IPy import IP

#googleips_temp = open('item.txt','r')

googleips = open('ips.txt','a')

with open('item.txt','r') as f:
    for line in f.readlines():
        for ip in IP(line.strip()):
            with open('ips.txt','a') as f:
                f.write(str(ip) + "\n")
            print(ip)