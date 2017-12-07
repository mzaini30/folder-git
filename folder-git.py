import sys, re, os

nama_folder = sys.argv[1]

nama_folder_baru = re.sub(r"-", r" ", nama_folder)
nama_folder_baru = nama_folder_baru + " (git)"

os.system("mv '"+nama_folder+"' '"+nama_folder_baru+"'")