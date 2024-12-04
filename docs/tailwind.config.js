/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx,mdx}", "./docs/**/*.{md,mdx}"],
  theme: {
    extend: {
      colors: {
        'primary': {
          50: '#f3f1ff',
          100: '#ebe5ff',
          200: '#d9ceff',
          300: '#bea6ff',
          400: '#9f75ff',
          500: '#843dff',
          600: '#7916ff',
          700: '#6b04fd',
          800: '#5a03d5',
          900: '#4b05ad',
        },
        accent: {
          100: '#FFECEF',
          200: '#FFCCD2',
          300: '#FF99A3',
          400: '#FF6675',
          500: '#FF3347',
          600: '#DB0024',
          700: '#A8001B',
          800: '#750012',
          900: '#420009',
        },
      },
      fontFamily: {
        sans: ['"Poppins"', 'sans-serif'],
        display: ['"Playfair Display"', 'serif'],
      },
      animation: {
        'float': 'float 6s ease-in-out infinite',
        'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0.6, 1) infinite',
        'gradient-animation': 'GradientAnimation 15s ease infinite',
        'glow': 'glow 2s ease-in-out infinite alternate',
        'sparkle': 'sparkle 1.5s ease-in-out infinite',
        'wave': 'wave 3s ease-in-out infinite',
        'spin-slow': 'spin 20s linear infinite',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-20px)' },
        },
        GradientAnimation: {
          '0%': { 'background-position': '0% 50%' },
          '50%': { 'background-position': '100% 50%' },
          '100%': { 'background-position': '0% 50%' },
        },
        glow: {
          '0%': { filter: 'brightness(1) drop-shadow(0 0 0 rgba(132, 94, 247, 0))' },
          '100%': { filter: 'brightness(1.2) drop-shadow(0 0 10px rgba(132, 94, 247, 0.5))' },
        },
        sparkle: {
          '0%, 100%': { opacity: 1, transform: 'scale(1) rotate(0deg)' },
          '50%': { opacity: 0.5, transform: 'scale(1.2) rotate(180deg)' },
        },
        wave: {
          '0%, 100%': { transform: 'translateY(0) rotate(-2deg)' },
          '50%': { transform: 'translateY(-10px) rotate(2deg)' },
        },
        shimmer: {
          '0%': { opacity: 0.5 },
          '50%': { opacity: 1 },
          '100%': { opacity: 0.5 },
        },
      },
      backdropBlur: {
        xs: '2px',
      },
    },
  },
  plugins: [
    require('tailwindcss-animate'),
    require('@tailwindcss/aspect-ratio'),
    require('@tailwindcss/typography'),
  ],
};
