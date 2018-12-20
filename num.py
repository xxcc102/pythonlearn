import socket


def get_ip_status(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # print(port)
        server.connect((ip, port))
        print('ip {0} port {1} is open'.format(ip,port))
    except Exception as err:
        pass
        # print('port {0} is not open'.format(port))
    finally:
        server.close()


if __name__ == '__main__':
    host1 = '209.250.237.134'
    host2 = '144.202.82.195'
    socket.setdefaulttimeout(1)
    get_ip_status(host1, 8080)



    for port in range(20, 65000):
        get_ip_status(host1, port)
        get_ip_status(host2, port)
    print("end")

# with open("1.txt", 'w', encoding='utf-8') as f:
#     for i in range(1,65000):
#         f.write(str(i) + ",")
#
# f.close()
