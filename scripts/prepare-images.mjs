import sharp from 'sharp';
import { readFile, writeFile } from 'node:fs/promises';
// Existing research figures retain their full content and original downloadable PNG.
const images = ['choke-spectra', 'choke-comparison', 'choke-placement', 'verilog-features', 'verilog-augmentation'];
for (const name of images) {
  await sharp(`public/images/${name}.png`).resize({ width: 1600, withoutEnlargement: true }).webp({ lossless: true }).toFile(`public/images/${name}.webp`);
}
const social = `<svg width="1200" height="630" xmlns="http://www.w3.org/2000/svg"><rect width="1200" height="630" fill="white"/><rect x="70" y="80" width="60" height="5" fill="#003366"/><text x="70" y="140" fill="#003366" font-family="Arial" font-size="22" letter-spacing="1">ELECTRICAL ENGINEER · POWER ELECTRONICS · MACHINES · EMC</text><g fill="#1a1a1a" font-family="Georgia"><text x="70" y="260" font-size="76">Fengyifei XU</text><text x="70" y="340" font-size="40">Fast, practical models</text><text x="70" y="392" font-size="40">for real electrical hardware.</text></g><path d="M70 460h1060" stroke="#dfe4e9"/><text x="70" y="515" font-family="Arial" font-size="26" fill="#555">NUS M.Sc. EE (Dec 2026) · Available in Singapore from Jan 2027</text><text x="70" y="560" font-family="Arial" font-size="24" fill="#003366">arash279.github.io/Arash_Portfolio</text></svg>`;
const portrait = await sharp('public/images/portrait.webp').resize(300, 300).composite([{ input: Buffer.from('<svg width="300" height="300"><circle cx="150" cy="150" r="150" fill="white"/></svg>'), blend: 'dest-in' }]).png().toBuffer();
await sharp(Buffer.from(social)).composite([{ input: portrait, left: 830, top: 110 }]).png().toFile('public/images/social-card.png');
const manifest = {};
for (const name of ['motor-fit.svg', 'motor-ablation.svg', 'model-selection.svg', ...images.flatMap(n => [n + '.png', n + '.webp'])]) {
  const m = await sharp('public/images/' + name).metadata();
  manifest['/images/' + name] = { width: m.width, height: m.height };
}
await writeFile('src/image-dimensions.json', JSON.stringify(manifest, null, 2) + '\n');
console.log('Prepared lossless web images, social card, and dimensions.');
