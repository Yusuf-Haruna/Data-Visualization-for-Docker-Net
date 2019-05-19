import matplotlib.pyplot as plt
import numpy as np

iperf3_host_TCP = np.array([1991,2085,1952,1747,1758,1748,1802,1811,2035,2092,2081,2001,2061,2012,2074,1926,2078,2065,1960,2022,2006,1945,965,1773,1721,1833,1597,1784,1995,1918])
iperf3_NAT_TCP = np.array([1741,1788,1802,1700,1640,1650,1775,1707,1763,1742,1809,1301,1392,1711,1728,1700,1821,1724,1739,1839,1691,1868,1766,1686,1738,1722,1773,1651,1819,1665])
iperf3_VXLAN_TCP = np.array([492,495,478,481,482,493,472,477,482,478,476,483,485,490,469,484,481,473,471,486,482,469,478,486,477,466,483,460,417,479])
iperf3_weave_TCP = np.array([352,302,327,332,331,333,330,328,328,327,322,333,325,325,331,327,334,330,333,333,326,325,328,329,335,333,324,329,331,336])


# Create a figure instance
fig = plt.figure()

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot([iperf3_host_TCP, iperf3_NAT_TCP, iperf3_VXLAN_TCP, iperf3_weave_TCP])

## Custom x-axis labels
ax.set_xticklabels(['Host', 'NAT', 'VXLAN', 'Weave'])
plt.title("iperf3 TCP throughput")
plt.ylabel("Throughput (MBps)")
plt.show()
