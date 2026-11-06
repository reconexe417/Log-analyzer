import re

OCTET = r'(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)'
IPV4_RE = re.compile(rf'\b{OCTET}\.{OCTET}\.{OCTET}\.{OCTET}\b')

PATTERN_RE = re.compile(
    r'\b(?:401|403|404|408|500|502|503|504|520|521|522|523|524|525|526)\b'
)

results = []
counts = {}

with open('sample.log') as f:
    file = f.read()

    print("All IPv4 addresses:")
    print(IPV4_RE.findall(file))

    for line in file.splitlines():
        ip_match = IPV4_RE.search(line)
        pattern_match = PATTERN_RE.search(line)

        if ip_match and pattern_match:
            ip = ip_match.group()
            code = pattern_match.group()

            results.append((ip, code))

            counts[code] = counts.get(code, 0) + 1

print("\nFailed HTTP codes with IP addresses:")

for ip, code in results:
    print(f"IP: {ip} | Code: {code}")

print("\nHTTP Status Code Statistics:")

for code, count in counts.items():
    print(f"{code}: {count} occurrences")