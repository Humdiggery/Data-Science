# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 06:44:49 2016

@author: Katie
"""

#ingredients are stored as a dictionary of tuples. Each tuple includes
#the ingredients and the amount of milliliters

ingredients = {
               'butter' : ('butter',118.3),
               'sugar' : ('sugar',236.6),
               'vanilla' : ('vanilla',4,929),
               'eggs' : ('eggs', 2),
               'cocoa': ('cocoa',118.3),
               'flour':('flour',118.3)
                }

#butter refrigerated, so not soft yet
butter_soft=False

bowl=[]


#To make a cake need the following functions:
def melt(this):
    print("Melting {0}.".format(this))
    
def bake(this, temp):
    print("Baking {0} at {1}.".format(this,temp))
    
def mix(this):
    print('Mixing {0}.'.format(this))
    
def add_to_bowl(ingredient):
    print('Adding {0} to the bowl.'.format(ingredient))



#start the algorithm
if butter_soft !=True:
    melt(ingredients['butter'][0])
    butter_soft=True

add_to_bowl(ingredients['butter'][0])     
add_to_bowl(ingredients['sugar'][0])

mix(bowl)

#mix until creamy
mixture_creamy=False
mixing_time=0

while mixture_creamy==False:
    mix(bowl)
    mixing_time+=1
    if mixing_time==3:
        mixture_creamy=True
        
add_to_bowl['eggs'][0]
add_to_bowl['vanilla'][0]


mix(bowl)

add_to_bowl['flour'][0]
add_to_bowl['coccoa'][0]

mixing_time=0
well_blended=False

while well_blended==False:
    mix(bowl)
    mixing_time+=1
    if mixing_time==4:
        well_blended=True
        
cake_pan=bowl

cooking_temp=350
cooking_time=30


for minutes in range(0, cooking_time):
    bake(cake_pan, cooking_temp)

print('The cake is done')
