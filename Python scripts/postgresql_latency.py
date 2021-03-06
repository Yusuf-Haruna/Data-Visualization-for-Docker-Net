import numpy as np
import matplotlib.pyplot as plt


postgresql_host_lat = np.array([48.692
,45.366
,70.902
,74.49
,51.042
,51.436
,73.022
,84.056
,83.875
,75.807
,61.25
,107.722
,77.121
,57.09
,38.076
,60.833
,91.638
,48.585
,74.604
,52.997
,71.348
,59.022
,94.179
,38.329
,55.435
,54.641
,46.543
,48.107
,78.246
,840.135
])
postgresql_NAT_lat = np.array([66.398
,97.582
,68.105
,76.988
,68.378
,65.996
,71.526
,77.486
,101.359
,83.177
,109.341
,84.314
,120.652
,87.819
,87.73
,126.789
,85.546
,37.443
,58.807
,78.626
,54.741
,90.508
,103.699
,93.791
,49.88
,102.715
,75.392
,111.37
,377.458
,51.099
])
postgresql_VXLAN_lat = np.array([153.856
,100.246
,104.005
,156.5
,497.503
,108.425
,87.175
,101.203
,112.244
,81.927
,108.911
,91.206
,136.285
,113.688
,179.525
,142.127
,90.356
,99.146
,70.773
,159.383
,161.629
,88.407
,120.275
,118.347
,64.99
,115.473
,129.28
,151.042
,129.31
,117.48
])
postgresql_weave_lat = np.array([143.991
,107.618
,90.391
,105.772
,81.001
,107.057
,128.407
,150.363
,126.357
,99.035
,94.233
,92.172
,84.371
,121.703
,130.152
,97.603
,86.165
,168.255
,115.481
,106.589
,90.657
,163.088
,95.166
,99.438
,61.357
,99.018
,118.273
,129.653
,1041.216
,74.172
])

# calculate the average
postgresql_host_lat_avg = np.mean(postgresql_host_lat)
postgresql_NAT_lat_avg = np.mean(postgresql_NAT_lat)
postgresql_VXLAN_lat_avg = np.mean(postgresql_VXLAN_lat)
postgresql_weave_lat_avg = np.mean(postgresql_weave_lat)

# calculate the standard deviation
postgresql_host_lat_std = np.std(postgresql_host_lat)
postgresql_NAT_lat_std = np.std(postgresql_NAT_lat)
postgresql_VXLAN_lat_std = np.std(postgresql_VXLAN_lat)
postgresql_weave_lat_std = np.std(postgresql_weave_lat)


x = ["Host", "NAT", "VXLAN", "Weave"]
y = [postgresql_host_lat_avg, postgresql_NAT_lat_avg, postgresql_VXLAN_lat_avg, postgresql_weave_lat_avg]
error = [postgresql_host_lat_std, postgresql_NAT_lat_std, postgresql_VXLAN_lat_std, postgresql_weave_lat_std]

# plot the result
plt.bar(x, y, yerr=error, align='center', alpha=0.6, ecolor='black', capsize=5)
plt.title("PostgreSQL latency")
plt.ylabel("Latency (ms)")
plt.margins(0.01)
plt.show()