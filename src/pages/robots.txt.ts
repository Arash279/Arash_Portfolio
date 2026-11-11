import type { APIRoute } from 'astro';
export const GET: APIRoute = ({ site }) => {
  const published = !!import.meta.env.SITE_URL;
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  return new Response(published ? 'User-agent: *\nAllow: /\nSitemap: ' + new URL(base + '/sitemap-index.xml', site).href + '\n' : 'User-agent: *\nDisallow: /\n', { headers: { 'Content-Type': 'text/plain' } });
};
