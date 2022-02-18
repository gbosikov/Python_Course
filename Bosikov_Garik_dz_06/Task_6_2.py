
line = '255.1.25.255 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"'


print(line.replace('-', ' ')[:15].replace(' ', ''))
print(line[line.find('"') + 1:line.find('"') + 4])
print(line[line.find('"') + 5:line.find('"') + 5 + 20])



