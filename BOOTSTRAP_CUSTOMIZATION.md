# Bootstrap Customization - 613 Mitzvot

## Overview

Bootstrap has been customized to match the purple-blue color theme of the 613 Mitzvot app.

## Color Palette

### Primary Colors

- **Primary Blue**: `#3498db` - Used for links, buttons, active states
- **Secondary Dark**: `#2c3e50` - Dark blue-gray for headers and emphasis
- **Success Green**: `#155724` - Dark green for positive mitzvot
- **Danger Red**: `#721c24` - Dark red for negative mitzvot
- **Warning Orange**: `#f57c00` - Orange accents
- **Info Blue**: `#1976d2` - Information highlights

### Theme Colors

- **Purple Light**: `#667eea` - Body gradient start
- **Purple Dark**: `#764ba2` - Body gradient end
- **Blue Bright**: `#3498db` - Primary interactive color
- **Blue Darker**: `#2980b9` - Darker blue variant

### Mitzvot-Specific Colors

- **Positive Background**: `#d4edda` (light green)
- **Positive Text**: `#155724` (dark green)
- **Negative Background**: `#f8d7da` (light pink/red)
- **Negative Text**: `#721c24` (dark red)

### Gray Scale

- `$gray-100`: `#f8f9fa` (lightest)
- `$gray-200`: `#e9ecef`
- `$gray-300`: `#dee2e6`
- `$gray-400`: `#ced4da`
- `$gray-500`: `#bfc5cc`
- `$gray-600`: `#6c757d`
- `$gray-700`: `#555555`
- `$gray-800`: `#343a40`
- `$gray-900`: `#2c3e50` (darkest)

## Custom Utility Classes

The custom Bootstrap build includes additional utility classes:

### Gradient Backgrounds

```html
<div class="bg-gradient-primary">
  <!-- Dark blue-gray to bright blue gradient -->
</div>

<div class="bg-gradient-purple">
  <!-- Purple gradient (matches body background) -->
</div>
```

### Mitzvot Type Classes

```html
<span class="text-positive">Positive Mitzvah Text</span>
<span class="text-negative">Negative Mitzvah Text</span>

<div class="bg-positive">Positive Mitzvah Badge</div>
<div class="bg-negative">Negative Mitzvah Badge</div>
```

## Build Process

### Rebuild Custom Bootstrap

When you make changes to the color variables or need to update Bootstrap:

```bash
npm run build:vendor
```

This command:

1. Compiles `styles/scss/custom-bootstrap.scss`
2. Outputs to `vendor/bootstrap/css/bootstrap.min.css`
3. Copies all other vendor dependencies

### Edit Color Variables

To change the color scheme:

1. Edit `styles/scss/custom-bootstrap.scss`
2. Modify the variables at the top of the file
3. Run `npm run build:vendor`
4. The changes will be reflected in your app immediately

## File Structure

```
/styles
  /scss
    custom-bootstrap.scss    # Custom Bootstrap theme with color variables
  app.css                    # Additional custom styles

/vendor
  /bootstrap
    /css
      bootstrap.min.css      # Compiled custom Bootstrap (generated)
    /js
      bootstrap.bundle.min.js # Bootstrap JS

/scripts
  build-vendor.js            # Build script that compiles SCSS
```

## Styling Philosophy

1. **Bootstrap for structure** - Use Bootstrap classes for layout, grid, buttons, forms
2. **Custom colors throughout** - All Bootstrap components now use your purple-blue theme
3. **Custom CSS for specifics** - `app.css` adds app-specific styles on top of Bootstrap
4. **Consistent color coding** - Green = positive mitzvot, Red = negative mitzvot everywhere

## Benefits

✅ Consistent color theme across all Bootstrap components  
✅ Buttons, badges, alerts, forms all match your purple-blue palette  
✅ Reduced need for custom CSS overrides  
✅ Easy to maintain and update colors in one place  
✅ Professional, cohesive visual design

## Notes

- The body gradient (`#667eea` → `#764ba2`) is still applied via `app.css` since Bootstrap variables can't handle gradients
- The custom SCSS file imports only the Bootstrap components you're using to keep file size optimal
- Deprecation warnings from Sass are expected and don't affect functionality (Bootstrap will update to modern Sass in future versions)
