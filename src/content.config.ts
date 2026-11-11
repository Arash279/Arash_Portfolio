import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';
const projects = defineCollection({
  loader: glob({ pattern: '**/*.mdx', base: './src/content/projects' }),
  schema: z.object({
    title: z.string(), shortTitle: z.string(), summary: z.string(), abstract: z.string(),
    status: z.string(), order: z.number().int(), category: z.string(), role: z.string(),
    thumbnail: z.string(), thumbnailAlt: z.string(), highlight: z.string(),
    tags: z.array(z.string()).max(3), takeaways: z.array(z.string()).min(2).max(3),
    period: z.string().optional(), supervisor: z.string().optional(),
    resourceLinks: z.array(z.object({ label: z.string(), href: z.string() })).default([]),
    toc: z.boolean().default(true),
  }),
});
export const collections = { projects };
