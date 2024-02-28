import socket
import platform

def get_host_name():
    # Get the system's hostname
    hostname = socket.gethostname()
    return hostname

def get_system_info():
    # Get the system's OS and release information
    system_info = platform.system() + " " + platform.release()
    return system_info
