# -*- coding: utf-8 -*-

'''

Country Euro coin holder collection

A derivative work based in the design of Jose Manuel Loureiro Vazquez

https://www.thingiverse.com/thing:2017447

License

CC-BY-NC-SA

Created by Julián Caro Linares

jcarolinares@gmail.com

'''

import os
import subprocess


#List of countries that uses the euro Source: https://europa.eu/european-union/about-eu/money/euro_en
#list_of_countries=["Alemania","Austria","Bélgica","Chipre","Eslovaquia","Eslovenia","España","Estonia","Finlandia","Francia","Grecia","Irlanda","Italia","Letonia","Lituania","Luxemburgo","Malta","PaísesBajos","Portugal","Andorra", "Mónaco", "SanMarino", "Vaticano"]
list_of_countries=["Austria", "Belgium", "Cyprus", "Estonia", "Finland", "France", "Germany", "Greece", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Portugal", "Slovakia", "Slovenia", "Spain","Andorra", "Mónaco", "SanMarino", "Vatican"]


def main():

    #List of countries
    for country in list_of_countries:
        print(country)
        if len(country)>9:
            subprocess.call('openscad -D \'country=\"'+ country+'\"\' -D \'fontsize=3\' -o '+country+'_eurocollection.stl' +' eurocollectioncountries.scad' ,shell=True)
        elif len(country)>6:
            subprocess.call('openscad -D \'country=\"'+ country+'\"\' -D \'fontsize=3.7\' -o '+country+'_eurocollection.stl' +' eurocollectioncountries.scad' ,shell=True)
        else:
            subprocess.call('openscad -D \'country=\"'+ country+'\"\' -o '+country+'_eurocollection.stl' +' eurocollectioncountries.scad' ,shell=True)

    subprocess.call('notify-send -t 4500 "STL Files Generation completed"' ,shell=True)

if __name__ == '__main__':
    main()
