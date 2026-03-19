# Publishing Your Mod to GX.store

## How to Upload

1. **Create a zip** of your mod folder:
   - **IMPORTANT**: Zip the *contents* of the folder, not the folder itself. `manifest.json` must be at the **root** of the zip (not inside "Izuku Midoriya Rising/manifest.json")
   - Include: `manifest.json`, `license.txt`, and all folders (`wallpaper/`, `music/`, `sound/`, `keyboard/`, `shader/`, `webmodding/`)
   - Include: `Deku_Nut.png` (or whatever your icon file is named)
   - Ensure `webmodding/` contains all CSS files: `theme.css`, `opera.css`, `youtube.css`, etc.
   - **Do NOT** include: `scripts/`, `README.md`, `PUBLISHING.md`, `.git/`, or `Deku_Final_Smash.mp4` (source video)

2. **Go to** [create.gx.games/mods](https://create.gx.games/mods)

3. **Sign in** with your GX.games account

4. **Create a studio** (if you haven't) in the Studios tab

5. **Upload** your zip file

6. **Fill in the backend**:
   - Title, description, tags (e.g. "My Hero Academia", "anime", "wallpaper")
   - Add promo images in the Media tab (screenshots of your mod in action)
   - Set thumbnail/icon if prompted

7. **Publish**: In the Publishing tab, check "public" when ready

---

## Pre-Upload Checklist

- [ ] Manifest has no JSON errors (no `//` comments)
- [ ] All referenced files exist (icon, wallpaper, music, sounds, webmodding CSS files)
- [ ] Icon is 512×512 PNG
- [ ] license.txt is filled out
- [ ] Test mod loads locally in Opera GX before zipping
