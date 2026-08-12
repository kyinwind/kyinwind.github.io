# MichaelDev

Personal app showcase and help center for MichaelDev.

The site is built with [Astro](https://astro.build/) and [Starlight](https://starlight.astro.build/), then published to GitHub Pages.

## Local development

```bash
npm install
npm run dev
```

## Build

```bash
npm run build
```

The generated site is written to `dist/`.

## Content structure

- App data: `src/data/apps.ts`
- English home page: `src/pages/index.astro`
- Chinese home page: `src/pages/zh/index.astro`
- App detail pages: `src/pages/apps/[slug].astro`
- Chinese app detail pages: `src/pages/zh/apps/[slug].astro`
- Help center docs: `src/content/docs/`
- Images and static assets: `public/`

## Adding a new app

1. Add the app icon to `public/images/`.
2. Add the app record in `src/data/apps.ts`.
3. If the app needs help docs, add Markdown files under `src/content/docs/help/{app-slug}/`.
4. Run `npm run build` before publishing.

## Sync help docs from Feishu

The app help center can be regenerated from Feishu wiki sources:

```bash
python3 scripts/sync-feishu-app-help.py
python3 scripts/sync-feishu-videohero-help.py
npm run build
```

`sync-feishu-app-help.py` currently mirrors RightClickMate, TTSMate, and SongJing Assistant docs.

`sync-feishu-videohero-help.py` mirrors the VideoHero Chinese and English help centers:

```bash
python3 scripts/sync-feishu-videohero-help.py
npm run build
```

Both scripts convert Feishu pages to Starlight Markdown, download document images into `public/help-assets/`, and rewrite known Feishu wiki links to local site links.

## GitHub Pages

This repository uses `.github/workflows/deploy.yml` to publish the Astro build output.

In GitHub repository settings, set Pages source to **GitHub Actions**.
