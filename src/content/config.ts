import { z, defineCollection } from 'astro:content';

const filmCollection = defineCollection({
  type: 'data',
  schema: z.array(z.object({
    link: z.string(),
    title: z.string(),
    year: z.string(),
    // directorlist: z.array(z.string()),
    runtime: z.number(),
    // genrelist: z.array(z.string()),
    // castlist: z.record(z.string(), z.string()),
    tagline: z.string(),
    summary: z.string(),
    rating: z.number(),
  }))
});

export const collections = {
  'films': filmCollection,
};
