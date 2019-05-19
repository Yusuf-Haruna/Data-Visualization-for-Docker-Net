import numpy as np
import matplotlib.pyplot as plt


iperf3_host_UDP = np.array([719,647,604,527,552,590,557,586,606,605,592,603,627,628,598,602,613,608,628,603,603,607,332,590,590,606,505,606,602,627])
iperf3_NAT_UDP = np.array([326,295,277,270,273,289,283,274,269,274,274,279,277,280,278,283,288,276,279,304,284,279,273,292,291,283,275,289,270,276])
iperf3_VXLAN_UDP = np.array([229,194,201,191,199,186,195,185,191,181,189,187,186,193,210,189,187,190,185,199,173,199,179,196,180,183,187,191,190,203])
iperf3_weave_UDP = np.array([203,175,170,171,163,174,182,167,171,189,171,170,171,186,157,155,186,176,153,188,181,173,166,182,176,167,192,174,165,176])

# calculate the average
iperf3_host_UDP_avg = np.mean(iperf3_host_UDP)
iperf3_NAT_UDP_avg = np.mean(iperf3_NAT_UDP)
iperf3_VXLAN_UDP_avg = np.mean(iperf3_VXLAN_UDP)
iperf3_weave_UDP_avg = np.mean(iperf3_weave_UDP)


# calculate the standard deviation
iperf3_host_UDP_std = np.std(iperf3_host_UDP)
iperf3_NAT_UDP_std = np.std(iperf3_NAT_UDP)
iperf3_VXLAN_UDP_std = np.std(iperf3_VXLAN_UDP)
iperf3_weave_UDP_std = np.std(iperf3_weave_UDP)


x = ["Host", "NAT", "VXLAN", "Weave"]
y = [iperf3_host_UDP_avg, iperf3_NAT_UDP_avg, iperf3_VXLAN_UDP_avg, iperf3_weave_UDP_avg]
error = [iperf3_host_UDP_std, iperf3_NAT_UDP_std, iperf3_VXLAN_UDP_std, iperf3_weave_UDP_std]

# plot the result
plt.bar(x, y, yerr=error, align='center', alpha=0.6, ecolor='black', capsize=5)
plt.title("iperf3 UDP throughput")
plt.ylabel("Throughput (MBps)")
plt.show()