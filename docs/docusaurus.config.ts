import type * as Preset from '@docusaurus/preset-classic';
import type { Config } from '@docusaurus/types';
import { themes as prismThemes } from 'prism-react-renderer';
import { katexConfig } from './src/math';

const config: Config = {
  title: 'macaron',
  tagline: "start with the best",
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://macaron.w4w.dev/',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'wyattowalsh', // Usually your GitHub org/user name.
  projectName: 'macaron', // Usually your repo name.

  onBrokenLinks: 'warn', // Change from 'throw' to 'warn'
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  plugins: [
    'docusaurus-plugin-sass',
    '@docusaurus/plugin-ideal-image',
  ],

  customFields: {},

  presets: [
    [
      'classic',
      {
        googleTagManager: {
          containerId: 'GTM-P9MQGWXJ',
        },

        docs: {
          sidebarPath: './sidebars.ts',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl:
          //   'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
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
        // blog: {
        //   showReadingTime: true,
        //   feedOptions: {
        //     type: ['rss', 'atom'],
        //     xslt: true,
        //   },
        //   // Please change this to your repo.
        //   // Remove this to remove the "edit this page" links.
        //   editUrl:
        //     'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        //   // Useful options to enforce blogging best practices
        //   onInlineTags: 'warn',
        //   onInlineAuthors: 'warn',
        //   onUntruncatedBlogPosts: 'warn',
        // },
        theme: {
          customCss: ['./src/css/custom.scss', './src/css/globals.css'],
        },
      } satisfies Preset.Options,
    ],
  ],

  stylesheets: katexConfig.stylesheets,
  scripts: katexConfig.scripts,

  themeConfig: {
    metadata: [
        { name: 'description', content: 'Macaron - Start with the best. Official documentation and guides.' },
        { name: 'keywords', content: 'macaron, documentation, guide, tutorial' },
        { property: 'og:title', content: 'macaron' },
        { property: 'og:description', content: 'Start with the best. Official documentation and guides.' },
        { property: 'og:image', content: 'https://macaron.w4w.dev/img/icon.webp' },
        { property: 'og:url', content: 'https://macaron.w4w.dev' },
        { name: 'twitter:card', content: 'summary_large_image' },
        { name: 'twitter:title', content: 'macaron' },
        { name: 'twitter:description', content: 'Start with the best. Official documentation and guides.' },
        { name: 'twitter:image', content: 'https://macaron.w4w.dev/img/icon.webp' },
      ],
    // Replace with your project's social card
    image: 'img/icon.png',
    navbar: {
      title: 'macaron',
      logo: {
        alt: 'macaron site navbar icon',
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
          href: 'https://github.com/wyattowalsh/macaron',
          position: 'right',
          className: 'navbar--github',
        },
      ],
    },
    footer: {
      logo: {
        alt: 'macaron site footer icon',
        src: 'img/icon.webp',
        href: 'https://macaron.w4w.dev',
        width: "60px",
        height: "60px",
      },
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              html: `
                  <a href="./docs"><span>Get Started 🏁</span></a></div>
                `,
            },
          ],
        },
        // {
        //   title: 'Community',
        //   items: [
        //     {
        //       label: 'Stack Overflow',
        //       href: 'https://stackoverflow.com/questions/tagged/docusaurus',
        //     },
        //     {
        //       label: 'Discord',
        //       href: 'https://discordapp.com/invite/docusaurus',
        //     },
        //     {
        //       label: 'Twitter',
        //       href: 'https://twitter.com/docusaurus',
        //     },
        //   ],
        // },
        {
          title: 'More',
          items: [
            // {
            //   label: 'Blog',
            //   to: '/blog',
            // },
            // {
            //   label: 'GitHub',
            //   href: 'https://github.com/wyattowalsh/macaron',
            // },
            {
              html: `
                  <a href="https://github.com/wyattowalsh/macaron" class="footer__link-item" style="display: inline-flex; align-items: center; gap: 8px; padding: 4px 8px; border-radius: 8px; background: rgba(255, 255, 255, 0.1); transition: all 0.3s ease;">
                    <img src="img/icons/github.svg" style="width: 24px; height: 24px; filter: brightness(0) invert(1);" alt="GitHub icon"/>
                    <span style="font-size: 1.1em;">GitHub</span>
                  </a>
                `,
            },
          ],
        },
      ],
      copyright: `
          <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; position: relative; z-index: 4;">
            <div style="margin: 4px 0; display: flex; align-items: center; gap: 8px; white-space: nowrap;">
              Copyright © ${new Date().getFullYear()} macaron,
              Built with Docusaurus
              <img src="img/icons/docusaurus.svg" style="width: clamp(20px, 2vw, 28px); height: clamp(20px, 2vw, 28px);"/>
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
