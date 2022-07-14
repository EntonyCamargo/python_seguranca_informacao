import nmap

scanNmap = nmap.PortScanner()
scanNmap.scan("192.168.0.1", '22', '80')
print("Valores de scan", ['192.168.0.1'])
print(scanNmap, ['192.168.0.1'])
print('-' * 40)
print('Chaves do dicionarios scanNmap', ['192.168.0.1'])
for valores in scanNmap['192.168.0.1']:
    print(valores)
print('-' * 40)
print('Valores de scanNmap', ['192.168.0.1'], ['status'])
print(scanNmap, ['192.168.0.1'], ['status'])
print('-' * 40)
print("Valor de scanNmap", ['192.168.0.1'], ['status'], ['state'])
print(scanNmap, ['192.168.0.1'], ['status'], ['state'])