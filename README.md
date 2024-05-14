# ADT PlaneTools (PT) Documentation

> Yuya Sugo, Performance Lead 2024-2025, USC AeroDesign Team </br> 5/14/2024

## Intention

The purpose of this series of documentation is to lay out the detailed explanation of the entire code in chunks, and allows for new users who are interested to get a overview of what is happening behind that yields these results. 

## What is PlaneTools?

PlaneTools is an in-house MATLAB code that simulates the performance of theoretical planes using physics models in a time-based environment. Based on the predicted "best plane" that the scores are going to be normalized against, PT finds the ADT plane that can score the highest! The overall flow of PT can be seen in this beautiful flow chart made by Jude Sorkin (Perf. Lead 2023-24) but we'll delve deeper into each file later on!

![PTFlowChartJude](./PlaneTools%20Flowchart.jpeg)

## Current Version

This version is based off Jude Sorkin's (Performance Lead 2023-24) final commit to the `devel` brach made on 05/12/24.

## GitHub

Since the first version of PT, the code has always been available upon request to anyone on the team. Contact your Performance Lead [usc.adt.performance@gmail.com](mailto:usc.adt.performance@gmail.com) to be added onto the GitHub. For more information on how to use GitHub or git in general, there are many useful, beginner friendly videos on YouTube to get you started!

## Organization of Documentation

Each MATLAB file in the code base will have it's own documentation file that describes and layouts the variables (meaning, units, type), what the code is doing, and any additional background information that may be required. To gain an overview of how the entire code structure works, see the below section. Each indent indicates a layer down, where it's parent is the first time said MATLAB file is called. 

## Overview of the Code Structure

- `TradeStudy.m` Defines design space, runs trade study, calculates scores, and identifies best plane
    - `definePlane.m` Creates a plane struct that holds basically all of the information related to the plane
    - `defineEnvironment.m` Creates an environment struct that defines the conditions the plane is flying at (mainly used for headwind studies)
