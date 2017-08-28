/*

Country Euro coin holder collection

A derivative work based in the design of Jose Manuel Loureiro Vazquez

https://www.thingiverse.com/thing:2017447

License

CC-BY-NC-SA

Created by Julián Caro Linares

jcarolinares@gmail.com
*/

// Country name
country="España"; // ["Alemania","Austria","Bélgica","Chipre","Eslovaquia","Eslovenia","España","Estonia","Finlandia","Francia","Grecia","Irlanda","Italia","Letonia","Lituania","Luxemburgo","Malta","PaísesBajos","Portugal"]

// Size of the text
fontsize=4.5;


difference()
{
//Euro coin holder
scale([1.008,1.008,1]) //Scale to fit better the coins
translate([50,35,0])
{
import("v2_euro_cc.stl");
}


//Country text
translate([4,33.5,2.5])
{
color("red")
linear_extrude(height = 2, center = false, convexity = 10)
    text(country,size=fontsize);
    }
}

//// Euro coin
//translate([39,35.25,0]){
//color("blue")
//import("euro-coin.stl");
//}
