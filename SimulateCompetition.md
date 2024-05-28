finde# `SimulateCompetition.m`
> Yuya Sugo, Performance Lead 2024-2025, USC AeroDesign Team </br> 5/17/2024


<!--ts-->
   * [Main Purpose](#main-purpose)
   * [Background Knowledge](#background-knowledge)
      * [MATLAB global variables](#matlab-global-variables)
   * [Code Breakdown](#code-breakdown)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: yuyasugo, at: Wed May 29 00:49:45 JST 2024 -->

<!--te-->



## Main Purpose
This function simulates the plane at competition, calling the mass estimate function, drag estimate function, and simulates both Mission 2 and Mission 3 flights. 

Since this is a function, taking in a `plane` struct and a `environment` struct and returning structs `missionResults2`, `missionResults3`, `plane`.

## Background Knowledge

### MATLAB `global` variables
As opposed to local variables that can be only accessed inside the function that it was declared in, a variable defined as global can be accessed from any function. Keep in mind that declaring a variable as global inside a function does not make it global in the base workspace, unless it is explicitly declared there as well.

```MATLAB
clc; clear;

global VARIABLE

VARIABLE = 10;

fprintf('Global VARIABLE = %.0f\n', VARIABLE) 

function changeVar()
    global VARIABLE
    VARIABLE = 30;
end

changeVar();

fprintf('Global VARIABLE = %.0f\n', VARIABLE)
```

This yields `Global VARIABLE = 10` and `Global VARIABLE = 30`. 

Where as if the global variable was not declared as global in the parent script, it will not work as intended. 

```MATLAB
clc; clear;

variable = 10;

fprintf('variable = %.0f\n', variable) 

function changeVar()
    global variable
    variable = 30;
end

changeVar();

fprintf('variable = %.0f\n', variable)
```

This yields `variable = 10`, `variable = 10`



## Code Breakdown

```MATLAB
% The two options below cannot be true at the same time
skipM3 = false; % use this to simulate a bunch of M2 only planes
runM3 = false; % use this to simulate M3 even if M2 fails tofl
EWPenalty = true; % use this to add an empty weight penalty for heavier MSC
```
These are basically settings that allows users to skip certain parts of the code. This is left over from the 2023-2024 DBF comp. 

```MATLAB
global T CTf CPf
CTf = 1; % multiplier on thrust coefficient (empirical/theoretical --> experimental)
CPf = 1; % multiplier on thrust coefficient (empirical/theoretical --> experimental)
```
This bit declares three global variables, `T` (thrust) `CTf` (Coefficient of Thrust Fudge factor) `CPf` (Coefficient of Power Fudge factor)

```MATLAB
% Build up weight and drag
[M2massResults, plane] = massBuildup(plane, 2);
```
Calls [`massBuildup.m`](./massBuildup.md) with inputs of plane struct and 2 indicating mass buildup for mission 2. 