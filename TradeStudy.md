# `TradeStudy.m`
> Yuya Sugo, Performance Lead 2024-2025, USC AeroDesign Team </br> 5/14/2024

<!--ts-->
* [TradeStudy.m](#tradestudym)
   * [Main Purpose](#main-purpose)
   * [Code Breakdown](#code-breakdown)
      * [Trade Study Setup](#trade-study-setup)
      * [Trade Study](#trade-study)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: yuyasugo, at: Fri May 17 19:40:52 JST 2024 -->

<!--te-->


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

### Trade Study Setup

```MATLAB
% Define parameter ranges and values
% overall
span_range = 1.5;  % [m] max is 1.52 m (5ft)
AR_range = 3.8;             % [-]
% M2
% cabinetMass_range = 6 : -0.1 : -3; % [kg]
cabinetMass_range = 1 : .3 : 6; % [kg]
% M3
nPassengers_range = 26; % [-] only whole numbers
windSpeed_range = 0:1:16; % [m/s]
```
This is the section that defines the design space of the trade study. In the section above, `span` `AR` `cabinetMass` `nPassengers` and `windSpeed` are being varied. Because of the way the following section is coded, these can be either a scalar value, or an array with increments as seen above. 

With these ranges, we can take 2 approaches: we can have X number of nested for-loops with each layer being a range of variables, or we can "flatten" all of the possible combinations into one single array. This allows to track and estimate how much progress you have made in the design space, which is shown below. 

```MATLAB
% Generate grids of parameter values
[AR, cabinetMass, nPassengers, windSpeed] = ndgrid( ...
    AR_range, ...
    cabinetMass_range, ...
    nPassengers_range, ...
    windSpeed_range);

% Generate grids of indices
[AR_index, cabinetMass_index, nPassengers_index, windSpeed_index] = ndgrid( ...
    1:numel(AR_range), ...
    1:numel(cabinetMass_range), ...
    1:numel(nPassengers_range), ...
    1:numel(windSpeed_range));

% Combine parameter grids and indices
combined = cat(2, ...
    reshape(AR, [], 1), ...
    reshape(cabinetMass, [], 1), ...
    reshape(nPassengers, [], 1), ...
    reshape(windSpeed, [], 1), ...
    reshape(AR_index, [], 1), ...
    reshape(cabinetMass_index, [], 1), ...
    reshape(nPassengers_index, [], 1), ...
    reshape(windSpeed_index, [], 1));
```

It look me a long long time to understand what this was doing, but here's my attempt at it (if it doesn't make sense, there's an example after this that should simplify it).

`ndgrid` creates a gird of data in N-dimensions, based on the number of input arrays. This is used in combination with the next 2 steps to create all possible combinations. In a simplified case, think of a function of 2 variables, $`f(x, y)`$. If you create an array for $`x`$ and $`y`$, you can't really plot it unless you create all possible combinations of $`(x, y)`$ within the bounds of the 2 arrays. Then you can input this grid into $`f(X, Y)`$ with capital letters denoting grids instead of 1D arrays. 


`reshape` as the name suggests, reshapes the grid created by `ndgrid`. The way used by the code snipped above is it reshapes the multi-dimensional grid into one large column vector. Per the Matlab doc page, `reshape(A, n1, n2)` returns array `A` reshaped into a `n1-by-n2` dimension array. For us, we want to create a 1D, column vector so `n2=1`, and `n1=[]` since we don't care at this point how many rows it has. 

`cat` is short for concatenate, and it is used like `cat(dim, A1, A2, A3...)` . `dim` refers to the dimension the arrays should be added along, so in the case of `dim = 2` it means along the columns so sideways. 

With the 3 functions, it basically creates a `combined` 2D array with the columns being `[AR, cabinetMass, nPassengers, windSpeed, AR_index, cabinetMass_index, nPassengers_index, windSpeed_index]`

Here's an example of what PT is doing to create one long list of all possible combinations in a (hopefully) simpler example. 

```MATLAB
a = ["a_1", "a_2", "a_3", "a_4"];
b = ["b_1", "b_2", "b_3", "b_4"];
c = ["c_1", "c_2", "c_3", "c_4"];

[A, B, C] = ndgrid(a, b, c)

combined = cat(2, reshape(A, [], 1), reshape(B, [], 1), reshape(C, [], 1))
```

```
    "a_1"    "b_1"    "c_1"
    "a_2"    "b_1"    "c_1"
    "a_3"    "b_1"    "c_1"
    "a_4"    "b_1"    "c_1"
    "a_1"    "b_2"    "c_1"
    "a_2"    "b_2"    "c_1"
    "a_3"    "b_2"    "c_1"
    "a_4"    "b_2"    "c_1"
    "a_1"    "b_3"    "c_1"
    "a_2"    "b_3"    "c_1"
    "a_3"    "b_3"    "c_1"
    "a_4"    "b_3"    "c_1"
    "a_1"    "b_4"    "c_1"
    "a_2"    "b_4"    "c_1"
    "a_3"    "b_4"    "c_1"
    "a_4"    "b_4"    "c_1"
    "a_1"    "b_1"    "c_2"
    "a_2"    "b_1"    "c_2"
    "a_3"    "b_1"    "c_2"
    "a_4"    "b_1"    "c_2"
    "a_1"    "b_2"    "c_2"
    "a_2"    "b_2"    "c_2"
    "a_3"    "b_2"    "c_2"
    "a_4"    "b_2"    "c_2"
    "a_1"    "b_3"    "c_2"
    "a_2"    "b_3"    "c_2"
    "a_3"    "b_3"    "c_2"
    ... you get the idea :)
```

```MATLAB
lengthCombined = size(combined, 1); % calculating the length once (rather than every time it's looped)

% Create a matrix to store the calculated results
planes = cell(1, lengthCombined);
```


With this, the length (number of rows) of this can be determined, and then a creates a cell array of the length to store the returned `plane` struct with all of the results in it as well.

```MATLAB
% Set up a timer to guess how long it takes to run
tic
usedTimer = 0;
timeNow = datetime('now');
```

This code predicts how long the entire trade study will take, and these couple of lines sets that up. 

### Trade Study

```MATLAB
% Iterate over combinations
for i = 1:lengthCombined

    % Extract parameter values and indices for the current combination
    current_AR = combined(i, 1);
    current_cabinetMass = combined(i, 2);
    current_nPassengers = combined(i, 3);
    current_windSpeed = combined(i, 4);
    current_span = span_range;

    %     Print the current plane specs so user knows it's running
    fprintf('Plane:              %.0f of %.0f\nSpan [m]:           %.2f\nCabinet mass [kg]:  %.2f\nNum Passengers [-]: %.2f\nAR:                 %.1f\nWind Speed [m/s]:   %.2f\n\n',...
       i, lengthCombined, current_span, current_cabinetMass, current_nPassengers, current_AR, current_windSpeed);
```
We now being to iterate through all of the combinations of the design space. It gets the current index's variables and the outputs it so that the user can know the progress it's made. 

```MATLAB
    % Assign wind speed to environment
    environment.windSpeed = current_windSpeed;

    % Assign currents to plane structure
    plane.AR = current_AR;
    plane.massPayloads2 = current_cabinetMass;
    plane.nPayloads3 = current_nPassengers;
    plane.b = current_span;
    plane.hWinglet = 0.1 * plane.b;

    % Based on V3 numbers
    plane.lFuse = 53 * 0.0254; % [in -> m]

    % Wing params change accordingly
    plane.c = plane.b/plane.AR;
    plane.S = plane.b*plane.c;
    plane.croot = 2*plane.c / (1 + plane.taperRatio);
    plane.ctip = plane.croot*plane.taperRatio;
    
```
Now it updates the `plane` struct with the current values of the variables being traded, along with updating some of the `plane` elements. 
$$` c  = \frac{b}{AR} `$$
$$` S_{ref} = b\ c `$$
$$ `c_{root} =  \frac{2\ c}{1 + \lambda} `$$
$$` c_{tip} = \lambda\ c_{root}  `$$



```MATLAB
    % Tail params change accordingly
    plane = sizeTail(plane);
    % tail sized in definePlane
```
The tail is roughly sized based on the new planform specs for this specific plane. More in-depth sizing of the tail is done by the Aero S&C lead but for initial estimates, this [`sizeTail`](./sizeTail.md) function is used. 

```MATLAB
    % Simulating competition
    [m2results, m3results, plane] = SimulateCompetition(plane, environment);
```
Then, the main part that does all of the prediction is here! PT calls `SimulateCompetition` which takes in the current plane and environment, and returns the results and the plane struct. See [`SimulateCompetition`](./SimulateCompetition.md) for more details. 
