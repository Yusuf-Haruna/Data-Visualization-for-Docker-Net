import numpy as np
import matplotlib.pyplot as plt

nginx_host_lat = np.array([ 3.37
 ,3.33
 ,3.23
 ,3.36
 ,3.35
 ,3.31
 ,3.34
 ,3.48
 ,3.32
 ,3.31
 ,3.34
 ,3.30
 ,3.26
 ,3.32
 ,3.30
 ,3.29
 ,3.27
 ,3.32
 ,3.30
 ,3.39
 ,3.39
 ,3.01
 ,3.46
 ,3.12
 ,3.51
 ,3.68
 ,3.34
 ,3.44
 ,3.33
 ,3.40
])
nginx_NAT_lat = np.array([ 3.67
 ,3.63
 ,3.56
 ,3.62
 ,3.60
 ,3.70
 ,3.66
 ,3.56
 ,3.59
 ,3.61
 ,3.62
 ,3.62
 ,3.57
 ,3.64
 ,3.58
 ,3.59
 ,3.53
 ,3.64
 ,3.67
 ,3.59
 ,3.60
 ,3.67
 ,3.62
 ,3.68
 ,3.65
 ,3.60
 ,3.63
 ,3.62
 ,3.59
 ,3.59
])
nginx_VXLAN_lat = np.array([ 3.72
 ,3.73
 ,4.00
 ,3.77
 ,3.78
 ,3.59
 ,3.65
 ,3.68
 ,3.96
 ,3.45
 ,3.88
 ,3.66
 ,3.35
 ,3.73
 ,3.68
 ,3.60
 ,3.66
 ,3.73
 ,3.66
 ,3.70
 ,3.62
 ,3.74
 ,3.66
 ,3.60
 ,3.66
 ,3.72
 ,3.75
 ,3.70
 ,3.71
 ,3.70
])
nginx_weave_lat = np.array([ 2.20
 ,2.12
 ,2.13
 ,2.65
 ,2.65
 ,2.58
 ,2.54
 ,2.57
 ,2.57
 ,2.58
 ,2.62
 ,2.58
 ,2.55
 ,2.59
 ,2.57
 ,2.60
 ,2.68
 ,2.61
 ,2.55
 ,2.60
 ,2.54
 ,2.61
 ,2.61
 ,2.56
 ,2.56
 ,2.57
 ,2.52
 ,2.60
 ,2.60
 ,2.60
])

# Create a figure instance
fig = plt.figure()

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot([nginx_host_lat*1000, nginx_NAT_lat*1000, nginx_VXLAN_lat*1000, nginx_weave_lat*1000])

## Custom x-axis labels
ax.set_xticklabels(['Host', 'NAT', 'VXLAN', 'Weave'])
plt.title("Nginx 1KB file latency for 60K reqs/s")
plt.ylabel("Latency (ms)")
plt.show()