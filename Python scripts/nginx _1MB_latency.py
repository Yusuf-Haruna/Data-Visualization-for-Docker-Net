import numpy as np
import matplotlib.pyplot as plt

nginx_host_lat = np.array([ 2.75
 ,2.44
 ,2.42
 ,2.44
 ,2.29
 ,2.32
 ,2.53
 ,2.72
 ,2.66
 ,2.55
 ,2.59
 ,2.42
 ,2.84
 ,2.67
 ,2.39
 ,3.14
 ,2.40
 ,2.65
 ,2.64
 ,2.48
 ,2.46
 ,2.56
 ,2.79
 ,2.80
 ,2.57
 ,2.34
 ,2.18
 ,2.08
 ,2.31
 ,2.43
])
nginx_NAT_lat = np.array([ 2.52
 ,2.92
 ,2.62
 ,2.50
 ,2.73
 ,2.67
 ,2.46
 ,2.61
 ,2.80
 ,2.73
 ,52.97
 ,2.58
 ,2.61
 ,2.64
 ,2.69
 ,2.74
 ,2.70
 ,2.77
 ,3.44
 ,3.07
 ,3.70
 ,2.73
 ,2.74
 ,2.51
 ,2.57
 ,2.44
 ,2.64
 ,2.74
 ,2.91
 ,2.64
])
nginx_VXLAN_lat = np.array([ 3.08
 ,3.43
 ,2.67
 ,2.72
 ,2.69
 ,2.72
 ,2.60
 ,3.41
 ,2.52
 ,2.60
 ,2.63
 ,2.46
 ,2.81
 ,3.16
 ,3.40
 ,2.84
 ,2.80
 ,2.57
 ,2.59
 ,3.48
 ,2.95
 ,2.70
 ,2.39
 ,2.72
 ,2.68
 ,2.92
 ,3.29
 ,2.87
 ,3.02
 ,3.76
])
nginx_weave_lat = np.array([ 2.65
 ,2.61
 ,2.50
 ,2.67
 ,2.68
 ,2.68
 ,2.58
 ,2.67
 ,2.54
 ,2.86
 ,3.00
 ,2.46
 ,2.50
 ,2.47
 ,2.72
 ,2.55
 ,2.37
 ,2.71
 ,2.58
 ,2.56
 ,2.55
 ,2.69
 ,2.45
 ,2.68
 ,2.70
 ,2.54
 ,2.39
 ,2.79
 ,2.63
 ,2.62
])

# calculate the average
nginx_host_lat_avg = np.mean(nginx_host_lat)
nginx_NAT_lat_avg = np.mean(nginx_NAT_lat)
nginx_VXLAN_lat_avg = np.mean(nginx_VXLAN_lat)
nginx_weave_lat_avg = np.mean(nginx_weave_lat)

# calculate the standard deviation
nginx_host_lat_std = np.std(nginx_host_lat)
nginx_NAT_lat_std = np.std(nginx_NAT_lat)
nginx_VXLAN_lat_std = np.std(nginx_VXLAN_lat)
nginx_weave_lat_std = np.std(nginx_weave_lat)

x = ["Host", "NAT", "VXLAN", "Weave"]
y = [nginx_host_lat_avg, nginx_NAT_lat_avg, nginx_VXLAN_lat_avg, nginx_weave_lat_avg]
error = [nginx_host_lat_std, nginx_NAT_lat_std, nginx_VXLAN_lat_std, nginx_weave_lat_std]

# plot the result
plt.bar(x, y, yerr=error, align='center', alpha=0.6, ecolor='black', capsize=5)
plt.title("Nginx 1MB file, 3K reqs/sec")
plt.ylabel("Latency (ms)")
plt.show()