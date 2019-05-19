import numpy as np
import matplotlib.pyplot as plt


memcached_host_lat = np.array([6.695
,6.399
,5.615
,6.225
,6.807
,6.875
,6.683
,6.396
,6.48
,6.384
,6.599
,6.725
,6.899
,6.934
,6.161
,6.852
,6.608
,6.65
,6.456
,6.522
,6.641
,4.083
,6.917
,7.16
,6.313
,6.446
,6.536
,6.491
,6.653
,6.763
])
memcached_NAT_lat = np.array([8.239
,8.454
,7.865
,8.43
,8.138
,7.952
,8.208
,8.182
,8.053
,8.365
,8.312
,8.309
,8.349
,8.151
,8.485
,7.863
,8.373
,7.822
,7.974
,7.631
,7.966
,7.831
,7.839
,7.766
,7.665
,7.715
,8.261
,7.83
,8.126
,7.233
])
memcached_VXLAN_lat = np.array([8.71
,8.315
,8.25
,8.721
,8.408
,8.266
,8.153
,8.425
,8.303
,8.548
,8.34
,8.143
,8.319
,8.232
,8.535
,8.152
,8.412
,9.608
,8.847
,8.625
,8.461
,8.915
,8.964
,5.913
,9.035
,7.96
,9.068
,9.629
,9.276
,8.821
])
memcached_weave_lat = np.array([12.036
,10.573
,10.104
,10.357
,9.984
,10.136
,10.378
,8.214
,11.639
,10.983
,10.841
,10.973
,11.399
,9.992
,6.78
,11.224
,11.394
,12.316
,11.505
,11.226
,11.42
,11.139
,10.476
,11.075
,10.864
,10.889
,10.252
,11.513
,11.535
,10.027
])

# Create a figure instance
fig = plt.figure()

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot([memcached_host_lat, memcached_NAT_lat, memcached_VXLAN_lat, memcached_weave_lat])

## Custom x-axis labels
ax.set_xticklabels(['Host', 'NAT', 'VXLAN', 'Weave'])
plt.title("Memcached latency")
plt.ylabel("Latency (ms)")
plt.show()