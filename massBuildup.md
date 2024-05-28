# `massBuildup.m`
> Yuya Sugo, Performance Lead 2024-2025, USC AeroDesign Team </br> 5/28/2024

<!--ts-->
* [massBuildup.m](#massbuildupm)
   * [Main Purpose](#main-purpose)
   * [Background Knowledge](#background-knowledge)
      * [Definitions of Different Weights in PT](#definitions-of-different-weights-in-pt)
   * [Code Breakdown](#code-breakdown)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: yuyasugo, at: Wed May 29 00:49:44 JST 2024 -->

<!--te-->

## Main Purpose

This function builds up the mass of the aircraft for any given mission (2nd positional argument)

Since this is a function, taking in a `plane` struct and a `mission` integer and returning structs `massResults`, `plane`

## Background Knowledge

Weight Engineering is an entire discipline of engineering, and especially at our scale with a small number of aircraft that we can compare and reference, it can be especially difficult to estimate the weight of our aircraft. 

Previous years has shown that mass buildups have yielded pretty inaccurate values, as the year progresses, actual values have been hardcoded in for a better estimate. 

### Definitions of Different Weights in PT

Note that some of these definitions vary to standard definition used in industry. 

- `Empty Weight` refers to the sum of Fuselage, Wing, Tail, Battery, Motor*nMotors, MotorMount, LG, Servos, Wiring, ESC, and Avionics

## Code Breakdown

> Note: A lot of the code has been hardcoded with actual values, this doc will bypass those hardcoded values. 

```MATLAB
function [massResults, plane] = massBuildup(plane, mission)
```
This is the function declaration header, and it takes in a `plane` struct and a `mission` number. It then returns a `massResults` struct and an updated `plane` struct. 

```MATLAB
%% Bypass everything if plane is already built
if ~plane.massBuildup
    [...]
else
```
Will bypass the mass build up if the plane is already built -- reduces runtime. 
```MATLAB
    if plane.wingBuildMethod.isequal("builtup")
        [mWing, plane] = calcMass_BuiltupWing(plane);
        plane.mWing = mWing;
    elseif plane.wingBuildMethod.isequal("foamcore")
        [mWing, plane] = calcMass_FoamcoreWing(plane);
        plane.mWing = mWing;
    end
```
Mass estimate of the wing for either buildup [`calcMass_BuiltupWing.m`](./calcMass_BuiltupWing.md) or foamcore (seems to be outdated, no doc created at this time.)

```MATLAB
    % Fuselage
    mFuse = calcMass_Fuselage(plane);
    plane.mFuse = mFuse;
```
Mass estimate of the fuselage [`calcMass_Fuselage.m`](./calcMass_Fuselage.md)

```MATLAB
%     % Tail
%     mTail = 1.2 * calcMass_FoamcoreTail(plane); % foamcore + skin
```
```MATLAB
    % Conventional Tail / T Tail (Built-up)
    
    % builtupDensity = mWing / (plane.b * plane.c); % kg/m2
    % mVStab = builtupDensity * plane.cTail * plane.hTail;
    % mHStab = builtupDensity * plane.cTail * plane.bTail;
    % mTail = mVStab + mHStab;
    
    tailAvgThickness = 0.05 * plane.cTailH;
    mTail = plane.cTailH*(plane.bTail + plane.hTail)*tailAvgThickness*density_balsa;
    plane.mTail = mTail;
    % V Tail (Built-up)
```