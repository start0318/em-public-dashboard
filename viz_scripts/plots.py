
import pandas as pd
import numpy as np
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Patch

sns.set_style("whitegrid")
sns.set()
get_ipython().run_line_magic('matplotlib', 'inline')

SAVE_DIR="/plots/"

def pie_chart_mode(plot_title,labels,values,file_name):
    all_labels= ['Car, drove alone',
                 'Bus', 
                 'Train', 
                 'Free Shuttle',
                 'Taxi/Uber/Lyft', 
                 'Car, with others', 
                 'Bikeshare',
                 'Scooter share',
                 'Pilot ebike', 
                 'Walk', 
                 'Skate board', 
                 'Regular Bike', 
                 'Not a Trip',
                 'No Travel', 
                 'Same Mode', 
                 'Other']
    
    colours = dict(zip(all_labels, plt.cm.tab20.colors[:len(all_labels)]))
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(aspect="equal"))
    
     
    
    def func(pct, values):
        total = sum(values)
        absolute = int(round(pct*total/100.0))
        return "{:.1f}%\n({:d})".format(pct, absolute) if pct > 3 else''
 
    wedges, texts, autotexts = ax.pie(values,
                                      labels = labels,
                                      colors=[colours[key] for key in labels],
                                      pctdistance=0.75,
                                      autopct= lambda pct: func(pct, values),
                                      textprops={'size': 16})


    ax.set_title(plot_title, size=18)
    plt.setp(autotexts, **{'color':'white', 'weight':'bold', 'fontsize':16})
    plt.savefig(SAVE_DIR+file_name, bbox_inches='tight')
    plt.show()

def pie_chart_purpose(plot_title,labels,values,file_name):
    labels_trip= ['Work', 
                  'Home',
                  'Meal',
                  'Shopping',
                  'Personal/Medical',
                  'Recreation/Exercise', 
                  'Transit transfer', 
                  'Pick-up/Drop off',
                  'Entertainment/Social',
                  'Other',
                  'School',
                  'Religious',
                  'No travel', 
                  'not_a_trip']
    
    colours = dict(zip(labels_trip, plt.cm.tab20.colors[:len(labels_trip)]))
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(aspect="equal"))
    
    def func(pct, values):
        total = sum(values)
        absolute = int(round(pct*total/100.0))
        return "{:.1f}%\n({:d})".format(pct, absolute) if pct > 3 else''
    
    wedges, texts, autotexts = ax.pie(values,
                                      labels = labels,
                                      colors=[colours[key] for key in labels],
                                      pctdistance=0.85,
                                      autopct=lambda pct: func(pct, values),
                                      textprops={'size': 16})


    ax.set_title(plot_title, size=18)
    plt.setp(autotexts, **{'color':'white', 'weight':'bold', 'fontsize':16})
    plt.savefig(SAVE_DIR+file_name, bbox_inches='tight')
    plt.show()
    
    
def distancevsenergy(data,x,y,legend,plot_title,file_name):
    all_labels= ['Car, drove alone',
                 'Bus', 
                 'Train', 
                 'Free Shuttle',
                 'Taxi/Uber/Lyft', 
                 'Car, with others', 
                 'Bikeshare',
                 'Scooter share',
                 'Pilot ebike', 
                 'Walk', 
                 'Skate board', 
                 'Regular Bike', 
                 'Not a Trip',
                 'No Travel', 
                 'Same Mode', 
                 'Other']
    
    colours = dict(zip(all_labels, plt.cm.tab20.colors[:len(all_labels)]))
    f = plt.subplots(figsize=(15, 6))
    
 
    sns.set(style='whitegrid')
    sns.scatterplot(x=x, y=y, data=data, hue=legend, palette=colours)
    plt.legend(loc='upper right')
    plt.xlabel("", fontsize=15)
    plt.ylabel(y, fontsize=15)
    plt.title(plot_title, fontsize=15)
    plt.savefig(SAVE_DIR+ file_name, bbox_inches='tight')
    
    


def overeall_energy_impact(x,y,color,data,plot_title,file_name):
    plt.figure(figsize=(15, 8))
    width = 0.8
    ax = sns.barplot(x=x, y=y, hue=color,data=data)
    ax.set_title(plot_title, fontsize=18)
    ax.set_xlabel(x, fontsize=18)
    ax.set_ylabel(y,fontsize=18)
    ax.xaxis.set_tick_params(labelsize=15)
    ax.yaxis.set_tick_params(labelsize=15)
    ax.relim()
    ax.autoscale_view()                  
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=18)
    
    plt.savefig(SAVE_DIR+ file_name, bbox_inches='tight')
    
    
    
def energy_impact(x,y,color,plot_title,file_name):
    color = color.map({True: 'green', False: 'red'})
    objects = ('Energy Savings', 'Energy Loss')
    
    y_labels = y
    plt.figure(figsize=(15, 8))
    width = 0.8
    ax = x.plot(kind='barh',width=width, color=color)
    ax.set_title(plot_title, fontsize=18)
    ax.set_xlabel('Energy_Impact(kWH)', fontsize=18)
    ax.set_ylabel('Replaced Mode',fontsize=18)
    ax.set_yticklabels(y_labels)
    ax.xaxis.set_tick_params(labelsize=15)
    ax.yaxis.set_tick_params(labelsize=15)
    ax.relim()
    ax.autoscale_view() 

    rects = ax.patches

   
    for rect in rects:
        x_value = rect.get_width()
        y_value = rect.get_y() + rect.get_height() / 2
        space = 5
        ha = 'left'

       
        if x_value < 0:
            space *= -1
            ha = 'right'

        
        label = "{:.1f}".format(x_value)

        # Create annotation
        plt.annotate(
            label,                      
            (x_value, y_value),         
            xytext=(space, 0),          
            textcoords="offset points", 
            va='center',                
            ha=ha, fontsize=12, color='black', fontweight='bold')
        
        # map names to colors
    cmap = {True: 'green', False: 'red'}
        
    patches = [Patch(color=v, label=k) for k, v in cmap.items()]
    
    plt.legend(labels=objects, handles=patches, loc='upper right', borderaxespad=0, fontsize=15, frameon=True)

    plt.savefig(SAVE_DIR+ file_name, bbox_inches='tight')
    
    
def barplot_mode(data,x,y,plot_title,file_name):
    all_labels= ['Car, drove alone',
                 'Bus', 
                 'Train', 
                 'Free Shuttle',
                 'Taxi/Uber/Lyft', 
                 'Car, with others', 
                 'Bikeshare',
                 'Scooter share',
                 'Pilot ebike', 
                 'Walk', 
                 'Skate board', 
                 'Regular Bike', 
                 'Not a Trip',
                 'No Travel', 
                 'Same Mode', 
                 'Other']
    
    colours = dict(zip(all_labels, plt.cm.tab20.colors[:len(all_labels)]))
    sns.set(font_scale=1.5)
    f = plt.subplots(figsize=(15, 6))
    sns.set(style='whitegrid')
    ax = sns.barplot(x=x, y=y, palette=colours,data=data, ci=None)
    plt.xlabel(x, fontsize=16)
    plt.ylabel(y, fontsize=16)
    plt.title(plot_title, fontsize=16)
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.savefig(SAVE_DIR+ file_name, bbox_inches='tight')
    

def barplot_mode2(data,x,y,y2,plot_title,file_name):
    all_labels= ['Car, drove alone',
                 'Bus', 
                 'Train', 
                 'Free Shuttle',
                 'Taxi/Uber/Lyft', 
                 'Car, with others', 
                 'Bikeshare',
                 'Scooter share',
                 'Pilot ebike', 
                 'Walk', 
                 'Skate board', 
                 'Regular Bike', 
                 'Not a Trip',
                 'No Travel', 
                 'Same Mode', 
                 'Other']
    
    colours = dict(zip(all_labels, plt.cm.tab20.colors[:len(all_labels)]))
    sns.set(font_scale=1.5)

    fig, ax1 = plt.subplots(figsize=(15,6))
   
    #bar plot creation
    ax1.set_title(plot_title, fontsize=16)
    ax1.set_xlabel(x, fontsize=16)
    ax1.set_ylabel(y, fontsize=16)
    ax1 = sns.barplot(x=x, y=y, data = data, palette=colours, ci=None)
    ax1.grid(False)
    
    #specify we want to share the same x-axis
    ax2 = ax1.twinx()
    color = 'tab:red'
    #line plot creation
    ax2.set_ylabel('Count', fontsize=16)
    ax2 = sns.pointplot(x=x, y=y2, data = data, sort=False, color=color)
    ax2.grid(False)
    plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')
    plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')
    plt.savefig(SAVE_DIR+ file_name, bbox_inches='tight')
    
    
def barplot_day(data,x,y,plot_title,file_name):

    sns.set(font_scale=1.5)
    f = plt.subplots(figsize=(15, 6))
    sns.set(style='whitegrid')
    ax = sns.barplot(x=x, y=y,data=data, ci=None, color='blue')
    plt.xlabel(x, fontsize=16)
    plt.ylabel(y, fontsize=16)
    plt.title(plot_title, fontsize=16)
    plt.savefig(SAVE_DIR+ file_name, bbox_inches='tight')
