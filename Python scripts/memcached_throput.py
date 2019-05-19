import numpy as np
import matplotlib.pyplot as plt

memcached_host_thput = np.array([876.4,915.83,1043.32,939.52,862.11,854.27,878.28,916.8,906.02,920.49,890.95,873.09,849.74,845.7,946.37,856.84,887.06,883.5,907.19,896.2,881.57,1429.29,846.93,817.07,927.01,906.85,896.59,905.1,883.7,859.22])
memcached_NAT_thput = np.array([712.15
,694.04
,746.63
,697.78
,720.07
,739.87
,714.48
,718.98
,728.2
,701.21
,703.91
,704.6
,701.23
,717.38
,691.59
,745.6
,700.63
,750.13
,736
,765.37
,738.1
,749.34
,749.06
,754.86
,764.86
,760.12
,712.74
,748.58
,720.38
,808.52
])
memcached_VXLAN_thput = np.array([673.91
,706.79
,713.17
,675.13
,699.4
,709.93
,718.64
,696.19
,705.28
,686.62
,702.15
,715.54
,706.69
,713.98
,687.7
,720.34
,696.24
,613.05
,660.23
,680.94
,693.69
,658.82
,654.73
,993.72
,649.47
,734.34
,650.45
,610.66
,634.22
,665.45
])
memcached_weave_thput = np.array([486.65
,553.88
,580.79
,567.2
,587.5
,579.32
,565.46
,711.58
,505.43
,536.67
,542.43
,533.98
,517.31
,586.29
,864.56
,525.18
,515.31
,477.14
,510.35
,522.32
,513.47
,525.41
,560.06
,531.07
,539.37
,541.85
,571.27
,509.69
,509.16
,586.5
])

# calculate the average
memcached_host_thput_avg = np.mean(memcached_host_thput)
memcached_NAT_thput_avg = np.mean(memcached_NAT_thput)
memcached_VXLAN_thput_avg = np.mean(memcached_VXLAN_thput)
memcached_weave_thput_avg = np.mean(memcached_weave_thput)

# calculate the standard deviation
memcached_host_thput_std = np.std(memcached_host_thput)
memcached_NAT_thput_std = np.std(memcached_NAT_thput)
memcached_VXLAN_thput_std = np.std(memcached_VXLAN_thput)
memcached_weave_thput_std = np.std(memcached_weave_thput)

x = ["Host", "NAT", "VXLAN", "Weave"]
y = [memcached_host_thput_avg, memcached_NAT_thput_avg, memcached_VXLAN_thput_avg, memcached_weave_thput_avg]
error = [memcached_host_thput_std, memcached_NAT_thput_std, memcached_VXLAN_thput_std, memcached_weave_thput_std]


# plot the result
plt.bar(x, y, yerr=error, align='center', alpha=0.6, ecolor='black', capsize=5)
plt.title("Memcached throughput")
plt.ylabel("Throughput (KBps)")
plt.show()



