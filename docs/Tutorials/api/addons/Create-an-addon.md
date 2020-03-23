# Create an Addon

## Introduction

BentoBox relies on **_Addons_ to provide new features or new _Gamemodes_**.
This tutorial will guide you through the process of **creating your first addon**.
It also covers the defining features of a **_Gamemode_** and the necessary steps to create your own.

Creating an Addon is often easier and quicker than creating a plugin from scratch, because BentoBox provides [wrappers](https://en.wikipedia.org/wiki/Wrapper_function) and key API features.
Addons also have direct access to the other addons' API, unlike plugins, due to the [visibility principle of Java Classloaders](https://www.javatpoint.com/classloader-in-java).

In order to comfortably follow this tutorial, you should have previous experience in plugin development.
The addon development process is indeed very similar to the latter, and we will consider throughout this tutorial that you understand the key Java concepts, for the sake of concision.

## Table of Contents

[TOC]

## Preparing the project

### Import BentoBox as a dependency
