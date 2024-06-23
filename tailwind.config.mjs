/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
    colors: {
      'white': '#ffffff',
      'black': '#252525',
      'lightgrey': '#e8e7e6',
      'darkgrey': '#d9d9d9',
      'yellow': '#e0a800',
    },
    fontFamily: {
      sans: ['Proza Libre', 'sans-serif'],
      serif: ['Spectral', 'serif'],
    },
		extend: {},
	},
	plugins: [],
}
