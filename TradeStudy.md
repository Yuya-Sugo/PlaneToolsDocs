# `TradeStudy.m`
> Yuya Sugo, Performance Lead 2024-2025, USC AeroDesign Team </br> 5/14/2024

## Main Purpose
This script defines design space, runs trade study, calculates scores, and identifies best plane. This is the file you would interact with to set independent variables for the plane, and plot in. 

Since this is a script, this does not return anything. 

## Code Breakdown
```MATLAB
clc; clear all; close all;
global planeToolsDirectory slash;

%% Inputs
currentDirectory = split(pwd, 'PlaneTools22');
currentDirectoryCharacterVector = char(currentDirectory(1,:));
backslashLocations = strfind(currentDirectoryCharacterVector, '\');
if isempty(backslashLocations)
    slash = '/'; % forward slash for Apple Mac directories
else
    slash = '\'; % back slash for Windows directories
end
```
This allows PT to be used on Macs as well as Windows computers, resolves the differences in file path conventions. 


```MATLAB
%% Add directories to path and initialize global propulsion functions
addpath([planeToolsDirectory slash 'PhysicsModels' slash]);
addpath([planeToolsDirectory slash 'PhysicsModels' slash 'MassBuildup']);
addpath([planeToolsDirectory slash 'ComponentLibrary']);
addpath([planeToolsDirectory slash 'Plotting']);
addpath([planeToolsDirectory slash 'Environments']);
% addpath([planeToolsDirectory slash 'ComponentLibrary' slash 'material.mat']);
```
This adds the paths to the physics model, mass build-up functions, component libraries, plotting scripts, environment files onto the "search" (?) path so that when calling them in lower level functions, MATLAB can find them without calling other similarly named files on your computer. 


```MATLAB
%% Read aircraft from text file
plane = definePlane();
```
This calls the `definePlane` function to create a temporary, arbitrary plane struct with initial values. See [definePlane.md](./definePlane.md) for more information about the plane struct. 

```MATLAB
%% Define Environment
environment = defineEnvironment("Whittier");
```
This calls `defineEnvironment` to define conditions, namely desnisty and wind information (direction, speed, and headwind component on takeoff) 

