#!/usr/bin/python3

import sys, numpy as np, pandas as pd

import matplotlib.pyplot as plt

#graphs dimensions
fsz=(10, 8)
_dpi=100
plt.figure(figsize=fsz, dpi=_dpi)

out_ext = ".png"

plt.style.use(['bmh'])
# plt.style.use(['ggplot'])
# plt.style.use(['seaborn'])
# plt.style.use(['dark_background'])

filename = ""

degree = 2
cols = []

#filename mask for wildcard for opening csv files
if len(sys.argv) > 4:
    filename = sys.argv[1]
    degree = int(sys.argv[2])
    cols.append(sys.argv[3])
    cols.append(sys.argv[4])
else:
    filename = input("filename: ")
    degree = int(input("aproximation degree: "))
    cols = input("Enter columns separated by space: ").split(' ')

fdata = pd.DataFrame(columns=cols)

separator = ","

#Markers, default '.': https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
marker = '.'

df = pd.read_csv(filename, sep=separator)

x = np.array(df[cols[0]]).astype(float)
y = np.array(df[cols[1]]).astype(float)
model = np.poly1d(np.polyfit(x, y, degree))
polyline = np.linspace(df[cols[0]].min(), df[cols[0]].max())
fig, ax = plt.subplots(figsize=fsz, dpi=_dpi)
ax.plot(polyline, model(polyline), "tab:orange")
xs, ys = zip(*sorted(zip(df[cols[0]], df[cols[1]])))
ax.plot(xs,ys, marker)
fig.savefig(filename + "_" + out_ext)
