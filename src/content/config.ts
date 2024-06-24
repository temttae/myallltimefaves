import { z, defineCollection } from 'astro:content';

const filmCollection = defineCollection({
  type: 'data',
  schema: z.array(z.object({
    link: z.string(),
    title: z.string(),
    year: z.string(),
    directorlist: z.array(z.string()),
    runtime: z.number(),
    genrelist: z.array(z.string()),
    castlist: z.record(z.string(), z.string().nullish()),
    tagline: z.string(),
    summary: z.string(),
    rating: z.number(),
    ratingstars: z.string(),
    
    // add to json manually
    caption: z.string().optional(),
    quote: z.string().optional(),
    description: z.string().optional(),
    color: z.string().optional(),
  }))
});

export const collections = {
  'film': filmCollection,
};
