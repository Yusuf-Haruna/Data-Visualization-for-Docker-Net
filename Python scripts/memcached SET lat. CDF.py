import numpy as np
import matplotlib.pyplot as plt


nginx_SET_lat_host = np.array([10.944
,6.602
,5.841
,6.578
,7.871
,6.939
,7.517
,6.914
,6.747
,6.763
,6.617
,7.118
,6.951
,7.648
,6.138
,7.238
,7.055
,7.645
,6.914
,6.69
,6.776
,4.338
,7.726
,7.739
,6.759
,6.833
,7.386
,6.693
,6.811
,6.845
])
nginx_SET_lat_NAT = np.array([12.669
,9.565
,8.786
,9.706
,8.984
,8.488
,9.496
,9.531
,9.032
,8.773
,10.582
,9.509
,8.944
,8.446
,8.589
,7.64
,8.45
,7.824
,8.129
,10.753
,8.566
,8.572
,8.154
,8.06
,8.307
,7.916
,8.43
,7.796
,9.281
,7.711
])
nginx_SET_lat_VXLAN = np.array([12.94
,8.939
,8.888
,9.274
,9.013
,8.704
,8.23
,9.408
,8.74
,8.956
,9.434
,8.559
,8.38
,9.365
,8.553
,8.292
,8.699
,9.583
,9.082
,9.049
,8.71
,9.106
,9.677
,6.414
,9.07
,9.106
,9.834
,17.253
,9.127
,10.116
])
nginx_SET_lat_weave = np.array([22.458
,10.816
,10.073
,10.761
,10.842
,11.023
,11.061
,9.382
,11.651
,11.858
,12.453
,12.063
,12.045
,9.734
,7.003
,11.123
,11.943
,12.525
,11.385
,12.712
,11.762
,12.032
,10.555
,11.514
,11.792
,11.125
,11.239
,12.426
,12.209
,10.943
])

x1 = np.sort(nginx_SET_lat_host)
y1 = (np.arange(1, len(nginx_SET_lat_host)+1) / len(nginx_SET_lat_host)) * 100

x2 = np.sort(nginx_SET_lat_NAT)
y2 = (np.arange(1, len(nginx_SET_lat_NAT)+1) / len(nginx_SET_lat_NAT)) * 100

x3 = np.sort(nginx_SET_lat_VXLAN)
y3 = (np.arange(1, len(nginx_SET_lat_VXLAN)+1) / len(nginx_SET_lat_VXLAN)) * 100

x4 = np.sort(nginx_SET_lat_weave)
y4 = (np.arange(1, len(nginx_SET_lat_weave)+1) / len(nginx_SET_lat_weave)) * 100


plt.plot(x1, y1, linestyle='solid', linewidth=3, label='Host')
plt.plot(x2, y2, linestyle='solid', linewidth=3, label='NAT')
plt.plot(x3, y3, linestyle='solid', linewidth=3, label='VXLAN')
plt.plot(x4, y4, linestyle='solid', linewidth=3, label='Weave')

plt.legend(loc="best", shadow=True, fontsize="large")
plt.xlabel("Latency (ms)")
plt.ylabel("CDF (percentage)")
plt.title("Memcached SET operation")
plt.margins(0.01)
plt.show()