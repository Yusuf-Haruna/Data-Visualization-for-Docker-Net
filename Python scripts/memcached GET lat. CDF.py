import numpy as np
import matplotlib.pyplot as plt


nginx_GET_lat_host = np.array([6.254
,6.378
,5.592
,6.188
,6.697
,6.868
,6.596
,6.342
,6.453
,6.345
,6.598
,6.684
,6.894
,6.86
,6.164
,6.812
,6.562
,6.546
,6.409
,6.505
,6.627
,4.057
,6.834
,7.1
,6.268
,6.406
,6.448
,6.47
,6.637
,6.754
])
nginx_GET_lat_NAT = np.array([7.776
,8.337
,7.768
,8.297
,8.049
,7.897
,8.074
,8.042
,7.951
,8.322
,8.073
,8.184
,8.287
,8.12
,8.474
,7.886
,8.365
,7.822
,7.958
,7.306
,7.903
,7.753
,7.807
,7.736
,7.598
,7.694
,8.243
,7.833
,8.005
,7.184
])
nginx_GET_lat_VXLAN = np.array([8.266
,8.249
,8.183
,8.663
,8.344
,8.22
,8.145
,8.322
,8.258
,8.505
,8.226
,8.099
,8.313
,8.112
,8.533
,8.138
,8.382
,9.61
,8.823
,8.58
,8.435
,8.895
,8.889
,5.862
,9.031
,7.841
,8.987
,8.833
,9.291
,8.684
])
nginx_GET_lat_weave = np.array([10.952
,10.547
,10.107
,10.314
,9.893
,10.044
,10.305
,8.09
,11.637
,10.889
,10.668
,10.859
,11.331
,10.019
,6.757
,11.235
,11.336
,12.293
,11.518
,11.068
,11.384
,11.047
,10.467
,11.028
,10.765
,10.864
,10.149
,11.417
,11.463
,9.93
])

x1 = np.sort(nginx_GET_lat_host)
y1 = (np.arange(1, len(nginx_GET_lat_host)+1) / len(nginx_GET_lat_host)) * 100

x2 = np.sort(nginx_GET_lat_NAT)
y2 = (np.arange(1, len(nginx_GET_lat_NAT)+1) / len(nginx_GET_lat_NAT)) * 100

x3 = np.sort(nginx_GET_lat_VXLAN)
y3 = (np.arange(1, len(nginx_GET_lat_VXLAN)+1) / len(nginx_GET_lat_VXLAN)) * 100

x4 = np.sort(nginx_GET_lat_weave)
y4 = (np.arange(1, len(nginx_GET_lat_weave)+1) / len(nginx_GET_lat_weave)) * 100


plt.plot(x1, y1, linestyle='solid', linewidth=3, label='Host')
plt.plot(x2, y2, linestyle='solid', linewidth=3, label='NAT')
plt.plot(x3, y3, linestyle='solid', linewidth=3, label='VXLAN')
plt.plot(x4, y4, linestyle='solid', linewidth=3, label='Weave')

plt.legend(loc="best", shadow=True, fontsize="large")
plt.xlabel("Latency (ms)")
plt.ylabel("CDF (percentage)")
plt.title("Memcached GET operation")
plt.margins(0.01)
plt.show()