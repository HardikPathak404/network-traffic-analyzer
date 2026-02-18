from collections import Counter
packets = [
    "192.168.1.10",
    "192.168.1.12",
    "192.168.1.10",
    "10.0.0.5",
    "192.168.1.10",
    "10.0.0.5",
    "172.16.0.3",
    "172.16.0.3",
    "172.16.0.3",
]

counter = Counter(packets)

print("Traffic Summary:\n")

for ip, count in counter.items():
    print(f"{ip} → {count} packets")

print("\nSuspicious Activity:")

for ip, count in counter.items():
    if count > 2:
        print(f"⚠ High traffic detected from {ip}")
