import { unified } from '@astrojs/markdown-remark';
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
export default defineConfig({
  site: process.env.SITE_URL || 'http://localhost:4321',
  base: process.env.BASE_PATH || '/', output: 'static', trailingSlash: 'always',
  redirects: { '/projects/verilog-plagiarism/': (process.env.BASE_PATH || '/').replace(/\/$/, '') + '/projects/verilog-code-similarity/' },
  integrations: [mdx(), ...(process.env.SITE_URL ? [sitemap()] : [])],
  markdown: {
    shikiConfig: { themes: { light: 'github-light', dark: 'github-dark' } },
    processor: unified({ remarkPlugins: [remarkMath], rehypePlugins: [rehypeKatex] }),
  },
  devToolbar: { enabled: false },
});
