import sharp from 'sharp';
import { readFile, writeFile } from 'node:fs/promises';
// Existing research figures retain their full content and original downloadable PNG.
const images = ['choke-spectra', 'choke-comparison', 'choke-placement', 'verilog-features', 'verilog-augmentation'];
for (const name of images) {
  await sharp(`public/images/${name}.png`).resize({ width: 1600, withoutEnlargement: true }).webp({ lossless: true }).toFile(`public/images/${name}.webp`);
}
const social = `<svg width="1200" height="630" xmlns="http://www.w3.org/2000/svg"><rect width="1200" height="630" fill="white"/><rect x="70" y="80" width="60" height="5" fill="#003366"/><text x="70" y="150" fill="#003366" font-family="Arial" font-size="22">ELECTRICAL ENGINEERING &amp; APPLIED RESEARCH</text><g fill="#1a1a1a" font-family="Georgia" font-size="66"><text x="70" y="280">Models, methods,</text><text x="70" y="360">and evidence.</text></g><path d="M70 450h1060" stroke="#dfe4e9"/><text x="70" y="510" font-family="Arial" font-size="26" fill="#555">Electrical modeling · Scientific computing · Research insight</text></svg>`;
await sharp(Buffer.from(social)).png().toFile('public/images/social-card.png');
const manifest = {};
for (const name of ['motor-fit.svg', 'motor-ablation.svg', 'model-selection.svg', ...images.flatMap(n => [n + '.png', n + '.webp'])]) {
  const m = await sharp('public/images/' + name).metadata();
  manifest['/images/' + name] = { width: m.width, height: m.height };
}
await writeFile('src/image-dimensions.json', JSON.stringify(manifest, null, 2) + '\n');
console.log('Prepared lossless web images, social card, and dimensions.');
