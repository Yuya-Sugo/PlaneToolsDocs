# `defineEnvironment.m`
> Yuya Sugo, Performance Lead 2024-2025, USC AeroDesign Team </br> 5/14/2024

## Main Purpose
This function returns an `environement` struct that stores information about the conditions the plane is flying at. This is mainly used for headwind studies.

## Code Breakdown
```MATLAB
function [environment] = defineEnvironment(location)
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
environment = [];
    % density in kg/m^3
    if location == "Tucson"
        environment.dens = 1.14;
        environment.windSpeed = 3; % m/s
        environment.windDirection = deg2rad(290);
        environment.runwayDirectionUpwind = deg2rad(290);
    elseif location == "Whittier"
        environment.dens = 1.2;
        environment.windSpeed = 1; % m/s
        environment.windDirection = deg2rad(180);
        environment.runwayDirectionUpwind = deg2rad(200);
    elseif location == "Wichita"
        environment.dens = 1.15;
        environment.windSpeed = 6.5; % m/s
        environment.windDirection = deg2rad(190);
        environment.runwayDirectionUpwind = deg2rad(200);
    elseif location == "Lucerne"
        environment.dens = 1.2;
        environment.windSpeed = 2; % m/s
        environment.windDirection = 0;
        environment.runwayDirectionUpwind = 0;
    else
        error('Unknown environment')
    end

end
```
Based on the input location, returns struct of environment data. 