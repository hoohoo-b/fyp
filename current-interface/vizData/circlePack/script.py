
import os
for f in os.listdir("C:/xampp/htdocs/fyp/current-interface/expt2/hi"):
    os.rename(f, f[:-4]+'.json')