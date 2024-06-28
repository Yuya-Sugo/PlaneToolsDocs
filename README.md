# ADT PlaneTools (PT) Documentation

> Yuya Sugo, Performance Lead 2024-2025, USC AeroDesign Team </br> 5/14/2024

<!--ts-->
* [ADT PlaneTools (PT) Documentation](#adt-planetools-pt-documentation)
   * [Intention](#intention)
   * [What is PlaneTools?](#what-is-planetools)
   * [Current Version](#current-version)
   * [GitHub](#github)
   * [Organization of Documentation](#organization-of-documentation)
   * [Overview of the Code Structure](#overview-of-the-code-structure)
   * [Quick Reference to Useful Pages](#quick-reference-to-useful-pages)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: yuyasugo, at: Wed May 29 00:49:44 JST 2024 -->

<!--te-->

## Intention

The purpose of this series of documentation is to lay out the detailed explanation of the entire code in chunks, and allows for new users who are interested to get a overview of what is happening behind that yields these results. 

This is meant to be viewed on GitHub Desktop -- all of the formatting shuold work on the desktop version. Equations may not render properly on mobile versions of Github. 

## What is PlaneTools?

PlaneTools (PT) is an in-house MATLAB code that simulates the performance of theoretical planes using physics models in a time-based environment. Based on the predicted "best plane" that the scores are going to be normalized against, PT finds the ADT plane that can score the highest! The overall flow of PT can be seen in this beautiful flow chart made by Jude Sorkin (Perf. Lead 2023-24) but we'll delve deeper into each file later on!

![PTFlowChartJude](./Figures/PlaneTools%20Flowchart.jpeg)

## Current Version

This version of *PlaneToolsDocs* is based off Jude Sorkin's (Performance Lead 2023-24) final commit to the `devel` brach made on 05/12/24.

## GitHub

Since the first version of PT, the code has always been available upon request to anyone on the team. Contact your Performance Lead [usc.adt.performance@gmail.com](mailto:usc.adt.performance@gmail.com) to be added onto the GitHub. For more information on how to use GitHub or git in general, there are many useful, beginner friendly videos on YouTube to get you started!

## Organization of Documentation

Each MATLAB file in the code base will have it's own documentation file that describes and layouts the variables (meaning, units, type), what the code is doing, and any additional background information that may be required. To gain an overview of how the entire code structure works, see the below section. Each indent indicates a layer down, where it's parent is the first time the MATLAB file is called. 

## Overview of the Code Structure
> You can click on the file name to jump into the details of that MATLAB file!
- [`TradeStudy.m`](./TradeStudy.md) Defines design space, runs trade study, calculates scores, and identifies best plane
    - [`definePlane.m`](./definePlane.md) Creates a plane struct that holds basically all of the information related to the plane
    - [`defineEnvironment.m`](./defineEnvironment.md) Creates an environment struct that defines the conditions the plane is flying at (mainly used for headwind studies)
    - [`sizeTail.m`](./sizeTail.md) Updates the tail parameters in the plane struct, and returns updated plane struct. 
    - [`SimulateCompetition.m`](./SimulateCompetition.md) Simulates the plane flying at competition.
        - [`massBuildup.m`](./massBuildup.md) Estimates the mass of aircraft
            - [`calcMass_BuiltupWing.m`](./calcMass_BuiltupWing.md) Estimates the mass of builtup wing
            - [`calcMass_FoamcoreWing.m`](./calcMass_FoamcoreWing.md) Estimates the mass of Foamcore wing (seems depreciated, no documentation created.)
            - [`calcMass_Fuselage.m`](./calcMass_Fuselage.md) Estimates the mass of the fuselage
            - [`calcMass_FoamcoreTail.m`](./ca  lcMass_FoamcoreTail.md) Estimates the mass of a foam-core tail
            - [`calcMass_MotorMount.m`](./calcMass_MotorMount.md) Estimates the mass of motor mount(s)

## Quick Reference to Useful Pages
- [Plane Struct Variables](./definePlane.md)

