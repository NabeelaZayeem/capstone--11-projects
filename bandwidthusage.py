import psutil
import matplotlib.pyplot as plt
 # Define the network interface to monitor
interface="eth0"
#retrieve the n/w usage statistics for the specific inetrface
net_io_counters=psutil.net_io_counters()
#interface_counters=net_io_counters.get(interface)
print(net_io_counters)

#calculate the amount of data received and sent in MB
bytes_received=net_io_counters.bytes_recv/1024/1024
bytes_sent=net_io_counters.bytes_sent/1024/1024
#create a bar chart of the network usage
plt.bar(["Received","sent"],[bytes_received,bytes_sent])
plt.ylabel("Network usage for interface{}".format(interface))
plt.show()
