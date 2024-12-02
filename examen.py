from netmiko import ConnectHandler

cisco_router = {
    'device_type': 'cisco_ios',
    'host': 'sandbox-iosxe-latest-1.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    'po396rt': 22,
}

connexion = ConnectHandler(**cisco_router)


clock = connexion.send_command("show clock")
print(clock)

interface = connexion.send_command("sh ip int br")
with open ('interfaces.txt' , "w") as f:
    f.write(interface)

#Configure une interface loopback ayant l'adresse ip 10.8.8.8/28 (passez en mode
#6de configuration globale, int loopback, ip address ?)

param = [  'interface loopback',
           'ip address 10.8.8.8',
           'exit'
         ]

loop = connexion.send_config_set(param)
print(loop)














