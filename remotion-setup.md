# 🎬 Remotion Video Setup for Retro TTS

## Quick Start - Remotion Project

### 1. Create Remotion Project

```bash
# In a NEW folder (not in Presenter2.15.26)
cd c:\Users\Babz\Desktop
npx create-video@latest retro-tts-videos
```

Choose:
- Template: **TypeScript**
- Package manager: **npm** or **bun** (faster)

### 2. Project Structure

```
retro-tts-videos/
├── src/
│   ├── Root.tsx
│   ├── Composition.tsx
│   └── Videos/
│       ├── ThemeShowcase.tsx
│       ├── ThemeComparison.tsx
│       ├── HowToUse.tsx
│       ├── MatrixTheme.tsx
│       ├── VaporwaveTheme.tsx
│       ├── AmberTheme.tsx
│       ├── NeonTheme.tsx
│       └── MidnightTheme.tsx
├── public/
│   └── screenshots/  (put your TUI screenshots here)
└── package.json
```

---

## 🎥 Videos to Create

### 1. **Theme Showcase Loop** (30 seconds)
- Shows all 6 themes in succession
- 5 seconds per theme
- Smooth transitions
- Neon glow effects

### 2. **Theme Comparison** (45 seconds)
- Split screen showing themes side-by-side
- Highlights unique features of each
- Color palette showcase

### 3. **How to Use Tutorial** (60 seconds)
- Installation steps
- First launch
- Using the hotkey
- VU meter explanation
- Success demo

### 4. **Individual Theme Videos** (15 seconds each)
- One for each theme
- Shows the theme in action
- Displays key features
- Perfect for social media

---

## 📋 What You Need to Provide

### Screenshots Needed:

For each theme, capture:
1. **Ready state** - Idle, waiting
2. **Recording state** - VU meter active
3. **Processing state** - Converting speech
4. **Success state** - Text output shown

**How to capture:**
1. Run each theme (`SELECT_THEME.bat`)
2. Use **Win + Shift + S** (Windows Snipping Tool)
3. Save as PNG
4. Name like: `cyberpunk-ready.png`, `matrix-recording.png`, etc.

---

## 🎨 Remotion Components I'll Create

### ThemeShowcase.tsx
```typescript
// Animated showcase of a single theme
// - Fade in logo
// - Animate VU meter
// - Show text typing effect
// - Neon glow animations
```

### ThemeComparison.tsx
```typescript
// Side-by-side comparison
// - Split screen layout
// - Synchronized animations
// - Color palette display
```

### HowToUse.tsx
```typescript
// Tutorial video
// - Step-by-step guide
// - Animated instructions
// - Screen recording overlay
```

---

## 🚀 After Creating Videos

### Render Commands:

```bash
# Render all videos
npm run build

# Render specific video
npm run build -- --props='{"theme":"matrix"}'

# Output will be in out/ folder
```

### Upload to:
1. **YouTube** - Unlisted or public
2. **Streamblur.com** - Direct hosting
3. **GitHub** - In releases

### Embed on Landing Page:
```html
<video autoplay loop muted playsinline>
  <source src="videos/theme-showcase.mp4" type="video/mp4">
</video>
```

---

## 💡 Next Steps

1. I'll create the Remotion project files
2. You capture screenshots
3. I'll build the video compositions
4. You render the videos
5. I'll update the landing page with embeds

Ready? Let's do this! 🎬✨
