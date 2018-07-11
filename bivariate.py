#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 18:23:11 2018

@author: faris
"""
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid")


f, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect("equal")

# Draw the two density plots
ax = se.kdeplot(emerge.incomeperperson, emerge.incomeperperson,
                 cmap="Reds", shade=True, shade_lowest=False)
ax = se.kdeplot(developed.incomeperperson, developed.incomeperperson,
                 cmap="Blues", shade=True, shade_lowest=False)

# Add labels to the plot
red = se.color_palette("Reds")[-2]
blue = se.color_palette("Blues")[-2]
ax.text(40000, 40000, "Developed", size=16, color=blue)
ax.text(7000, 7000, "Emerging", size=16, color=red)

