# `definePlane.m`
> Yuya Sugo, Performance Lead 2024-2025, USC AeroDesign Team </br> 5/14/2024


<!--ts-->
* [definePlane.m](#defineplanem)
   * [Main Purpose](#main-purpose)
   * [Variables](#variables)
      * [General](#general)
      * [Wing](#wing)
      * [Winglets](#winglets)
      * [Fuselage](#fuselage)
      * [Tail](#tail)
      * [Propulsion](#propulsion)
      * [Landing Gear](#landing-gear)
      * [Mission 2](#mission-2)
      * [Mission 3](#mission-3)
   * [Code Breakdown](#code-breakdown)
   * [Add/Edit/Remove Component Library .mat Files](#addeditremove-component-library-mat-files)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: yuyasugo, at: Wed May 29 00:49:46 JST 2024 -->

<!--te-->

## Main Purpose
This function defines all variables that are related to a plane. This is expected to change as the trade study redefines aircraft parameters. You are going to have to update the derived parameter, after changing the independent parameters. It is **not** automatic, as in entering a new `AR`
 will not automatically update the `b` and `c` values.



## Variables
All defined element in the plane struct is shown in the tables below, categorized by what it represents. The columns are split into the following categories:
| Variable | Variable Meaning | Variable Type | Use | Source |
|----------|------------------|---------------|-----|--------|
### General
| General |---|---|---|---|
|---|---|---|---|---|
| `massBuildup` | Should conduct mass buildup | Boolean | Used in MassBuildup/massBuildup.m |  |
| `m2results` | Mission 2 Performance Results | Struct | TOFL, VTO, Vstall, nLaps, missionTime, *performance*, score, etc | Populated by SimulateComp in TradeStudy.m |
| `m3results` | Mission 3 Performance Results | Struct | TOFL, VTO, Vstall, nLaps, missionTime, *performance*, score, etc | Populated by SimulateComp in TradeStudy.m |

Note: *performance* stores time-based information of: `Vstall`, `t`, `V`, `s`, `CL`, `loadFactor`, `Pinduced`, `Pparasite`, `Vb`, `propspeed`, `N`, `J`, `CT`, `thrust`, `Cp`, `Pshaft`, `proptorque`, `I`, `Pelectric`, `cRate`, `Paircraft`, `VbUnderLoad`, `etaMotor`, `etaProp`, `eta`, `throttle`, `r`, `Ve`, and boolan `stall`

### Wing
| Wing |---|---|---|---|
|---|---|---|---|---|
| `b` | Span | Double |  |  |
| `AR` | Aspect Ratio | Double |  |  |
| `c` | Mean Chord | Double |  |  |
| `S` | Reference Area | Double |  |  |
| `wingControlFraction` | Chord-wise Wing Control Fraction | Double |  |  |
| `tcRatio` | Thichness-Chord Ratio | Double |  |  |
| `taperRatio` | Taper Ratio | Double |  |  |
| `croot` | Root Chord | Double |  |  |
| `ctip` | Tip Chord | Double |  |  |
| `airfoilCoordinatesFile` | Airofoil Coordinates File | Char Array |  |  |
| `airfoilPerimeter` | Airofoil Perimeter | Double |  | Found duing calcMass_BuiltupWing |
| `CLmax` | 2D/3D? Coefficient of Lift | Double |  |  |
| `wingThickness` | Dimensional Wing Thickness | Double |  |  |
| `wingThicknessLocation` | Max Wing Thickness Location | Double |  |  |
| `CLgroundRoll` | 2D/3D? Coefficient of Lift at Ground Roll | Double |  |  |
| `hWing` | Wing's Height above Ground | Double | Used in LG mass estimate and ground effect drag est. |  |
| `nStruct` | Max Structural Load Factor | Double | Used in CheckLimits.m |  |
| `webMaterial` | Wing Web Material | Char Array | Used in MassBuildup/sparSizerGM.m |  |
| `wingBuildMethod` | Wing Build Method | Char Array | Used in MassBuildup/massBuildup.m |  |
| `controlSurfMat` | Wing Control Surface Material | Char Array | Used in MassBuildup/calcMass_BuiltupWing.m |  |
| `wingMat` | Wing Surface Material | Char Array | Used in PhysicsModels/dragBuildup.m | From material.mat (includes density and surface roughness) |

### Winglets
| Winglets |---|---|---|---|
|---|---|---|---|---|
| `hWinglet` | Height of Winglets (span) | Double | Used for drag and mass buildup |  |
| `taperRatioWinglet` | Winglet Taper Ratio | Double | Used for mass buildup |  |
| `mWinglets` | Mass of Winglets | Double | Used for mass buildup |  |
| `wingletAirfoilCoordinatesFile` | Winglet Airfoil Coords File Path | Char Array |  |  |

### Fuselage
| Fuselage |---|---|---|---|
|---|---|---|---|---|
| `lFuse` | Length of Fuselage | Double |  |  |
| `wFuse` | Width of Fuselage | Double |  |  |
| `hFuse` | Height of Fuselage | Double |  |  |
| `fuseMat` | Fuselage Material | Char Array | Used for drag and mass buildup |  |
| `fuseBuildMethod` | Fuselage Build Method | Char Array |  |  |

### Tail
| Tail |---|---|---|---|
|---|---|---|---|---|
| `Vh` | Tail Volume Coefficient - Horizontal | Double |  |  |
| `Vv` | Tail Volume Coefficient - Vertical | Double |  |  |
| `nTails` | Number of Tails | Double | Not Traded |  |
| `tailMat` | Tail Material | Char Array |  |  |
| `bTail` | Span of Tail | Double |  |  |
| `hTail` | Height of Tail | Double |  |  |
| `cTailV` | Chord of Vertical Tail | Double | Mass Build up |  |
| `cTailH` | Chord of Horizontal Tail | Double | Mass Build up |  |
| **Horizontal** |---|---|---|---|
| `ARh` | Aspect Ratio of Horizontal | Double |  |  |
| `lh` | Moment Arm of Horizontal | Double |  |  |
| `Sh` | Ref Area of Horizontal | Double |  |  |
| `bh` | Span of Horizontal | Double |  |  |
| `ch` | Average Chord of Horizontal | Double |  |  |
| **Vertical** |---|---|---|---|
| `lv` | Moment Arm of Vertical | Double |  |  |
| `Sv` | Ref Area of Vertical | Double |  |  |
| `cv` | Average Chord of Vertical | Double |  |  |
| `bv` | Span of Vertical | Double |  |  |
| `ARv` | Aspect Ratio of Vertical | Double |  |  |

### Propulsion
| Propulsion |---|---|---|---|
|---|---|---|---|---|
| `motorType` | Name of Motor | Char Array |  | From motor.mat (Kv, R, m, maxPower, (length,) (diam)) |
| (local, not plane field) `motor` | Motor | Struct |  |  |
| `Kv` | Kv | Double | relates peak voltage and rotation speed |  |
| `motorMaxPower` | Motor's Max Power | Double |  |  |
| (local, not plane field) `Rmotor` | Resistance of the Motor | Double |  |  |
| `motorLength` | Motor Dimensions (Length) | Double | Motor Mount Mass Buildup |  |
| `motorDiam` | Motor Dimensions (Diameter) | Double |  |  |
| `nMotors` | Number of Motors | Double |  |  |
| `ESCMaxCurrent` | ESC's maximum instantaneous current | Double |  |  |
| `ESCContinuousCurrent` | ESC's maximum continuous current | Double |  |  |
| (local, not plane field) `Resc` | Resistance of ESC | Double |  |  |
| (local, not plane field) `Rwire` | Resistance of Wire | Double |  |  |

### Landing Gear
| Landing   Gear |---|---|---|---|
|---|---|---|---|---|
| `lgType` | Landing Gear Type | Char Array | Drag and Mass buildup |  |
| `lgMat` | Landing Gear Material | Char Array | Mass buildup |  |
| `rr` | Rolling Resistance | Double | Prop/Flight Model |  |

### Mission 2
| Mission   2 |---|---|---|---|
|---|---|---|---|---|
| `D2` | Mission 2 Propeller Diameter | Double |  |  |
| `P2` | Mission 2 Propeller Pitch | Double |  |  |
| `A2` | M2 Propeller Curve Fitting Parameters | Double | Used in ThrustModel for C_T and C_Power Determination |  |
| `B2` | M2 Propeller Curve Fitting Parameters | Double | Used in ThrustModel for C_T and C_Power Determination |  |
| `C2` | M2 Propeller Curve Fitting Parameters | Double | Used in ThrustModel for C_T and C_Power Determination |  |
| `E2` | M2 Propeller Curve Fitting Parameters | Double | Used in ThrustModel for C_T and C_Power Determination |  |
| `F2` | M2 Propeller Curve Fitting Parameters | Double | Used in ThrustModel for C_T and C_Power Determination |  |
| `G2` | M2 Propeller Curve Fitting Parameters | Double | Used in ThrustModel for C_T and C_Power Determination |  |
| **M2 Bat** |---|---|---|---|
| `batteryType2` | Mission 2 Battery Name | Char Array |  | From battery.mat (capacity, R, Imax, (mass), nSeries) |
| `bat2maxCurrent` | Mission 2 Battery Max Current | Double |  |  |
| `bat2R` | Mission 2 Battery Resistance | Double |  |  |
| `nSeries2` | Mission 2 Battery Series Cell Count | Double |  |  |
| `nParallel2` | Mission 2 Battery Parallel Cell Count | Double |  |  |
| `bat2capacity` | Mission 2 Battery Capacity (like coulombs) | Double |  |  |
| `Eb2` | Mission 2 Battery Energy (like joules) | Double |  |  |
| `Rt2` | Mission 2 Total Resistance | Double |  |  |
| **M2 Payloads** |---|---|---|---|
| `nPayloads2` | Number of Mission 2 Paylaods | Double |  |  |
| `massPayloads2` | Mass of Mission 2 Payloads | Double |  |  |
| `DApayload2` | Drag Added of Mission 2 Paylaods | Double |  |  |
| `mPayloadExtras2` | Untradeable, fixed Mission 2 Mass | Double |  |  |
| `seed_m2` | ??? | Double | Used in TubeSizer |  |
| `Vmax2` | Max Speed Mission 2 | Double |  |  |

### Mission 3
| Mission   3 |---|---|---|---|
|---|---|---|---|---|
| `D3` | Mission 3 Propeller Diameter | Double |  |  |
| `P3` | Mission 3 Propeller Pitch | Double |  |  |
| `A3` | M3 Propeller Curve Fitting Parameters | Double | Used in ThrustModel for C_T and C_Power Determination |  |
| `B3` | M3 Propeller Curve Fitting Parameters | Double | Used in ThrustModel for C_T and C_Power Determination |  |
| `C3` | M3 Propeller Curve Fitting Parameters | Double | Used in ThrustModel for C_T and C_Power Determination |  |
| `E3` | M3 Propeller Curve Fitting Parameters | Double | Used in ThrustModel for C_T and C_Power Determination |  |
| `F3` | M3 Propeller Curve Fitting Parameters | Double | Used in ThrustModel for C_T and C_Power Determination |  |
| `G3` | M3 Propeller Curve Fitting Parameters | Double | Used in ThrustModel for C_T and C_Power Determination |  |
| **M3 Bat** |---|---|---|---|
| `batteryType3` | Mission 3 Battery Name | Char Array |  |  |
| `bat3maxCurrent` | Mission 3 Battery Max Current | Double |  |  |
| `bat3R` | Mission 3 Battery Resistance | Double |  |  |
| `nSeries3` | Mission 3 Battery Series Cell Count | Double |  |  |
| `nParallel3` | Mission 3 Battery Parallel Cell Count | Double |  |  |
| `bat3capacity` | Mission 3 Battery Capacity (like coulombs) | Double |  |  |
| `Eb3` | Mission 3 Battery Energy (like joules) | Double |  |  |
| `Rt3` | Mission 3 Total Resistance | Double |  |  |
| **M3 Payloads** |---|---|---|---|
| `nPayloads3` | Number of Mission 3 Paylaods | Double |  |  |
| `massPayloads3` | Mass of Mission 3 Payloads | Double |  |  |
| `DApayload3` | Drag Added of Mission 3 Paylaods | Double |  |  |
| `mPayloadExtras3` | Untradeable, fixed Mission 3 Mass | Double |  |  |
| `Vmax3` | Max Speed Mission 3 | Double |  |  |


## Code Breakdown
Mostly straight forward...


```MATLAB
plane.motorType = 'Scorpion_A_4220_540';
% plane.motorType = 'Scorpion_HKIII_5025_520KV_F3S';
warning('off')
load('motor.mat', plane.motorType);
motor = eval(plane.motorType);
plane.Kv = motor.Kv;
plane.motorMaxPower = motor.maxPower;
Rmotor = motor.R;
plane.motorLength = motor.length;
plane.motorDiam = motor.diam;
plane.nMotors = 2;
% plane.nMotors = 1;
plane.ESCMaxCurrent = 260;
plane.ESCContinuousCurrent = 110;
Resc = .0005;
Rwire = .01;
```

This section pulls information about the motor from the `motor.mat` database stored in the component library. The `Resc` and `Rwire` are fixed estimates as of now. `motor.mat` stores the `Kv`, resistance, mass, and max power of each motor in a struct named with its motor name as defined in `plane.motorType`.


```MATLAB
diameter = 12; %12x6, 12x8
pitch = 8;
% diameter = 14;
% pitch = 8;
propellerMAT = matfile('myFile2.mat');
allProps = propellerMAT.allProps;
diamIndices = find(allProps(:,1)==diameter);
pitchIndices = find(allProps(:,2)==pitch);
[index,~]=intersect(diamIndices,pitchIndices);
plane.D2 = diameter*0.0254;
plane.P2 = pitch;
plane.A2 = allProps(index,3);
plane.B2 = allProps(index,4);
plane.C2 = allProps(index,5);
plane.E2 = allProps(index,6);
plane.F2 = allProps(index,7);
plane.G2 = allProps(index,8);
```
This section of the code reads in `myFile2.mat` stored in the component library folder, and stores all the prop information available to PT in `allProps` 2D array with columns: `diameter`, `pitch`, `A`, `B`, `C`, `E`, `F`, `G`. Them it finds the row with the right diameter and pitch, and stores the propeller coefficients for specific missions.
The `find` function returns a 1D array of zeros and ones to see where the diameter or pitch match the one we are looking for. The `intersect` of these 2 arrays is the row we are looking for. 

```MATLAB
% Battery
plane.batteryType3 = 'MA_2250_8s'; 
load('battery.mat', plane.batteryType3);
battery3 = eval(plane.batteryType3);
```
This section loads battery information just based off the battery name from the `battery.mat` database stored in the component library. This provides battery information in a struct  containing `capacity` (capacity per cell, rather than whole battery, **in units of Ah**) `R` `Imax` `mass` `nSeries`


```MATLAB
plane.bat3maxCurrent = battery3.Imax;
plane.bat3R = battery3.R;

% Total energy
plane.nSeries3 = battery3.nSeries;
plane.nParallel3 = 1;
plane.bat3capacity = battery3.capacity*plane.nParallel3;
plane.Eb3 = plane.bat3capacity*plane.nSeries3*3.7*3600;

% Total resistance
plane.Rt3 = Resc + Rwire + Rmotor + (plane.bat3R/plane.nParallel3);
```
With the values from the database, information relating to the whole battery was calcualted: 

- Battery Capacity: capacity per cell $` \times `$ # parallel
- Battery Energy: battery capacity $` \times `$ # series $` \times `$ 3.7 V (I think this is nominal voltage for a LiPo battery) $` \times `$ 3600 (hours to second conversion)
- Battery Resistance: battery resistance $`/`$ # parallel

## Add/Edit/Remove Component Library `.mat` Files

In the Component Library, there are Matlab scrips with the names `add____.m`. Editing those, and running them will allow for the new components to be added to the `.mat` files and `definePlane` to use them. 