
import subprocess

data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')

profiles = [value.split(':')[1][1:-1] for value in data if "All User Profile" in value]

for profile in profiles:
  password = subprocess.check_output(['netsh','wlan','show','profile',profile,'key=clear']).decode('utf-8').split('\n')

  password = [passwd.split(':')[1][1:-1] for passwd in password if "Key Content" in passwd]

  try:
  	print("{:<30}|  {:<}".format(profile,password[0]))
  except IndexError:
  	print("{:<30}|  {:<}".format(profile, ""))
