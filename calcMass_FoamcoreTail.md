# `calcMass_FoamcoreTail.m`
> Yuya Sugo, Performance Lead 2024-2025, USC AeroDesign Team </br> 06/10/2024

<!--ts-->
* [MATLAB FILE NAME.m](#matlab-file-namem)
   * [Main Purpose](#main-purpose)
   * [Background Knowledge](#background-knowledge)
   * [Code Breakdown](#code-breakdown)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: yuyasugo, at: Wed May 29 00:49:43 JST 2024 -->

<!--te-->

## Main Purpose

This function builds up the mass of a foam-core, FG skin tail. 

This is a function, taking in a plane struct and returning the mass of the tail and the plane struct. 

## Background Knowledge

To be written in further revisions. 

## Code Breakdown

```MATLAB
function [massFoamcoreTail, plane] = calcMass_FoamcoreTail(plane)
```
This is the function declaration header, taking in struct `plane` and returning `massFoamcoreTail` and (unchanged) struct `plane`.

```MATLAB
% Constants
density_foam = 3 * 16.018; % converting 3 lb/ft^3 foam to kg/m^3
density_fiberGlass = 3 / 29.494; %oz/yd2 --> kg/m2
epoxy_ratio = 0.55;
```
Defining densities and constants here. ADT purchased 2 oz/yd2 and 3 oz/yd2 E-glass fiberglass fabric in 2021-22. 

```MATLAB
% reading in airfoil x, y coordinates
airfoilFileName = 'NACA0010.csv'; % need to have this as input!
% read file (specifically the appropriate lines only)
airfoilDataOpts = detectImportOptions(airfoilFileName);
airfoilDataOpts.DataLines = [10, inf]; % NOTE: ASSUMES THAT THE AIRFOIL DATA STARTS ON LINE 10
airfoilData = readmatrix(airfoilFileName, airfoilDataOpts);
% convert from c_max = 100 -> c_max = 1, effectively mm -> m
airfoilData = airfoilData ./ 100;
```
Similar to the method shown in [calcMass_BuiltupWing.m](./calcMass_BuiltupWing.md), this gets the airfoil data from a file and normalizes it to have a chord length of 1. 

```MATLAB
%% Horizontal Stabilizer
% adjust to chord length
HstabAirfoil = airfoilData .* plane.cTailH;
% separate into x and y
xH = HstabAirfoil(:,1);
yH = HstabAirfoil(:,2);
```
This then scales the chord to be the length of the horizontal chord, then breaks the 2D array into 2 1-dimensional vectors holding the x and y coords. 

```MATLAB
% Foamcore
hStabPoly=polyshape(xH,yH);
hArea = area(hStabPoly);
hVolume = hArea * plane.bTail;
mHorzStab = hVolume * density_foam;
```
Using `polyshape` this gets the area of the airfoil, and using the span, gets the volume of the horizontal and then the mass of the horizontal stabilizer. 

```MATLAB
% Skin
hSurfArea = perimeter(hStabPoly);
mHorzStabSkin = hSurfArea * density_fiberGlass;
m_epoxy_hSkin = (epoxy_ratio/(1-epoxy_ratio)) * mHorzStabSkin;
```
This gets the surface area needed to calculates the mass of the fiberglass skin that surrounds the foam, with an `epoxy_ratio` (epoxy to fabric ratio) factor added.

```MATLAB
%% Vertical Stabilizer
% adjust to chord length
VstabAirfoil = airfoilData .* plane.cTailV;
% separate into x and y
xV = VstabAirfoil(:,1);
yV = VstabAirfoil(:,2);

% Foamcore
vStabPoly=polyshape(xV,yV);
vArea = area(vStabPoly);
vVolume = vArea * plane.hTail;
mVertStab = vVolume * density_foam;

% Skin
vSurfArea = perimeter(vStabPoly);
mVertStabSkin = vSurfArea * density_fiberGlass;
m_epoxy_vSkin = (epoxy_ratio/(1-epoxy_ratio)) * mVertStabSkin;
```
Same steps are taken for the vertical stabilizer as well. 

```MATLAB
%% Add it all up

tailMassComponents = [mVertStab mVertStabSkin m_epoxy_vSkin...
                      mHorzStab mHorzStabSkin m_epoxy_hSkin];

massFoamcoreTail = sum(tailMassComponents);

end
```
This adds up all of the components that lead up to the mass of the tail (excluding servos and wiring, done in the main [massBuildup.m](./massBuildup.md) file) and returns the value. 