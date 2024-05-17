# `sizeTail.m`
> Yuya Sugo, Performance Lead 2024-2025, USC AeroDesign Team </br> 5/17/2024


<!--ts-->
* [sizeTail.m](#sizetailm)
   * [Main Purpose](#main-purpose)
   * [Background Knowledge](#background-knowledge)
   * [Code Breakdown](#code-breakdown)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: yuyasugo, at: Fri May 17 19:40:53 JST 2024 -->

<!--te-->

## Main Purpose
This function sizes the tail based on the tail volume coefficients method, updating the plane struct.

This is a function, taking in a `plane` struct and returning a `plane` struct that is updated. 

## Background Knowledge

We can define a dimensionless coefficient called the Volume Coefficient for the horizontal and vertical tail to help us describe the tail. 
The horizontal tail volume coefficient is defined by:
```math
V_{HT} = \frac{l_{HT}\ S_{HT}}{c_{MAC}\ S_{wing}}
```

The vertical tail volume coefficient is defined by:
```math
V_{VT} = \frac{l_{VT}\ S_{VT}}{b\ S_{wing}}
```

The figure below graphically defines all of the variables used to define the tail planform for a conventional tail configuration. 


![Def of geometric terms for tail](<./Figures/Gud. Fig. 11-2.jpg>)

## Code Breakdown
```MATLAB
function [plane] = sizeTail(plane)
```
This defines the function: this takes in a `plane` struct and returns an updated `plane` struct. 

With the input `plane` struct, the fixed values that this function uses are: `S`, `b`, `c`, `ARh`, `Vh`, and `Vv`

```MATLAB
    % Arbitrary moment arm
    plane.lh = 0.6*plane.b; % old value
```
In this stage, PT estimates that the arm for the horizontal is 60% of the span of the wing. 

```MATLAB
    % Horizontal sizing
    plane.Sh = plane.Vh*plane.S*plane.c/plane.lh;
    plane.bh = sqrt(plane.ARh*plane.Sh);
    plane.ch = plane.Sh./plane.bh;
```
Based on the horizontal tail volume coefficient, `Sh` (reference area of the horizontal) was determined, followed by the span and chord based off `ARh`


```MATLAB
    % Vertical sizing
    plane.lv = plane.lh;
    plane.Sv = plane.Vv*plane.S*plane.b/plane.lv;
    plane.cv = plane.ch;
    plane.bv = plane.Sv/plane.cv;
    plane.ARv = plane.bv.^2./plane.Sv;
```
Next is the vertical. It assumes that the arm is the same as the horizontal, and with this, it determines the `Sv` (reference area of the vertical). Assuming the chords are the same (`cv` = `ch`), it determines `bv` and `ARv`. 

```MATLAB
    % Tail parameters (chord and span from hor, height from vert)
    plane.cTail = plane.ch;
    plane.bTail = plane.bh;
    plane.hTail = plane.bv;
```
Then it assigns the main parameters (chord, span, and height) into the `plane` struct. 