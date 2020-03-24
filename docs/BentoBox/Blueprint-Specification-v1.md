# BentoBox Blueprint Specification

**Version 1**

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).

## Introduction

This specification defines a format that describes a region (made up of blocks and entities) of a [Minecraft](https://minecraft.net) world for the purpose of serialization and storage to disk or to JSON-based database. It is designed in order to allow maximum cross-compatibility between platforms, versions, and various states of modification.

The goal of the BentoBox Blueprint format is to grant us the ability to serialize regions of a Minecraft world to disk or to any user-chosen storage method to be later placed back in the world, while avoiding to rely on third-party softwares or plugins to provide us the serialization and deserialization capabilities.

## Revision history

| Version | Date | BentoBox version | Description
|---|---|---|---|
| 1 | 2019-06-09 | [1.5.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/1.5.0) | Initial version, derivative of the BentoBox Schem format

## Definitions

### <a name="defMaterial"></a>Material

A [Material](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html) is an ID provided by the [Bukkit API](https://dev.bukkit.org/) that defines the literal type of a block or an item. It affects various rendering options client-side such as light, transparency or display. They represent a programmatical shortcut to the actual corresponding NamespacedKey.

## Specifications

### Format

The structure specified by this specification is persisted to the user-chosen storage method using the [JavaScript Object Notation](https://json.org) (JSON) format. The data must then be compressed using the ... data compression algorithm.

Files using this specification must use one of the following file extensions:
* `.blueprint` ;
* `.blu`

All field names in the specification are **case sensitive**.

### Schema

#### Fields

| Field name | Type | Description |
|---|---|---|
| name | `String` | Display name of the Blueprint |
| icon | `String` | [Material](#defMaterial) of the item representing the Blueprint in game as an icon |
| attached | `Array` | |
| entities | `Array` | |
| blocks | `Array` | |
| xSize | `integer` | |
| ySize | `integer` | |
| zSize | `integer` | |
| bedrock | `Array` | |