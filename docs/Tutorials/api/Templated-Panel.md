# BentoBox TemplatedPanel Documentation

The BentoBox TemplatedPanel is a powerful tool for Minecraft developers, enabling the creation of customizable inventory-based user interfaces (UIs) with ease. By defining panel layouts in YAML, developers can quickly adjust UI elements without needing to alter the codebase extensively. Here's a detailed breakdown of how to configure a TemplatedPanel using YAML.

## Panel Definition

### Panel Identification
- `detail_panel`: Define the unique name for the panel for reference in the code.

### Panel Title
- `title`: Set the display title of the panel. This title can be localized through a reference in the locale file.

### Panel Type
- `type`: Choose the type of inventory to display. Options include `INVENTORY`, `HOPPER`, and `DROPPER`.

### Background and Border
- `background`: Customize the background of the panel using Minecraft items. For example, `BLACK_STAINED_GLASS_PANE` can be used for aesthetic effect.
- `border`: Define the appearance of the panel's border, again using Minecraft items. This helps to contrast the panel items.

### Display Configuration
- `force-shown`: Specify which rows in the panel are to be displayed, affecting the panel's vertical size.

## Content Configuration

### Button Layout and Functionality
- `content`: Within this section, detail each item or button in the panel. Use row and column numbers to position each element.
  - `icon`: Set the Minecraft item to be used as the button icon.
  - `title`: Provide a title for the button, which can be localized.
  - `description`: Add a description for the button, also localizable.
  - `data`: Include data relevant to the button's function, such as the type of action it triggers.
  - `actions`: Define the actions that occur when the button is interacted with, specifying the type of click and any tooltips.

### Reusable Buttons
- `reusable`: Define templates for buttons that are used multiple times within the panel.
  - Within this section, specify details like the button's icon, title, description, and associated data.

## Example Button Configuration
- For a button at row 1, column 2:
  ```yaml
  1:
    2:
      icon: STONE
      title: level.gui.buttons.all_blocks.name
      description: level.gui.buttons.all_blocks.description
      data:
        type: TAB
        tab: ALL_BLOCKS
      actions:
        view:
          click-type: unknown
          tooltip: level.gui.tips.click-to-view
  ```

- For a reusable button named `material_button`:
  ```yaml
  reusable:
    material_button:
      title: level.gui.buttons.material.name
      description: level.gui.buttons.material.description
      data:
        type: BLOCK
  ```

This TemplatedPanel system offers BentoBox developers a streamlined and flexible way to design and implement interactive UI elements in the game, enhancing user engagement and functionality.

# TemplatedPanelBuilder Documentation

The `TemplatedPanelBuilder` class is part of the BentoBox API, designed to facilitate the creation of `TemplatedPanel` objects. It provides a fluent interface for constructing panels with various customization options, such as templates, user context, world context, and listeners. Here's an overview of its functionality and usage.

## Class Overview

`TemplatedPanelBuilder` is used for building instances of `TemplatedPanel`. It allows for setting various parameters and configurations necessary for the panel's operation within the Minecraft world, specifically within the BentoBox framework.

## Methods

### Template Methods

- `template(String guiName, File dataFolder)`: Sets the template for the panel based on the GUI name and the data folder. Returns the `TemplatedPanelBuilder` instance for chaining.
- `template(String panelName, String templateName, File dataFolder)`: Sets the template for the panel based on the panel name, template name, and the data folder. Introduced in version 1.20.0. Returns the `TemplatedPanelBuilder` instance for chaining.

### User Method

- `user(User user)`: Sets the user for whom the panel is being built. Returns the `TemplatedPanelBuilder` instance for chaining.

### World Method

- `world(World world)`: Sets the world context for the panel. Returns the `TemplatedPanelBuilder` instance for chaining.

### Parameters Method

- `parameters(@NonNull String... parameters)`: Sets the parameters for the panel title. Returns the `TemplatedPanelBuilder` instance for chaining. Available from version 1.20.0.
- Example: `panelBuilder.parameters("[name]", this.user.getName());` places the user's name into the title of the panel

### Listener Method

- `listener(PanelListener listener)`: Adds a `PanelListener` to the panel for handling user interactions. Returns the `TemplatedPanelBuilder` instance for chaining.
- Listeners are not required as functionality for moving to another tab, or reacting to a click is handled within the API.
- You may only need a Listener if you need some custom functionality.

### Type Builder Registration

- `registerTypeBuilder(String type, BiFunction<ItemTemplateRecord, TemplatedPanel.ItemSlot, PanelItem> buttonCreator)`: Registers a new button type builder for the panel. Returns the `TemplatedPanelBuilder` instance for chaining.
- Example:
```
        panelBuilder.registerTypeBuilder("NEXT", this::createNextButton);
        panelBuilder.registerTypeBuilder("PREVIOUS", this::createPreviousButton);
        panelBuilder.registerTypeBuilder("BLOCK", this::createMaterialButton);
```
- When the button with the associated name is clicked, the appropriate method will be called. It is passed the ItemTemplateRecord, the ItemSlot, and the PanelItem.

### Build Method

- `build()`: Constructs and returns a `TemplatedPanel` instance based on the provided configuration.

## Getters

- `getPanelTemplate()`: Retrieves the current `PanelTemplateRecord`.
- `getUser()`: Gets the `User` object associated with the panel.
- `getWorld()`: Returns the `World` context for the panel.
- `getParameters()`: Retrieves the list of parameters set for the panel title.
- `getListener()`: Returns the `PanelListener` attached to the panel.
- `getObjectCreatorMap()`: Provides access to the map linking objects with their panel item creators.

## Variables

- `panelTemplate`: Stores the GUI template record.
- `user`: Holds the reference to the user who opens the GUI.
- `world`: Represents the world where the GUI operates.
- `listener`: Stores the `PanelListener` for handling GUI interactions.
- `parameters`: A list to store parameters for the title object.
- `objectCreatorMap`: A map linking object types to their respective panel item creators.

## Usage

To use the `TemplatedPanelBuilder`, instantiate it and chain its methods to configure the panel as required. Once all configurations are set, call the `build()` method to create a `TemplatedPanel` instance.

Example:

```
        // Start building panel.
        TemplatedPanelBuilder panelBuilder = new TemplatedPanelBuilder();
        panelBuilder.user(this.user);
        panelBuilder.world(this.user.getWorld());

        panelBuilder.template("detail_panel", new File(this.addon.getDataFolder(), "panels"));

        panelBuilder.parameters("[name]", this.user.getName());

        panelBuilder.registerTypeBuilder("NEXT", this::createNextButton);
        panelBuilder.registerTypeBuilder("PREVIOUS", this::createPreviousButton);
        panelBuilder.registerTypeBuilder("BLOCK", this::createMaterialButton);

        panelBuilder.registerTypeBuilder("FILTER", this::createFilterButton);

        // Register tabs
        panelBuilder.registerTypeBuilder("TAB", this::createTabButton);

        // Register unknown type builder.
        panelBuilder.build();
```

