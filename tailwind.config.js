/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // search for templates or into templates
    "./**/templates/**/*.html", // search for apps level templates

  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

