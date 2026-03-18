# My Hero Academia - Opera GX Mod Pack

Full My Hero Academia themed mod for Opera GX: animated wallpaper, sounds, theme, shaders, and web modding.

## Structure

```
OperaGX/
├── manifest.json          # Mod configuration
├── icon_512.png           # Icon (512×512) for GX.store
├── license.txt
├── wallpaper/             # Animated wallpapers
│   ├── dark.webm, dark.png
│   └── light.webm, light.png
├── music/                 # Background music (4 tracks for vertical remixing)
├── sound/                 # Browser sounds (clicks, tabs, etc.)
├── keyboard/              # Keyboard typing sounds
├── shader/                # Shaders: Hero Glow, Plus Ultra
├── webmodding/            # CSS for web pages
└── scripts/               # Helper scripts
```

## Checklist: What You Need to Add

1. **Wallpaper** (placeholder included)
   - Currently uses static `wallpaper/dark.png` and `wallpaper/light.png`
   - For **animated**: add `dark.webm` + `dark.png` (first frame), then update manifest:
     ```json
     "image": "wallpaper/dark.webm",
     "first_frame": "wallpaper/dark.png"
     ```

2. **Icon** (placeholder included)
   - Run `python scripts/create_icon.py` to generate, or add your own 512×512px

3. **Sounds** (optional)
   - Placeholder silent audio is included. Replace with MHA-themed sounds:
   - **Browser sounds**: `sound/*.wav` (click, hover, tab_close, etc.)
   - **Keyboard sounds**: `keyboard/*.wav` (letter, space, enter, backspace)
   - **Background music**: `music/track_1.wav` through `track_4.wav`

4. **Music format**: WAV or MP3 both work. For MP3, install ffmpeg and run `python scripts/generate_placeholders.py` to regenerate.

## Creating Your Wallpaper

**WebM from video:**
```bash
ffmpeg -i your_video.mp4 -c:v libvpx-vp9 -b:v 2M -an wallpaper/dark.webm
ffmpeg -i wallpaper/dark.webm -vframes 1 wallpaper/dark.png
```

## Load & Test

1. Open `opera:extensions` in Opera GX
2. Enable **Developer mode** (top right)
3. Click **Load unpacked** → select this folder
4. Open `opera:mods` to enable your mod

## Publish

- **Local share**: Pack extension in `opera:extensions` → produces .CRX file
- **GX.store**: [GX.create](https://create.gx.games/mods)

## Theme Customization

The manifest uses MHA-inspired colors:
- **Accent**: Green (HSL 145, 85%, 50%)
- **Secondary**: Dark blue/black

Edit `manifest.json` → `mod.payload.theme` to change.

## Shaders

Two shaders included:
- **Hero Glow**: Subtle green tint
- **Plus Ultra**: Animated wave effect

Users can toggle shaders in the mod settings.
