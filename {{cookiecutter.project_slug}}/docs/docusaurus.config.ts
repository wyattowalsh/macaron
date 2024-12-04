import type * as Preset from '@docusaurus/preset-classic';
import type { Config } from '@docusaurus/types';
import { themes as prismThemes } from 'prism-react-renderer';
import { katexConfig } from './src/math';

const config: Config = {
  title: "{{ cookiecutter.project_name }}",
  tagline: "{{ cookiecutter.project_description }}",
  favicon: 'img/favicon.ico',

  url: "{{ cookiecutter.project_url }}",
  baseUrl: '/',

  organizationName: '{{ cookiecutter.github }}',
  projectName: '{{ cookiecutter.project_slug }}',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  plugins: ['docusaurus-plugin-sass'],

  presets: [
    [
      'classic',
      {
        // googleTagManager: {
        //   // containerId: <ADD YOURS HERE>,
        // },
        docs: {
          sidebarPath: './sidebars.ts',
          remarkPlugins: [
            require('remark-gfm'),
            require('remark-math'),
            require('remark-toc'),
            require('remark-frontmatter'),
            require('remark-mdx-frontmatter'),
            require('remark-smartypants'),
            require('remark-code-blocks'),
            require('remark-code-frontmatter'),
            require('remark-code-import'),
            require('remark-code-titles'),
            require('remark-custom-header-id'),
            require('remark-definition-list'),
            require('remark-embed-images'),
            require('remark-extended-table'),
            require('remark-hint'),
            require('remark-mdx-math-enhanced'),
            require('remark-oembed'),
            require('remark-sources'),
            require('remark-github-blockquote-alert').remarkAlert,
          ],
          rehypePlugins: [
            require('rehype-katex'),
            require('rehype-slug'),
            [require('rehype-autolink-headings'), { behavior: 'append' }],
            [require('rehype-prism-plus'), { ignoreMissing: true, showLineNumbers: true }],
            require('rehype-citation'),
            require('rehype-color-chips'),
            require('rehype-infer-reading-time-meta'),
            require('rehype-semantic-blockquotes'),
          ],
        },
        theme: {
          customCss: ['./src/styles/custom.scss', './src/styles/globals.css'],
        },
      } satisfies Preset.Options,
    ],
  ],

  stylesheets: katexConfig.stylesheets,
  scripts: katexConfig.scripts,

  themeConfig: {
    metadata: [
      { name: 'description', content: '{{ cookiecutter.project_description }}' },
      { name: 'keywords', content: '{{ cookiecutter.project_slug }}, documentation, guide, tutorial' },
      { property: 'og:title', content: '{{ cookiecutter.project_name }}' },
      { property: 'og:description', content: '{{ cookiecutter.project_description }}' },
      { property: 'og:image', content: '{{ cookiecutter.project_url }}/img/icon.webp' },
      { property: 'og:url', content: '{{ cookiecutter.project_url }}' },
      { name: 'twitter:card', content: 'summary_large_image' },
      { name: 'twitter:title', content: '{{ cookiecutter.project_name }}' },
      { name: 'twitter:description', content: '{{ cookiecutter.project_description }}' },
      { name: 'twitter:image', content: '{{ cookiecutter.project_url }}/img/icon.webp' },
    ],
    image: 'img/icon.png',
    navbar: {
      title: '{{ cookiecutter.project_name }}',
      logo: {
        alt: '{{ cookiecutter.project_name }} site navbar icon',
        src: 'img/icon.webp',
        className: 'navbar--icon',
      },
      items: [
        {
          type: 'doc',
          position: 'left',
          docId: 'index',
          label: 'Docs',
        },
        {
          type: 'search',
          position: 'right',
          className: 'navbar--search',
        },
        {
          html: '<i class="fa-brands fa-github"></i>',
          href: '{{ cookiecutter.github_url }}',
          position: 'right',
          className: 'navbar--github',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Get Started 🏁',
              to: '/docs',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'GitHub',
              href: '{{ cookiecutter.github_url }}',
            },
          ],
        },
      ],
      copyright: `
          <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center;">
            <div style="margin: 4px 0; display: flex; align-items: center; gap: 8px; white-space: nowrap;">
              Copyright © ${new Date().getFullYear()} {{ cookiecutter.project_name }}
              <img src="img/icon.webp" style="width: clamp(16px, 3vw, 64px); height: auto;"/>
              Built with Docusaurus
              <img src="img/icons/docusaurus.svg" style="width: clamp(16px, 3vw, 64px); height: auto;"/>
            </div>
          </div>
        `,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
    themes: ["docusaurus-json-schema-plugin"],
  } satisfies Preset.ThemeConfig,
};

export default config;
