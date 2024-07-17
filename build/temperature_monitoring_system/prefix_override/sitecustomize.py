import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/anthony/Desktop/Assignment6/install/temperature_monitoring_system'
