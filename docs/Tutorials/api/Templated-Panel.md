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
