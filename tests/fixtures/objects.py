file1 = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False
}

file2 = {
  "timeout": 20,
  "verbose": True,
  "host": "hexlet.io"
}

keys12 = ['follow', 'host', 'proxy', 'timeout', 'verbose']
keys10 = ['follow', 'host', 'proxy', 'timeout']
keys02 = ['host', 'timeout', 'verbose']

diff12 = [
          {'key': 'follow', 'status': 'DEL', 'value': False},
          {'key': 'host', 'status': 'STAY', 'value': 'hexlet.io'},
          {'key': 'proxy', 'status': 'DEL', 'value': '123.234.53.22'},
          {'key': 'timeout', 'status': 'CHANGE', 'value1_old': 50, 'value2_new': 20},
          {'key': 'verbose', 'status': 'ADD', 'value': True}
]
