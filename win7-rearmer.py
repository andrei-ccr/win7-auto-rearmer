#!/usr/bin/env python3

import winreg
import ctypes #For Admin rights check
import subprocess #For running commands in CMD

def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False

def fix_skip_rearm():
	handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\SoftwareProtectionPlatform", 0, winreg.KEY_ALL_ACCESS)
	val = winreg.QueryValueEx(handle, "SkipRearm")
	if val==(0,4):
		print("Increasing max rearms... ")
		try:
			winreg.SetValueEx(handle, "SkipRearm", 0, winreg.REG_DWORD, 1)
			winreg.CloseKey(handle)
			return True
		except:
			winreg.CloseKey(handle)
			return False
	else:
		winreg.CloseKey(handle)
		return True
		
	
def main():
	if is_admin():
		res = fix_skip_rearm()
		if res:
			print("Rearming...  ", end="")
			subprocess.check_output("SLMGR /REARM", shell=True)
			print("DONE\n")
	else:
		print("Run the script as Admin!")


if __name__== "__main__":
	main()