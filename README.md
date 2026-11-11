# Fengyifei XU — Engineering Portfolio

Live site: https://arash279.github.io/Arash_Portfolio/

Static portfolio built with Astro 6, MDX, native CSS, KaTeX and Shiki. Every push to `main` builds and deploys to GitHub Pages (`.github/workflows/pages.yml`).

## Run locally

Requires Node 24 and npm. From this directory:

```powershell
$env:ASTRO_TELEMETRY_DISABLED='1'
npm ci
npm run build
python scripts/check-site.py
npm run preview -- --host 127.0.0.1 --port 4321
```

Open http://127.0.0.1:4321/. For live editing use `npm run dev -- --host 127.0.0.1`. Python is needed only for the optional output checker or chart regeneration; normal npm builds do not require Python.

## Content and personal details

- `src/content/projects/*.mdx`: four case studies and validated metadata. Homepage and index use the same collection.
- `src/consts.ts`: confirmed name, photo, email, GitHub, LinkedIn, CV path, education, and professional experience. Empty fields hide the corresponding UI.
- `public/images/`: selected figures, lossless WebP derivatives, and a new review diagram.
- `public/data/motor-ablation.csv`: selected public numerical summary.

`public/cv/Fengyifei_XU_Resume.pdf` is the full resume linked from the site.

Do not copy research archives, briefs, private review manuscripts, original review SVGs, or student submissions into this directory. Resource buttons must point to real public files or URLs.

## Template provenance

Adapted directly from [Astro Scholar](https://github.com/shravanngoswamii/astro-scholar), commit `ea6e3c5b8823160b2ebc097a13a401d8d9354bbb` (v0.6.1). Its MIT LICENSE is retained. `package-lock.json` is the active lock.

Retained the Scholar palette, serif headings, local Atkinson fonts, path helper, and responsive contents-navigation behavior. Header/footer and the blog-derived project shell were simplified. Removed template blog, search, team, publications, dynamic image generation, analytics, and old deployment actions.

Compatible dependency fixes updated Astro within major 6 to 6.4.8. 

## Future GitHub Pages configuration

After owner review and approval, use **this directory as the repository root**. The workflow assumes package.json is at the repository root. Do not publish the parent directory.

Set repository variables `SITE_URL` to the approved origin and `BASE_PATH` to the actual repository prefix, or `/` for a user site/custom domain. No username or repository identity is assumed.

The included Pages workflow uses npm ci, the static build and checker, and official Pages artifact actions. It is **manual-only**; pushes do not deploy. It has not run on GitHub. Review dependency considerations in VERIFICATION.md before publication.

Subpath verification:

```powershell
$env:SITE_URL='https://portfolio-check.example'
$env:BASE_PATH='/engineering-portfolio'
npm run build
python scripts/check-site.py /engineering-portfolio https://portfolio-check.example
```

Clear temporary variables and rebuild before returning to a root-path preview. Local builds default to noindex and blocking robots; an explicit production origin enables indexing and sitemap generation. The 404 remains noindexed.

## Regenerating figures (optional)

`scripts/plot_ablation.py` uses matplotlib and reads the copied CSV. `node scripts/prepare-images.mjs` creates lossless WebP derivatives, dimensions, and a static sharing card. Generated assets are already included and these tools are not required by CI.
