1 | # Docusaurus 2 Website
2 | 
3 | ## Installation
4 | 
5 | 1. `yarn install` in the root of the repo (one level above this directory).
6 | 1. In this directory, do `yarn start`.
7 | 1. A browser window will open up, pointing to the docs.
8 | 


--------------------------------------------------------------------------------
/website/_dogfooding/README.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | test: 'some test front matter'
 3 | ---
 4 | 
 5 | # Docusaurus website dogfooding
 6 | 
 7 | This is where we test edge cases of Docusaurus by using fancy configs, ensuring they all don't fail during a real site build.
 8 | 
 9 | Eventually, we could move these tests later so another test site? Note there is value to keep seeing the live result of those tests.
10 | 
11 | Fancy things we can test for here:
12 | 
13 | - Plugin Multi-instance
14 | - Webpack configs
15 | - \_ prefix convention
16 | - Huge sidebars impact
17 | - Using folders with spaces on purpose
18 | - Importing MD docs that are out of content plugin folders as partials (such as this README file!)
19 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/_dogfooding/_asset-tests/4/docu.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/_dogfooding/_asset-tests/4/图片.png


--------------------------------------------------------------------------------
/website/_dogfooding/_asset-tests/badSyntax.css:
--------------------------------------------------------------------------------
1 | 
2 | 
3 | See https://github.com/facebook/docusaurus/issues/10460
4 | 
5 | Using bad JS syntax on purpose, this file shouldn't be processed and cause build errors, it should just be copied over.
6 | 
7 | import export with }{>< default switch
8 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_asset-tests/badSyntax.js:
--------------------------------------------------------------------------------
1 | 
2 | Using bad JS syntax on purpose, this file shouldn't be processed and cause build errors, it should just be copied over.
3 | 
4 | import export with }{>< default switch
5 | 
6 |   See https://github.com/facebook/docusaurus/issues/10460
7 | 
8 |     See https://github.com/facebook/docusaurus/pull/10658
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_asset-tests/dogfooding/javadoc/index.html:
--------------------------------------------------------------------------------
1 | <html>
2 |   <body>
3 |     static HTML file used for testing we should be able to link to it with a
4 |     markdown link see also https://github.com/facebook/docusaurus/issues/3309
5 |   </body>
6 | </html>
7 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/_dogfooding/_asset-tests/image with spaces.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/_dogfooding/_asset-tests/someFile.pdf


--------------------------------------------------------------------------------
/website/_dogfooding/_asset-tests/someFile.xyz:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/_dogfooding/_asset-tests/someFile.xyz


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/_dogfooding/_asset-tests/新控制器空间/图片.png


--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/2021-08-21-blog-post-toc-tests.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Blog TOC FrontMatter tests
 3 | authors:
 4 |   - slorber
 5 | toc_min_heading_level: 2
 6 | toc_max_heading_level: 4
 7 | tags: [paginated-tag]
 8 | ---
 9 | 
10 | {/* truncate */}
11 | 
12 | import Content from '@site/_dogfooding/_partials/toc-tests.mdx';
13 | 
14 | <Content />
15 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/2021-08-22-no-author.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | tags: [paginated-tag]
 3 | ---
 4 | 
 5 | # Hmmm!
 6 | 
 7 | This is a blog post from an anonymous author!
 8 | 
 9 | ```mdx-code-block
10 | import Partial from "./_partial.mdx"
11 | 
12 | <Partial />
13 | ```
14 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/2021-08-23-multiple-authors.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | authors:
 3 |   - slorber
 4 |   - name: Josh-Cena
 5 |     image_url: https://avatars.githubusercontent.com/u/55398995?v=4
 6 |     url: https://joshcena.com
 7 | tags:
 8 |   [
 9 |     blog,
10 |     docusaurus,
11 |     paginated-tag,
12 |     long,
13 |     long-long,
14 |     long-long-long,
15 |     long-long-long-long,
16 |     long-long-long-long-long,
17 |   ]
18 | ---
19 | 
20 | # Multiple authors
21 | 
22 | You can have multiple authors for one blog post!
23 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/2021-09-13-dup-title.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | tags: [paginated-tag]
 3 | authors:
 4 |   - name: Josh-Cena1
 5 |   - name: Josh-Cena2
 6 |     image_url: https://github.com/Josh-Cena.png
 7 |   - name: Josh-Cena3
 8 |     url: https://github.com/Josh-Cena
 9 |   - name: Josh-Cena4
10 |     email: sidechen2003@gmail.com
11 | ---
12 | 
13 | # Post with duplicate title
14 | 
15 | See https://github.com/facebook/docusaurus/issues/6059. This one and [2021-11-13-dup-title.md](./2021-11-13-dup-title.mdx) should both show up.
16 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/2021-10-07-blog-post-mdx-feed-tests.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Blog post MDX Feed tests
 3 | authors:
 4 |   - slorber
 5 | tags:
 6 |   [
 7 |     paginated-tag,
 8 |     blog,
 9 |     docusaurus,
10 |     long-long,
11 |     long-long-long,
12 |     long-long-long-long,
13 |   ]
14 | hide_reading_time: true
15 | ---
16 | 
17 | Some MDX tests, mostly to test how the RSS feed render those
18 | 
19 | {/* truncate */}
20 | 
21 | ## Imports
22 | 
23 | Here are some imports:
24 | 
25 | import Tabs from '@theme/Tabs';
26 | import TabItem from '@theme/TabItem';
27 | 
28 | ## Exports
29 | 
30 | Here are some exports:
31 | 
32 | export const someExport = 42;
33 | 
34 | ## Tabs test
35 | 
36 | Here are some tabs:
37 | 
38 | <Tabs>
39 |   <TabItem value="apple" label="Apple">
40 |     This is an apple 🍎
41 |   </TabItem>
42 |   <TabItem value="orange" label="Orange">
43 |     This is an orange 🍊
44 |   </TabItem>
45 | </Tabs>
46 | 
47 | Here are some tabs, inside `mdx-code-block`:
48 | 
49 | ```mdx-code-block
50 | <Tabs>
51 |   <TabItem value="apple" label="Apple">
52 |     This is an apple 🍎
53 |   </TabItem>
54 |   <TabItem value="orange" label="Orange">
55 |     This is an orange 🍊
56 |   </TabItem>
57 | </Tabs>
58 | ```
59 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/2021-10-08-blog-post-mdx-require-feed-tests.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Blog post MDX require Feed tests
 3 | authors:
 4 |   - slorber
 5 | tags:
 6 |   [
 7 |     paginated-tag,
 8 |     blog,
 9 |     docusaurus,
10 |     long-long,
11 |     long-long-long,
12 |     long-long-long-long,
13 |   ]
14 | ---
15 | 
16 | Some MDX tests, mostly to test how the RSS feed render those
17 | 
18 | {/* truncate */}
19 | 
20 | Test MDX with require calls
21 | 
22 | import useBaseUrl from '@docusaurus/useBaseUrl';
23 | 
24 | <img src={useBaseUrl('/img/docusaurus.png')} />
25 | 
26 | <img src={require('../../static/img/docusaurus.png').default} />
27 | 
28 | <img src={require('@site/static/img/docusaurus.png').default} />
29 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/2021-11-13-dup-title.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | tags: [paginated-tag]
3 | ---
4 | 
5 | # Post with duplicate title
6 | 
7 | I hope I'm still here
8 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/2022-01-21-dup-footnote.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Third post with footnote to test posts with same footnote reference.
 3 | ---
 4 | 
 5 | foo[^1]
 6 | 
 7 | bar[^2]
 8 | 
 9 | baz[^3]
10 | 
11 | [^1]: foo
12 | [^2]: bar
13 | [^3]: baz
14 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/2022-01-22-dup-footnote.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Second post with footnote to test posts with same footnote reference.
 3 | ---
 4 | 
 5 | foo[^1]
 6 | 
 7 | bar[^2]
 8 | 
 9 | baz[^3]
10 | 
11 | [^1]: foo
12 | [^2]: bar
13 | [^3]: baz
14 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/2022-04-20-dup-footnote.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: First post with footnote to test posts with same footnote reference.
 3 | ---
 4 | 
 5 | foo[^1]
 6 | 
 7 | bar[^2]
 8 | 
 9 | baz[^3]
10 | 
11 | [^1]: foo
12 | [^2]: bar
13 | [^3]: baz
14 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/2022-08-24-post-unlisted.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Unlisted blog post
 3 | unlisted: true
 4 | tags: [blog, visibility, unlisted]
 5 | slug: /unlisted-post
 6 | ---
 7 | 
 8 | This unlisted blog post should be "hidden" in production, but remain accessible.
 9 | 
10 | It is filtered from the sidebar, sitemap, SEO indexation...
11 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/2022-08-25-post-draft.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | title: Draft blog post
3 | draft: true
4 | tags: [blog, visibility, draft]
5 | slug: /draft-post
6 | ---
7 | 
8 | This draft blog post should not be accessible in production, only in dev!
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/2022-10-02-html-slug.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: A post with html slug
 3 | tags: [paginated-tag]
 4 | slug: /x/y/z.html
 5 | ---
 6 | 
 7 | # Hmmm!
 8 | 
 9 | This is a blog post with an html slug!
10 | 
11 | ```mdx-code-block
12 | import Partial from "./_partial.mdx"
13 | 
14 | <Partial />
15 | ```
16 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/2023-07-19-a.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: 'Test if href in feed resolved correctly'
 3 | ---
 4 | 
 5 | [absolute full url](https://github.com/facebook/docusaurus)
 6 | 
 7 | [absolute url with implicit domain name](/tests/blog/2023/07/19/b)
 8 | 
 9 | [relative url](2023-07-19-b.mdx)
10 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/2023-07-19-b.mdx:
--------------------------------------------------------------------------------
1 | # Test Relative Path
2 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/2023-08-05.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Ensure heading anchor slugs respect GitHub emoji behavior
 3 | date: 2023-08-05
 4 | sidebar_label: 'Ensure heading... (custom label)'
 5 | ---
 6 | 
 7 | ## :smiley: This is a friendly header
 8 | 
 9 | ## 😃 This is a friendly header (real smiley)
10 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/2024-07-03-dual-author.mdx:
--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/2024-07-03-single-author.mdx:
--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/_partial.mdx:
--------------------------------------------------------------------------------
1 | This is a blog partial
2 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/authors.yml:
--------------------------------------------------------------------------------
 1 | slorber:
 2 |   name: Sebastien Lorber
 3 |   title: Docusaurus maintainer
 4 |   url: https://sebastienlorber.com
 5 |   image_url: https://github.com/slorber.png
 6 |   page: true
 7 |   socials:
 8 |     x: sebastienlorber
 9 | 
10 | ozaki:
11 |   name: ozaki
12 |   page: {permalink: '/custom/ozaki/permalink'}
13 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/demo/2020-08-03-second-blog-intro.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Using twice the blog plugin
 3 | authors: [slorber]
 4 | tags: [paginated-tag, blog, docusaurus]
 5 | ---
 6 | 
 7 | Did you know you can use multiple instances of the same plugin?
 8 | 
 9 | {/* truncate */}
10 | 
11 | :::tip
12 | 
13 | Using twice the blog plugin permits you to create more than one blog on the same Docusaurus website!
14 | 
15 | :::
16 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_blog tests/tags.yml:
--------------------------------------------------------------------------------
 1 | paginated-tag:
 2 | blog:
 3 | docusaurus:
 4 | long:
 5 | long-long:
 6 | long-long-long:
 7 | long-long-long-long:
 8 | long-long-long-long-long:
 9 | visibility:
10 | unlisted:
11 | draft:
12 | new:
13 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/beginner's guide.mdx:
--------------------------------------------------------------------------------
1 | # Beginner's guide
2 | 
3 | [#9160](https://github.com/facebook/docusaurus/pull/9160)
4 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/doc-with-another-sidebar.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | displayed_sidebar: anotherSidebar
3 | ---
4 | 
5 | # Doc with another sidebar
6 | 
7 | My link appears in a sidebar, but I want to display another sidebar...
8 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/doc-with-last-update.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | last_update:
3 |   author: custom author
4 |   date: 1/1/2000
5 | ---
6 | 
7 | # Doc With Last Update Front Matter
8 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/doc-without-sidebar.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | displayed_sidebar: null
3 | ---
4 | 
5 | # Doc without sidebar
6 | 
7 | My link appears in a sidebar, but I don't want to display that...
8 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/dummy.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | slug: dummy.html
3 | ---
4 | 
5 | # Just a dummy page
6 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/folder with space/doc 1.mdx:
--------------------------------------------------------------------------------
1 | # Doc 1
2 | 
3 | Inside folder with space
4 | 
5 | [doc 2](./doc%202.mdx)
6 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/folder with space/doc 2.mdx:
--------------------------------------------------------------------------------
1 | # Doc 2
2 | 
3 | Inside folder with space
4 | 
5 | [doc 1](./doc%201.mdx)
6 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/index.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | slug: /
 3 | tags: [a, b, c]
 4 | unlisted: true # Makes the navbar link disappear in prod
 5 | id: index
 6 | sidebar_label: Docs tests # TODO why is this required?
 7 | ---
 8 | 
 9 | # Docs tests
10 | 
11 | This Docusaurus docs plugin instance is meant to test fancy edge-cases that regular unit tests don't really cover.
12 | 
13 | - [/tests/docs](/tests/docs)
14 | - [/tests/blog](/tests/blog)
15 | - [/tests/pages](/tests/pages)
16 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/more-test.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | tags: [a, e, some-tag]
3 | ---
4 | 
5 | # Another test page
6 | 
7 | [Test link](./folder%20with%20space/doc%201.mdx)
8 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/standalone.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | tags:
 3 |   - b
 4 |   - d
 5 | ---
 6 | 
 7 | # Standalone doc
 8 | 
 9 | This doc is not in any sidebar, on purpose, to measure the build size impact of the huge sidebar
10 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tags.yml:
--------------------------------------------------------------------------------
 1 | a:
 2 |   description: 'Description for tag a'
 3 | b:
 4 |   label: 'Label for tag b'
 5 | c:
 6 |   permalink: '/permalink-for-tag-c'
 7 | d:
 8 | e:
 9 |   label: 'Label for tag e'
10 |   description: 'Description for tag e'
11 |   permalink: '/permalink-for-tag-e'
12 | some-tag:
13 | visibility:
14 | draft:
15 | listed:
16 | unlisted:
17 | d-custom-permalink:
18 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/Case-Sentitive-Doc.mdx:
--------------------------------------------------------------------------------
1 | # Case-Sensitive doc
2 | 
3 | This doc has uppercase and lowercase chars in its filename, and thus in its path / slug.
4 | 
5 | It should still work fine if the doc is server from a lowercase/uppercase path.
6 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/another-draft.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | draft: true
3 | ---
4 | 
5 | # Another Draft
6 | 
7 | This page should only be visible in local development
8 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/ascii/folder/æøå.mdx:
--------------------------------------------------------------------------------
1 | Dogfood test for https://github.com/facebook/docusaurus/pull/8137
2 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/ascii/æøå/index.mdx:
--------------------------------------------------------------------------------
1 | Dogfood test for https://github.com/facebook/docusaurus/pull/8137
2 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/category-links/_category_.json:
--------------------------------------------------------------------------------
1 | {
2 |   "label": "Category Links",
3 |   "description": "Category Links - Custom Description",
4 |   "link": {
5 |     "type": "generated-index",
6 |     "slug": "/category-links-generated-index-slug"
7 |   }
8 | }
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/category-links/custom-index-convention/intro.mdx:
--------------------------------------------------------------------------------
1 | # Introduction
2 | 
3 | This file is called `intro.md`. Typically, it won't be selected by the convention; however, it is in this case, because we have used a custom one.
4 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/category-links/custom-index-convention/sample-doc.mdx:
--------------------------------------------------------------------------------
1 | # Sample doc
2 | 
3 | Lorem Ipsum
4 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/category-links/no-index-doc/_category_.json:
--------------------------------------------------------------------------------
1 | {
2 |   "link": null
3 | }
4 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/category-links/no-index-doc/index.mdx:
--------------------------------------------------------------------------------
1 | # Index
2 | 
3 | This file (`index.md`) is supposed to be a category index, but it isn't because we have set `link: null` in the `_category_.json`.
4 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/category-links/no-index-doc/sample-doc.mdx:
--------------------------------------------------------------------------------
1 | # Sample doc
2 | 
3 | Lorem Ipsum
4 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/category-links/no-subdoc/index.mdx:
--------------------------------------------------------------------------------
1 | # No sub-docs
2 | 
3 | The only doc of this category is the index page. It should show up as a regular doc link.
4 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/category-links/readme.mdx:
--------------------------------------------------------------------------------
1 | # Readme
2 | 
3 | This `readme.md` should not be used as the category index due to the `_category_.json` link
4 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/category-links/regular-category/sample-doc.mdx:
--------------------------------------------------------------------------------
1 | # Sample doc
2 | 
3 | Lorem Ipsum
4 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/category-links/with-category-name-doc/sample-doc.mdx:
--------------------------------------------------------------------------------
1 | # Sample doc
2 | 
3 | Lorem Ipsum
4 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/category-links/with-category-name-doc/with-category-name-doc.mdx:
--------------------------------------------------------------------------------
 1 | # Category with a doc of category's name
 2 | 
 3 | You should be able to click on the category and browse this `<categoryName>/<categoryName>.md` doc
 4 | 
 5 | ## Intro
 6 | 
 7 | Some intro text
 8 | 
 9 | :::tip
10 | 
11 | It is also possible to render the card items for that category thanks to MDX:
12 | 
13 | :::
14 | 
15 | ## Category content
16 | 
17 | ```mdx-code-block
18 | import DocCardList from '@theme/DocCardList';
19 | import {useCurrentSidebarCategory} from '@docusaurus/theme-common';
20 | 
21 | <DocCardList items={useCurrentSidebarCategory().items}/>
22 | ```
23 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/category-links/with-index-doc/index.mdx:
--------------------------------------------------------------------------------
1 | # Category with index.md doc
2 | 
3 | You should be able to click on the category and browse this `index.md` doc
4 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/category-links/with-index-doc/sample-doc.mdx:
--------------------------------------------------------------------------------
1 | # Sample doc
2 | 
3 | Lorem Ipsum
4 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/category-links/with-readme-doc/README.mdx:
--------------------------------------------------------------------------------
1 | # Category with readme.md doc
2 | 
3 | You should be able to click on the category and browse this `readme.md` doc
4 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/category-links/with-readme-doc/sample-doc.mdx:
--------------------------------------------------------------------------------
1 | # Sample doc
2 | 
3 | Lorem Ipsum
4 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/custom-props/_category_.json:
--------------------------------------------------------------------------------
1 | {
2 |   "label": "Custom Props"
3 | }
4 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/custom-props/doc-with-custom-props.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_custom_props:
 3 |   prop: custom
 4 |   number: 1
 5 |   boolean: true
 6 | ---
 7 | 
 8 | # Doc with Custom Props
 9 | 
10 | This doc has custom props.
11 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/custom-props/doc-without-custom-props.mdx:
--------------------------------------------------------------------------------
1 | # Doc Without Custom Props
2 | 
3 | This doc doesn't have custom props.
4 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/custom-props/index.mdx:
--------------------------------------------------------------------------------
 1 | # Custom Props
 2 | 
 3 | ```mdx-code-block
 4 | import {useCurrentSidebarCategory} from '@docusaurus/theme-common';
 5 | 
 6 | export const DocPropsList = ({items}) => (
 7 |   <table>
 8 |     <tr>
 9 |       <th>Doc Page</th>
10 |       <th>Custom Props</th>
11 |     </tr>
12 |     {items.map((item, index) => (
13 |       <tr key={index}>
14 |         <td>{item.label}</td>
15 |         <td>{JSON.stringify(item.customProps)}</td>
16 |       </tr>
17 |     ))}
18 |   </table>
19 | );
20 | 
21 | <DocPropsList items={useCurrentSidebarCategory().items}/>
22 | ```
23 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/img-tests.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | image: ./img/oss_logo.png
 3 | ---
 4 | 
 5 | # Image tests
 6 | 
 7 | import Image from '@theme/IdealImage';
 8 | 
 9 | import docusaurusImport from '@site/static/img/docusaurus.png';
10 | 
11 | export const docusaurusRequire = require('@site/static/img/docusaurus.png');
12 | 
13 | ![URL encoded image](./img/oss_logo%20%282%29.png)
14 | 
15 | ## Regular images
16 | 
17 | <img src={docusaurusImport} />
18 | 
19 | <img src={docusaurusRequire.default} />
20 | 
21 | ## Ideal images
22 | 
23 | <Image img={docusaurusImport} />
24 | 
25 | <Image img={docusaurusRequire} />
26 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/_dogfooding/_docs tests/tests/img/oss_logo (2).png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/_dogfooding/_docs tests/tests/img/oss_logo.png


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/import-bad-package.mdx:
--------------------------------------------------------------------------------
 1 | # Import Bad Package
 2 | 
 3 | We are importing MDX content from a file that is in a package that has a bad React version.
 4 | 
 5 | This is expected to work despite the bad version.
 6 | 
 7 | See https://github.com/facebook/docusaurus/issues/9027
 8 | 
 9 | ---
10 | 
11 | import Readme from '@site/../admin/test-bad-package/README.mdx';
12 | 
13 | <Readme />
14 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/links/broken-anchors-tests.mdx:
--------------------------------------------------------------------------------
 1 | # Broken Anchors tests
 2 | 
 3 | import Link from '@docusaurus/Link';
 4 | 
 5 | <Link id="test-link-anchor">#test-link-anchor</Link>
 6 | 
 7 | [Markdown link to above anchor](#test-link-anchor)
 8 | 
 9 | [Markdown link to above anchor](#)
10 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/links/target.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | slug: target-doc-slug
 3 | ---
 4 | 
 5 | # Target doc
 6 | 
 7 | This is just a doc meant to be linked to by other docs.
 8 | 
 9 | ## Target heading {#target-heading}
10 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/toc-partials/_first-level-partial.mdx:
--------------------------------------------------------------------------------
1 | import SecondLevelPartial from './_second-level-partial.mdx';
2 | 
3 | ## 1st level partial
4 | 
5 | I'm 1 level deep.
6 | 
7 | <SecondLevelPartial />
8 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/toc-partials/_partial.mdx:
--------------------------------------------------------------------------------
 1 | ## Partial
 2 | 
 3 | Partial intro
 4 | 
 5 | ### Partial Sub Heading 1
 6 | 
 7 | Partial Sub Heading 1 content
 8 | 
 9 | #### Partial Sub Sub Heading 1
10 | 
11 | Partial Sub Sub Heading 1 content
12 | 
13 | ### Partial Sub Heading 2
14 | 
15 | Partial Sub Heading 2 content
16 | 
17 | #### Partial Sub Sub Heading 2
18 | 
19 | Partial Sub Sub Heading 2 content
20 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/toc-partials/_second-level-partial.mdx:
--------------------------------------------------------------------------------
1 | ### 2nd level partial
2 | 
3 | I'm 2 levels deep.
4 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/toc-partials/index.mdx:
--------------------------------------------------------------------------------
 1 | import Partial from './_partial.mdx';
 2 | 
 3 | # TOC partial test
 4 | 
 5 | This page tests that MDX-imported content appears correctly in the table-of-contents
 6 | 
 7 | See also:
 8 | 
 9 | - https://github.com/facebook/docusaurus/issues/3915
10 | - https://github.com/facebook/docusaurus/pull/9684
11 | 
12 | ---
13 | 
14 | **The table of contents should include headings of this partial**:
15 | 
16 | <Partial />
17 | 
18 | ---
19 | 
20 | **We can import the same partial using a different name and it still works**:
21 | 
22 | import WeirdLocalName from './_partial.mdx';
23 | 
24 | <WeirdLocalName />
25 | 
26 | ---
27 | 
28 | **We can import a partial and not use it, the TOC remains unaffected**:
29 | 
30 | import UnusedPartial from './_partial.mdx';
31 | 
32 | ---
33 | 
34 | import FirstLevelPartial from './_first-level-partial.mdx';
35 | 
36 | **It also works for partials importing other partials**
37 | 
38 | <FirstLevelPartial />
39 | 
40 | ---
41 | 
42 | **And we can even use the same partial twice!**
43 | 
44 | **(although it's useless and not particularly recommended because headings will have the same ids)**
45 | 
46 | <FirstLevelPartial />
47 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/visibility/force-unlisted.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | unlisted: false
 3 | force_unlisted_parseFrontMatter_test: true
 4 | ---
 5 | 
 6 | # force_unlisted_parseFrontMatter_test
 7 | 
 8 | This doc is hidden despite `unlisted: false`
 9 | 
10 | We use `parseFrontMatter` to force it to true thanks to `force_unlisted_parseFrontMatter_test: true`
11 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/visibility/only-drafts/draft-subcategory/draft3.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | draft: true
3 | tags: [visibility, draft]
4 | ---
5 | 
6 | # Only Drafts - Draft 3
7 | 
8 | Doc with draft front matter
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/visibility/only-drafts/draft-subcategory/index.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | draft: true
 3 | tags: [visibility, draft]
 4 | ---
 5 | 
 6 | # Only Drafts - Subcategory index draft
 7 | 
 8 | Doc with draft front matter
 9 | 
10 | ```mdx-code-block
11 | import DocCardList from '@theme/DocCardList';
12 | 
13 | <DocCardList />
14 | ```
15 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/visibility/only-drafts/draft1.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | draft: true
3 | tags: [visibility, draft]
4 | ---
5 | 
6 | # Only Drafts - Draft 1
7 | 
8 | Doc with draft front matter
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/visibility/only-drafts/draft2.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | draft: true
3 | tags: [draft]
4 | ---
5 | 
6 | # Only Drafts - Draft 2
7 | 
8 | Doc with draft front matter
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/visibility/only-unlisteds/unlisted-subcategory/index.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | unlisted: true
 3 | tags: [visibility, unlisted]
 4 | ---
 5 | 
 6 | # Only Unlisteds - Subcategory index unlisted
 7 | 
 8 | Doc with unlisted front matter
 9 | 
10 | ```mdx-code-block
11 | import DocCardList from '@theme/DocCardList';
12 | 
13 | <DocCardList />
14 | ```
15 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/visibility/only-unlisteds/unlisted-subcategory/unlisted3.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | unlisted: true
3 | tags: [visibility, unlisted]
4 | ---
5 | 
6 | # Only Unlisteds - Unlisted 3
7 | 
8 | Doc with unlisted front matter
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/visibility/only-unlisteds/unlisted1.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | unlisted: true
3 | tags: [visibility, unlisted]
4 | ---
5 | 
6 | # Only Unlisteds - Unlisted 1
7 | 
8 | Doc with unlisted front matter
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/visibility/only-unlisteds/unlisted2.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | unlisted: true
3 | tags: [visibility, unlisted]
4 | ---
5 | 
6 | # Only Unlisteds - Unlisted 2
7 | 
8 | Doc with unlisted front matter
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/visibility/some-drafts/draft-subcategory/draft3.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | draft: true
3 | tags: [visibility, draft]
4 | ---
5 | 
6 | # Some Drafts - Draft 3
7 | 
8 | Doc with draft front matter
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/visibility/some-drafts/draft-subcategory/index.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | draft: true
 3 | tags: [visibility, draft]
 4 | ---
 5 | 
 6 | # Some Drafts - Subcategory index draft
 7 | 
 8 | Doc with draft front matter
 9 | 
10 | ```mdx-code-block
11 | import DocCardList from '@theme/DocCardList';
12 | 
13 | <DocCardList />
14 | ```
15 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/visibility/some-drafts/draft-subcategory/listed1.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | tags: [visibility, listed]
3 | ---
4 | 
5 | # Some Drafts - Listed 1
6 | 
7 | Regular doc
8 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/visibility/some-drafts/draft1.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | draft: true
3 | tags: [visibility, draft]
4 | ---
5 | 
6 | # Some Drafts - Draft 1
7 | 
8 | Doc with draft front matter
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/visibility/some-drafts/draft2.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | draft: true
3 | tags: [visibility, draft]
4 | ---
5 | 
6 | # Some Drafts - Draft 2
7 | 
8 | Doc with draft front matter
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/visibility/some-unlisteds/unlisted-subcategory/index.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | unlisted: true
 3 | tags: [visibility, unlisted]
 4 | ---
 5 | 
 6 | # Some Unlisteds - Subcategory index unlisted
 7 | 
 8 | Doc with unlisted front matter
 9 | 
10 | ```mdx-code-block
11 | import DocCardList from '@theme/DocCardList';
12 | 
13 | <DocCardList />
14 | ```
15 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/visibility/some-unlisteds/unlisted-subcategory/listed1.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | tags: [visibility, listed]
3 | ---
4 | 
5 | # Some Unlisteds - Listed 1
6 | 
7 | Regular doc
8 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/visibility/some-unlisteds/unlisted-subcategory/unlisted3.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | unlisted: true
3 | tags: [visibility, unlisted]
4 | ---
5 | 
6 | # Some Unlisteds - Unlisted 3
7 | 
8 | Doc with unlisted front matter
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/visibility/some-unlisteds/unlisted1.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | unlisted: true
3 | tags: [visibility, unlisted]
4 | ---
5 | 
6 | # Some Unlisteds - Unlisted 1
7 | 
8 | Doc with unlisted front matter
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/tests/visibility/some-unlisteds/unlisted2.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | unlisted: true
3 | tags: [visibility, unlisted]
4 | ---
5 | 
6 | # Some Unlisteds - Unlisted 2
7 | 
8 | Doc with unlisted front matter
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/toc/toc-2-2.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | toc_min_heading_level: 2
3 | toc_max_heading_level: 2
4 | ---
5 | 
6 | import Content from '@site/_dogfooding/_partials/toc-tests.mdx';
7 | 
8 | <Content />
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/toc/toc-2-3.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | toc_min_heading_level: 2
3 | toc_max_heading_level: 3
4 | ---
5 | 
6 | import Content from '@site/_dogfooding/_partials/toc-tests.mdx';
7 | 
8 | <Content />
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/toc/toc-2-4.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | toc_min_heading_level: 2
3 | toc_max_heading_level: 4
4 | ---
5 | 
6 | import Content from '@site/_dogfooding/_partials/toc-tests.mdx';
7 | 
8 | <Content />
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/toc/toc-2-5.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | toc_min_heading_level: 2
3 | toc_max_heading_level: 5
4 | ---
5 | 
6 | import Content from '@site/_dogfooding/_partials/toc-tests.mdx';
7 | 
8 | <Content />
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/toc/toc-3-5.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | toc_min_heading_level: 3
3 | toc_max_heading_level: 5
4 | ---
5 | 
6 | import Content from '@site/_dogfooding/_partials/toc-tests.mdx';
7 | 
8 | <Content />
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/toc/toc-3-_.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | toc_min_heading_level: 3
3 | # toc_max_heading_level:
4 | ---
5 | 
6 | import Content from '@site/_dogfooding/_partials/toc-tests.mdx';
7 | 
8 | <Content />
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/toc/toc-4-5.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | toc_min_heading_level: 4
3 | toc_max_heading_level: 5
4 | ---
5 | 
6 | import Content from '@site/_dogfooding/_partials/toc-tests.mdx';
7 | 
8 | <Content />
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/toc/toc-5-5.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | toc_min_heading_level: 5
3 | toc_max_heading_level: 5
4 | ---
5 | 
6 | import Content from '@site/_dogfooding/_partials/toc-tests.mdx';
7 | 
8 | <Content />
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/toc/toc-_-5.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | # toc_min_heading_level:
3 | toc_max_heading_level: 5
4 | ---
5 | 
6 | import Content from '@site/_dogfooding/_partials/toc-tests.mdx';
7 | 
8 | <Content />
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/toc/toc-_-_.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | # toc_min_heading_level:
3 | # toc_max_heading_level:
4 | ---
5 | 
6 | import Content from '@site/_dogfooding/_partials/toc-tests.mdx';
7 | 
8 | <Content />
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/toc/toc-test-bad.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | toc_min_heading_level: 2
 3 | toc_max_heading_level: 6
 4 | ---
 5 | 
 6 | Test the TOC behavior of a real-world MD doc with invalid headings
 7 | 
 8 | ---
 9 | 
10 | BAD HEADINGS:
11 | 
12 | ###### lvl 6
13 | 
14 | ##### lvl 5
15 | 
16 | #### lvl 4
17 | 
18 | ##### lvl 5
19 | 
20 | #### lvl 4
21 | 
22 | ### lvl 3
23 | 
24 | ## lvl 2
25 | 
26 | # lvl 1
27 | 
28 | ---
29 | 
30 | GOOD HEADINGS:
31 | 
32 | ## lvl 2
33 | 
34 | ### lvl 3
35 | 
36 | #### lvl 4
37 | 
38 | ##### lvl 5
39 | 
40 | ###### lvl 6
41 | 
42 | ## lvl 2
43 | 
44 | ### lvl 3
45 | 
46 | #### lvl 4
47 | 
48 | ##### lvl 5
49 | 
50 | ###### lvl 6
51 | 
52 | ---
53 | 
54 | INLINE:
55 | 
56 | ```mdx-code-block
57 | import BrowserWindow from '@site/src/components/BrowserWindow';
58 | 
59 | import TOCInline from '@theme/TOCInline';
60 | 
61 | <BrowserWindow>
62 | 
63 | <TOCInline toc={toc} minHeadingLevel={2} maxHeadingLevel={6} />
64 | 
65 | </BrowserWindow>
66 | ```
67 | 
68 | ---
69 | 
70 | COLLAPSIBLE:
71 | 
72 | ```mdx-code-block
73 | import TOCCollapsible from '@theme/TOCCollapsible';
74 | 
75 | <BrowserWindow>
76 | 
77 | <TOCCollapsible toc={toc} minHeadingLevel={2} maxHeadingLevel={6} />
78 | 
79 | </BrowserWindow>
80 | ```
81 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_docs tests/toc/toc-test-good.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | toc_min_heading_level: 2
 3 | toc_max_heading_level: 6
 4 | ---
 5 | 
 6 | Test the TOC behavior of a real-world MD doc with valid headings
 7 | 
 8 | ---
 9 | 
10 | ## lvl 2
11 | 
12 | ### lvl 3
13 | 
14 | #### lvl 4
15 | 
16 | ##### lvl 5
17 | 
18 | ###### lvl 6
19 | 
20 | ## lvl 2
21 | 
22 | ### lvl 3
23 | 
24 | #### lvl 4
25 | 
26 | ##### lvl 5
27 | 
28 | ###### lvl 6
29 | 
30 | ---
31 | 
32 | INLINE:
33 | 
34 | ```mdx-code-block
35 | import BrowserWindow from '@site/src/components/BrowserWindow';
36 | 
37 | import TOCInline from '@theme/TOCInline';
38 | 
39 | <BrowserWindow>
40 | 
41 | <TOCInline toc={toc} minHeadingLevel={2} maxHeadingLevel={6} />
42 | 
43 | </BrowserWindow>
44 | ```
45 | 
46 | ---
47 | 
48 | COLLAPSIBLE:
49 | 
50 | ```mdx-code-block
51 | import TOCCollapsible from '@theme/TOCCollapsible';
52 | 
53 | <BrowserWindow>
54 | 
55 | <TOCCollapsible toc={toc} minHeadingLevel={2} maxHeadingLevel={6} />
56 | 
57 | </BrowserWindow>
58 | ```
59 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_pages tests/_pagePartial.mdx:
--------------------------------------------------------------------------------
1 | ### Page partial content
2 | 
3 | This is text coming from a page partial
4 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_pages tests/_script.js:
--------------------------------------------------------------------------------
1 | /**
2 |  * Copyright (c) Facebook, Inc. and its affiliates.
3 |  *
4 |  * This source code is licensed under the MIT license found in the
5 |  * LICENSE file in the root directory of this source tree.
6 |  */
7 | 
8 | export default 1;
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_pages tests/data.json:
--------------------------------------------------------------------------------
1 | {
2 |   "hello": "world"
3 | }
4 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_pages tests/draft.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | draft: true
3 | ---
4 | 
5 | # Draft page
6 | 
7 | This draft page should not be accessible in prod
8 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_pages tests/head-metadata.mdx:
--------------------------------------------------------------------------------
 1 | ## Head Metadata tests
 2 | 
 3 | This page declares the following custom head metadata:
 4 | 
 5 | ```html
 6 | <head>
 7 |   <meta name="generator" value="custom generator name!" />
 8 |   <meta name="viewport" content="initial-scale=1, viewport-fit=cover" />
 9 |   <meta name="robots" content="noindex, nofollow, my-extra-directive" />
10 | </head>
11 | ```
12 | 
13 | <head>
14 |   <meta name="generator" value="custom generator name!" />
15 |   <meta name="viewport" content="initial-scale=1, viewport-fit=cover" />
16 |   <meta name="robots" content="noindex, nofollow, my-extra-directive" />
17 | </head>
18 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_pages tests/hydration-tests.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React from 'react';
 9 | import Link from '@docusaurus/Link';
10 | import Layout from '@theme/Layout';
11 | 
12 | // Repro for hydration issue https://github.com/facebook/docusaurus/issues/5617
13 | function BuggyText() {
14 |   return (
15 |     <span>
16 |       Built using the <Link to="https://www.electronjs.org/">Electron</Link> ,
17 |       based on <Link to="https://www.chromium.org/">Chromium</Link>, and written
18 |       using <Link to="https://www.typescriptlang.org/">TypeScript</Link> ,
19 |       Xplorer promises you an unprecedented experience.
20 |     </span>
21 |   );
22 | }
23 | 
24 | export default function Home(): JSX.Element {
25 |   return (
26 |     <Layout>
27 |       <BuggyText />
28 |     </Layout>
29 |   );
30 | }
31 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_pages tests/layout-no-children.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React from 'react';
 9 | import Layout from '@theme/Layout';
10 | 
11 | // See https://github.com/facebook/docusaurus/issues/6337#issuecomment-1012913647
12 | export default function LayoutNoChildren(): JSX.Element {
13 |   return <Layout />;
14 | }
15 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_pages tests/link-tests.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React, {useRef} from 'react';
 9 | import Link from '@docusaurus/Link';
10 | import Layout from '@theme/Layout';
11 | 
12 | export default function LinkTest(): JSX.Element {
13 |   const anchorRef = useRef<HTMLAnchorElement>(null);
14 |   return (
15 |     <Layout>
16 |       <main className="container margin-vert--xl">
17 |         <Link ref={anchorRef} to="/">
18 |           A little link
19 |         </Link>
20 |         <button
21 |           type="button"
22 |           onClick={() => {
23 |             anchorRef.current!.style.backgroundColor = 'red';
24 |           }}>
25 |           Change the link
26 |         </button>
27 |       </main>
28 |     </Layout>
29 |   );
30 | }
31 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/_dogfooding/_pages tests/local-image.png


--------------------------------------------------------------------------------
/website/_dogfooding/_pages tests/navbar-dropdown-tests.mdx:
--------------------------------------------------------------------------------
 1 | # navbar-dropdown-tests
 2 | 
 3 | <div id="navbar-dropdown-tests">
 4 | 
 5 | 1. Make sure that the theme switcher is placed immediately after the language switcher in the navbar.
 6 | 2. Press `Tab` several times to focus language switcher.
 7 | 3. Press `Enter` to open language switcher.
 8 | 4. Press `Tab` several times to exit language switcher.
 9 | 5. Check if the theme selection button is in focus immediately after the last item.
10 | 
11 | </div>
12 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_pages tests/page-toc-tests.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | toc_min_heading_level: 2
3 | toc_max_heading_level: 4
4 | ---
5 | 
6 | import Content from '@site/_dogfooding/_partials/toc-tests.mdx';
7 | 
8 | <Content />
9 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_pages tests/react-18/_components/heavyComponent.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React from 'react';
 9 | 
10 | export default function HeavyComponent(): JSX.Element {
11 |   return (
12 |     <div style={{border: 'solid', margin: 10, padding: 10}}>
13 |       <button type="button" onClick={() => alert('click')}>
14 |         HeavyComponent
15 |       </button>
16 |     </div>
17 |   );
18 | }
19 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_pages tests/seo.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: custom SEO title
 3 | description: custom SEO description
 4 | keywords: [custom, keywords]
 5 | image: ./local-image.png
 6 | ---
 7 | 
 8 | # SEO tests
 9 | 
10 | Using page SEO front matter:
11 | 
12 | ```yaml
13 | title: custom SEO title
14 | description: custom SEO description
15 | keywords: [custom, keywords]
16 | image: ./local-image.png
17 | ```
18 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_pages tests/svg/index.mdx:
--------------------------------------------------------------------------------
 1 | import Integrations from './integrations.svg';
 2 | import OpenSource from './open-source.svg';
 3 | import Mascot from './mascot.svg';
 4 | 
 5 | # Many inline SVGs
 6 | 
 7 | Have a bunch of SVGs, they're written to intentionally override each others styled when inlined on the same page.
 8 | 
 9 | <Integrations height="20rem" />
10 | <OpenSource height="20rem" />
11 | <Mascot height="20rem" />
12 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_pages tests/unlisted.mdx:
--------------------------------------------------------------------------------
1 | ---
2 | unlisted: true
3 | ---
4 | 
5 | # Unlisted page
6 | 
7 | This unlisted page should always be directly accessible, but hidden from search engines
8 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_pages tests/z-index-tests.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React from 'react';
 9 | import Layout from '@theme/Layout';
10 | 
11 | export default function zIndexTest(): JSX.Element {
12 |   return (
13 |     <Layout>
14 |       <p id="z-index-test">This should have a z-index of 100</p>
15 |     </Layout>
16 |   );
17 | }
18 | 


--------------------------------------------------------------------------------
/website/_dogfooding/_partials/toc-tests.mdx:
--------------------------------------------------------------------------------
 1 | # title
 2 | 
 3 | some text
 4 | 
 5 | ## section 1
 6 | 
 7 | some text
 8 | 
 9 | ### subsection 1-1
10 | 
11 | some text
12 | 
13 | #### subsection 1-1-1
14 | 
15 | some text
16 | 
17 | ##### subsection 1-1-1-1
18 | 
19 | some text
20 | 
21 | ###### subsection 1-1-1-1-1
22 | 
23 | some text
24 | 
25 | ###### subsection 1-1-1-1-2
26 | 
27 | some text
28 | 
29 | ##### subsection 1-1-1-2
30 | 
31 | some text
32 | 
33 | #### subsection 1-1-2
34 | 
35 | some text
36 | 
37 | ### subsection 1-2
38 | 
39 | some text
40 | 
41 | ### subsection 1-3
42 | 
43 | some text
44 | 
45 | ## section 2
46 | 
47 | some text
48 | 
49 | ### subsection 2-1
50 | 
51 | some text
52 | 
53 | ### subsection 2-1
54 | 
55 | some text
56 | 
57 | ## section 3
58 | 
59 | some text
60 | 
61 | ### subsection 3-1
62 | 
63 | some text
64 | 
65 | ### subsection 3-2
66 | 
67 | some text
68 | 


--------------------------------------------------------------------------------
/website/_dogfooding/clientModuleCSS.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | /* Used to test CSS insertion order */
 9 | .test-marker-site-client-module {
10 |   content: 'site-client-module';
11 | }
12 | 


--------------------------------------------------------------------------------
/website/_dogfooding/dogfooding.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | html {
 9 |   @media screen and (min-width: 1px) {
10 |     &.plugin-docs.plugin-id-docs-tests {
11 |       .red > a {
12 |         color: red;
13 |       }
14 | 
15 |       .navbar {
16 |         border-bottom: solid thin cyan;
17 |       }
18 |     }
19 | 
20 |     &.plugin-blog.plugin-id-blog-tests {
21 |       .navbar {
22 |         border-bottom: solid thin lime;
23 |       }
24 |     }
25 | 
26 |     &.plugin-pages.plugin-id-pages-tests {
27 |       .navbar {
28 |         border-bottom: solid thin yellow;
29 |       }
30 |     }
31 | 
32 |     &:has(#navbar-dropdown-tests) .navbar__item.dropdown ~ a {
33 |       display: none;
34 |     }
35 |   }
36 | }
37 | 
38 | #z-index-test {
39 |   z-index: 100;
40 | }
41 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2021/05-12-announcing-docusaurus-two-beta/img/favorites.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2021/05-12-announcing-docusaurus-two-beta/img/image.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2021/05-12-announcing-docusaurus-two-beta/img/image_cropped.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2021/05-12-announcing-docusaurus-two-beta/img/slorber.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2021/05-12-announcing-docusaurus-two-beta/img/social-card.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2021/05-12-announcing-docusaurus-two-beta/img/trend.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2021/11-21-algolia-docsearch-migration/img/crawler-overview.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2021/11-21-algolia-docsearch-migration/img/editor.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2021/11-21-algolia-docsearch-migration/img/favorites.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2021/11-21-algolia-docsearch-migration/img/index-analytics.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2021/11-21-algolia-docsearch-migration/img/index-overview.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2021/11-21-algolia-docsearch-migration/img/slorber.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2021/11-21-algolia-docsearch-migration/img/social-card.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2021/11-21-algolia-docsearch-migration/img/trend.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/01-24-docusaurus-2021-recap/img/courier.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/01-24-docusaurus-2021-recap/img/dyte-dark.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/01-24-docusaurus-2021-recap/img/dyte-light.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/01-24-docusaurus-2021-recap/img/ionic-dark.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/01-24-docusaurus-2021-recap/img/ionic-light.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/01-24-docusaurus-2021-recap/img/iota-dark.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/01-24-docusaurus-2021-recap/img/iota-light.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/01-24-docusaurus-2021-recap/img/npm-trend.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/01-24-docusaurus-2021-recap/img/rising-stars.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/01-24-docusaurus-2021-recap/img/star-history.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/01-24-docusaurus-2021-recap/img/thumbnail.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/npm-downloads.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/plugins/redocusaurus.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/plugins/search.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/plugins/shiki-twoslash.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/slash-plushies.jpg


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/social-card.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/star-history.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v1/babel.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v1/docusaurus.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v1/katex.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v1/prettier.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v1/react-native.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v2-theming/courier.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v2-theming/datagit.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v2-theming/dyte.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v2-theming/hasura.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v2-theming/ionic.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v2-theming/outerbounds.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v2-theming/quickwit.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v2-theming/react-native.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v2/figma.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v2/gulp.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v2/iota.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v2/lacework.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v2/react-navigation.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v2/sap-cloud.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v2/snapchat.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v2/solana.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v2/stackblitz.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v2/supabase.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/08-01-announcing-docusaurus-2.0/img/v2/tauri.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/09-01-docusaurus-2.1/img/doc-card-list.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2022/09-01-docusaurus-2.1/img/social-card.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2023/09-22-upgrading-frontend-dependencies-with-confidence-using-visual-regression-testing/img/argos-github-comment.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2023/09-22-upgrading-frontend-dependencies-with-confidence-using-visual-regression-testing/img/argos-github-status.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2023/09-22-upgrading-frontend-dependencies-with-confidence-using-visual-regression-testing/img/argos-react-native-regression.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2023/09-22-upgrading-frontend-dependencies-with-confidence-using-visual-regression-testing/img/docusaurus-argos-example-repo-screenshot.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2023/09-22-upgrading-frontend-dependencies-with-confidence-using-visual-regression-testing/img/social-card.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2023/09-29-preparing-your-site-for-docusaurus-v3/img/mdx-checker-output.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2023/09-29-preparing-your-site-for-docusaurus-v3/img/mdx2-playground-options.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/2023/09-29-preparing-your-site-for-docusaurus-v3/img/social-card.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/releases/2.2/img/social-card.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/releases/2.3/img/social-card.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/releases/2.4/img/navbar-error.jpg


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/releases/2.4/img/sidebar-item-description.jpg


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/releases/2.4/img/social-card.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/releases/3.0/img/social-card.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/releases/3.1/img/broken-anchor.jpg


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/releases/3.1/img/social-card.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/releases/3.2/img/social-card.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/releases/3.3/img/social-card.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/releases/3.4/img/hash.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/releases/3.4/img/social-card.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/releases/3.5/img/author-index.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/releases/3.5/img/author-page.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/releases/3.5/img/author-socials.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/releases/3.5/img/blog-feed-xslt.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/releases/3.5/img/blog-sidebar-years.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/releases/3.5/img/social-card.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/releases/3.6/img/rsdoctor.jpg


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/blog/releases/3.6/img/social-card.png


--------------------------------------------------------------------------------
/website/blog/tags.yml:
--------------------------------------------------------------------------------
 1 | blog:
 2 | release:
 3 |   description: "Blog posts about Docusaurus' new releases"
 4 | recap:
 5 |   description: "Blog posts about Docusaurus' year recaps"
 6 | birth:
 7 | endi:
 8 | tribute:
 9 | i18n:
10 | beta:
11 | search:
12 | maintenance:
13 | documentation:
14 | docusaurus:
15 | profilo:
16 | adoption:
17 | unlisted:
18 | new:
19 | 


--------------------------------------------------------------------------------
/website/community/3-contributing.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Contributing
 3 | hide_title: true
 4 | sidebar_label: Contributing
 5 | ---
 6 | 
 7 | ```mdx-code-block
 8 | import Contributing from "@site/../CONTRIBUTING.md"
 9 | 
10 | <Contributing />
11 | ```
12 | 


--------------------------------------------------------------------------------
/website/delayCrowdin.mjs:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | /*
 9 | We delay a bit the i18n staging deployment
10 | Because sometimes, prod + i18n-staging call this script at the exact same time
11 | And then both try to dl the translations at the same time, and then we have a
12 | 409 error. This delay makes sure prod starts to dl the translations in priority
13 | Used in conjunction with waitForCrowdin.js (which is not enough)
14 |  */
15 | 
16 | /**
17 |  * @param {number} ms
18 |  */
19 | async function delay(ms) {
20 |   return new Promise((resolve) => {
21 |     setTimeout(resolve, ms);
22 |   });
23 | }
24 | 
25 | if (
26 |   process.env.NETLIFY === 'true' &&
27 |   process.env.SITE_NAME === 'docusaurus-i18n-staging'
28 | ) {
29 |   console.log(
30 |     '[Crowdin] Delaying the docusaurus-i18n-staging deployment to avoid 409 errors',
31 |   );
32 |   await delay(30000);
33 | }
34 | 


--------------------------------------------------------------------------------
/website/docs/advanced/index.mdx:
--------------------------------------------------------------------------------
 1 | # Advanced Tutorials
 2 | 
 3 | This section is not going to be very structured, but we will cover the following topics:
 4 | 
 5 | ```mdx-code-block
 6 | import DocCardList from '@theme/DocCardList';
 7 | 
 8 | <DocCardList />
 9 | ```
10 | 
11 | We will assume that you have finished the guides, and know the basics like how to configure plugins, how to write React components, etc. These sections will have plugin authors and code contributors in mind, so we may occasionally refer to [plugin APIs](../api/plugin-methods/README.mdx) or other architecture details. Don't panic if you don't understand everything😉
12 | 


--------------------------------------------------------------------------------
/website/docs/api/misc/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Miscellaneous
2 | position: 4
3 | 


--------------------------------------------------------------------------------
/website/docs/api/misc/eslint-plugin/prefer-docusaurus-heading.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | slug: /api/misc/@docusaurus/eslint-plugin/prefer-docusaurus-heading
 3 | ---
 4 | 
 5 | # prefer-docusaurus-heading
 6 | 
 7 | Ensures that the `@theme/Heading` theme component provided by Docusaurus [`theme-classic`](../../themes/theme-classic.mdx) is used instead of `<hn>` tags for headings.
 8 | 
 9 | ## Rule Details {#details}
10 | 
11 | Examples of **incorrect** code for this rule:
12 | 
13 | ```html
14 | <h1>This is heading 1</h1>
15 | 
16 | <h2>This is heading 2</h2>
17 | 
18 | <h3>This is heading 3</h3>
19 | ```
20 | 
21 | Examples of **correct** code for this rule:
22 | 
23 | ```javascript
24 | import Heading from '@theme/Heading'
25 | 
26 | <Heading as='h1'>This is heading 1</Heading>
27 | 
28 | <Heading as='h2'>This is heading 2</Heading>
29 | 
30 | <Heading as='h3'>This is heading 3</Heading>
31 | ```
32 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/docs/api/misc/logger/demo.png


--------------------------------------------------------------------------------
/website/docs/api/plugin-methods/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Plugin method references
2 | position: 1
3 | 


--------------------------------------------------------------------------------
/website/docs/api/plugins/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Plugins
2 | position: 2
3 | link:
4 |   type: doc
5 |   id: api/plugins/plugins-overview # Dogfood using a "qualified id"
6 | 


--------------------------------------------------------------------------------
/website/docs/api/themes/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Themes
2 | position: 3
3 | link:
4 |   type: doc
5 |   id: themes-overview # Dogfood using a "local id"
6 | 


--------------------------------------------------------------------------------
/website/docs/api/themes/theme-live-codeblock.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 3
 3 | slug: /api/themes/@docusaurus/theme-live-codeblock
 4 | ---
 5 | 
 6 | # 📦 theme-live-codeblock
 7 | 
 8 | This theme provides a `@theme/CodeBlock` component that is powered by react-live. You can read more on [interactive code editor](../../guides/markdown-features/markdown-features-code-blocks.mdx#interactive-code-editor) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-live-codeblock
12 | ```
13 | 
14 | ### Configuration {#configuration}
15 | 
16 | ```js title="docusaurus.config.js"
17 | export default {
18 |   plugins: ['@docusaurus/theme-live-codeblock'],
19 |   themeConfig: {
20 |     liveCodeBlock: {
21 |       /**
22 |        * The position of the live playground, above or under the editor
23 |        * Possible values: "top" | "bottom"
24 |        */
25 |       playgroundPosition: 'bottom',
26 |     },
27 |   },
28 | };
29 | ```
30 | 


--------------------------------------------------------------------------------
/website/docs/api/themes/theme-mermaid.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 5
 3 | slug: /api/themes/@docusaurus/theme-mermaid
 4 | ---
 5 | 
 6 | # 📦 theme-mermaid
 7 | 
 8 | This theme provides a `@theme/Mermaid` component that is powered by [mermaid](https://mermaid-js.github.io/). You can read more on [diagrams](../../guides/markdown-features/markdown-features-diagrams.mdx) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-mermaid
12 | ```
13 | 
14 | ## Configuration {#configuration}
15 | 
16 | ```js title="docusaurus.config.js"
17 | export default {
18 |   themes: ['@docusaurus/theme-mermaid'],
19 |   // In order for Mermaid code blocks in Markdown to work,
20 |   // you also need to enable the Remark plugin with this option
21 |   markdown: {
22 |     mermaid: true,
23 |   },
24 | };
25 | ```
26 | 


--------------------------------------------------------------------------------
/website/docs/api/themes/theme-search-algolia.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 4
 3 | slug: /api/themes/@docusaurus/theme-search-algolia
 4 | ---
 5 | 
 6 | # 📦 theme-search-algolia
 7 | 
 8 | This theme provides a `@theme/SearchBar` component that integrates with Algolia DocSearch easily. Combined with `@docusaurus/theme-classic`, it provides a very easy search integration. You can read more on [search](../../search.mdx) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-search-algolia
12 | ```
13 | 
14 | This theme also adds search page available at `/search` (as swizzlable `SearchPage` component) path with OpenSearch support. You can change this default path via `themeConfig.algolia.searchPagePath`. Use `false` to disable search page.
15 | 
16 | :::tip
17 | 
18 | If you have installed `@docusaurus/preset-classic`, you don't need to install it as a dependency.
19 | 
20 | :::
21 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/docs/assets/docusaurus-asset-example-banner.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/docs/assets/docusaurus-asset-example.docx


--------------------------------------------------------------------------------
/website/docs/assets/docusaurus-asset-example.xyz:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/docs/assets/docusaurus-asset-example.xyz


--------------------------------------------------------------------------------
/website/docs/guides/markdown-features/_markdown-partial-example.mdx:
--------------------------------------------------------------------------------
1 | <span>Hello {props.name}</span>
2 | 
3 | This is text some content from `_markdown-partial-example.md`.
4 | 


--------------------------------------------------------------------------------
/website/docs/guides/markdown-features/markdown-features-react.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .wrappingBlock {
 9 |   width: 50%;
10 |   display: inline-block;
11 |   padding: 5px;
12 |   vertical-align: top;
13 | }
14 | 
15 | .wrappingBlock code[class^='codeBlockLines'] {
16 |   white-space: pre-wrap;
17 | }
18 | 


--------------------------------------------------------------------------------
/website/docs/guides/markdown-features/markdown-features-tabs-styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .red {
 9 |   color: red;
10 | }
11 | 
12 | .red[aria-selected='true'] {
13 |   border-bottom-color: red;
14 | }
15 | 
16 | .orange {
17 |   color: orange;
18 | }
19 | 
20 | .orange[aria-selected='true'] {
21 |   border-bottom-color: orange;
22 | }
23 | 
24 | .yellow {
25 |   color: yellow;
26 | }
27 | 
28 | .yellow[aria-selected='true'] {
29 |   border-bottom-color: yellow;
30 | }
31 | 


--------------------------------------------------------------------------------
/website/docs/playground.mdx:
--------------------------------------------------------------------------------
 1 | # Playground
 2 | 
 3 | Playgrounds allow you to run Docusaurus **in your browser, without installing anything**!
 4 | 
 5 | They are mostly useful for:
 6 | 
 7 | - Testing Docusaurus
 8 | - Reporting bugs
 9 | 
10 | Use [docusaurus.new](https://docusaurus.new) as an easy-to-remember shortcut.
11 | 
12 | Choose one of the available options below.
13 | 
14 | ```mdx-code-block
15 | import {PlaygroundCardsRow} from '@site/src/components/Playground';
16 | 
17 | <PlaygroundCardsRow />
18 | ```
19 | 
20 | :::tip
21 | 
22 | For convenience, we'll remember your choice next time you visit [docusaurus.new](https://docusaurus.new).
23 | 
24 | :::
25 | 


--------------------------------------------------------------------------------
/website/docusaurus.config.localized.d.json.ts:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | declare const docusaurusConfigLocalized: {
 9 |   [key: string]: {[key: string]: string};
10 | };
11 | 
12 | export default docusaurusConfigLocalized;
13 | 


--------------------------------------------------------------------------------
/website/docusaurus.config.localized.json:
--------------------------------------------------------------------------------
/website/netlify.toml:
--------------------------------------------------------------------------------
 1 | 
 2 | # Note: this file's config overrides the Netlify UI admin config
 3 | 
 4 | # /!\ due to using a monorepo it can be a bit messy to configure Netlify
 5 | # See also https://github.com/netlify/build/issues/2483
 6 | 
 7 | [build]
 8 |   command = "yarn --cwd .. build:packages && yarn build"
 9 |   publish = "website/build"
10 | 
11 | [build.environment]
12 |   NETLIFY_USE_YARN = "true"
13 |   YARN_VERSION = "1.22.19"
14 |   NODE_VERSION = "18"
15 |   NODE_OPTIONS = "--max_old_space_size=8192"
16 | 
17 | [context.production]
18 |   command = "yarn --cwd .. build:packages && yarn netlify:build:production"
19 | 
20 | [context.branch-deploy]
21 |   command = "yarn --cwd .. build:packages && yarn netlify:build:branchDeploy"
22 | 
23 | [context.deploy-preview]
24 |   command = "yarn --cwd .. build:packages && yarn netlify:build:deployPreview"
25 | 
26 | [[plugins]]
27 | package = "netlify-plugin-cache"
28 |   [plugins.inputs]
29 |   paths = [
30 |     "node_modules/.cache/webpack",
31 |   ]
32 | 


--------------------------------------------------------------------------------
/website/sidebarsCommunity.js:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | /** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
 9 | export default {
10 |   community: [
11 |     {
12 |       type: 'autogenerated',
13 |       dirName: '.',
14 |     },
15 |     {
16 |       type: 'link',
17 |       href: '/changelog',
18 |       label: 'Changelog',
19 |     },
20 |     {
21 |       type: 'link',
22 |       href: '/showcase',
23 |       label: 'Showcase',
24 |     },
25 |     {
26 |       type: 'link',
27 |       href: '/feature-requests',
28 |       label: 'Feature Requests',
29 |     },
30 |     {
31 |       type: 'link',
32 |       label: 'Chat with us on Discord',
33 |       href: 'https://discord.gg/docusaurus',
34 |     },
35 |   ],
36 | };
37 | 


--------------------------------------------------------------------------------
/website/src/components/APITable/styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .apiTable {
 9 |   font-size: small;
10 | }
11 | 
12 | .apiTable tbody tr {
13 |   transition: box-shadow 0.2s;
14 | }
15 | 
16 | .apiTable tbody tr:focus,
17 | .apiTable tbody tr:hover {
18 |   outline: none;
19 |   box-shadow: 0 0 7px 0 inset var(--ifm-color-warning);
20 |   cursor: pointer;
21 |   transition: box-shadow 0.2s;
22 | }
23 | 
24 | .apiTable code {
25 |   cursor: text;
26 | }
27 | 


--------------------------------------------------------------------------------
/website/src/components/BrowserWindow/IframeWindow.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React from 'react';
 9 | 
10 | import BrowserWindow from './index';
11 | 
12 | // Quick and dirty component, to improve later if needed
13 | export default function IframeWindow({url}: {url: string}): JSX.Element {
14 |   return (
15 |     <div style={{padding: 10}}>
16 |       <BrowserWindow
17 |         url={url}
18 |         style={{
19 |           minWidth: 'min(100%,45vw)',
20 |           width: 800,
21 |           maxWidth: '100%',
22 |           overflow: 'hidden',
23 |         }}
24 |         bodyStyle={{padding: 0}}>
25 |         <iframe
26 |           src={url}
27 |           title={url}
28 |           style={{display: 'block', width: '100%', height: 300}}
29 |         />
30 |       </BrowserWindow>
31 |     </div>
32 |   );
33 | }
34 | 


--------------------------------------------------------------------------------
/website/src/components/ColorGenerator/styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .color {
 9 |   border-radius: 0.5rem;
10 |   display: inline-block;
11 |   vertical-align: middle;
12 |   width: 2rem;
13 |   height: 2rem;
14 | }
15 | 
16 | .input {
17 |   border-color: var(--ifm-color-content-secondary);
18 |   border-radius: var(--ifm-global-radius);
19 |   border-style: solid;
20 |   border-width: var(--ifm-global-border-width);
21 |   font-size: var(--ifm-font-size-base);
22 |   padding: 0.5rem;
23 | }
24 | 
25 | .colorInput {
26 |   position: relative;
27 |   border-color: var(--ifm-color-content-secondary);
28 |   border-radius: var(--ifm-global-radius);
29 |   border-style: solid;
30 |   border-width: var(--ifm-global-border-width);
31 |   height: 2.25rem;
32 |   top: 7px;
33 | }
34 | 
35 | .colorTable {
36 |   font-size: small;
37 | }
38 | 


--------------------------------------------------------------------------------
/website/src/components/ErrorBoundaryTestButton/index.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React, {type ReactNode, useState} from 'react';
 9 | 
10 | export default function ErrorBoundaryTestButton({
11 |   children = 'Boom!',
12 |   message = 'Boom!\nSomething bad happened, but you can try again!',
13 |   cause,
14 | }: {
15 |   children?: ReactNode;
16 |   message?: string;
17 |   cause?: string;
18 | }): JSX.Element {
19 |   const [state, setState] = useState(false);
20 |   if (state) {
21 |     throw new Error(message, {
22 |       cause: cause ? new Error(cause) : undefined,
23 |     });
24 |   }
25 |   return (
26 |     <button
27 |       className="button button--danger"
28 |       type="button"
29 |       onClick={() => setState(true)}>
30 |       {children}
31 |     </button>
32 |   );
33 | }
34 | 


--------------------------------------------------------------------------------
/website/src/components/HackerNewsIcon.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React from 'react';
 9 | import Link from '@docusaurus/Link';
10 | 
11 | export default function HackerNewsIcon({
12 |   size = 54,
13 | }: {
14 |   size?: number;
15 | }): JSX.Element {
16 |   return (
17 |     <Link
18 |       to="https://news.ycombinator.com/item?id=32303052"
19 |       style={{display: 'block', width: size, height: size}}>
20 |       <svg
21 |         xmlns="http://www.w3.org/2000/svg"
22 |         viewBox="0 0 48 48"
23 |         width={size}
24 |         height={size}>
25 |         <path fill="#FF6D00" d="M42 42H6V6h36v36z" />
26 |         <path fill="#FFF" d="M8 8v32h32V8H8zm30 30H10V10h28v28z" />
27 |         <path
28 |           fill="#FFF"
29 |           d="M23 32h2v-6l5.5-10h-2.1L24 24.1 19.6 16h-2.1L23 26z"
30 |         />
31 |       </svg>
32 |     </Link>
33 |   );
34 | }
35 | 


--------------------------------------------------------------------------------
/website/src/components/Highlight.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React, {type ReactNode} from 'react';
 9 | 
10 | export default function Highlight({
11 |   children,
12 |   color,
13 | }: {
14 |   children: ReactNode;
15 |   color: string;
16 | }): JSX.Element {
17 |   return (
18 |     <span
19 |       style={{
20 |         backgroundColor: color,
21 |         borderRadius: '2px',
22 |         color: '#fff',
23 |         padding: '0.2rem',
24 |       }}>
25 |       {children}
26 |     </span>
27 |   );
28 | }
29 | 


--------------------------------------------------------------------------------
/website/src/components/NavbarItems/CustomDogfoodNavbarItem.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React from 'react';
 9 | import {useLocation} from '@docusaurus/router';
10 | 
11 | // used to dogfood custom navbar elements are possible
12 | // see https://github.com/facebook/docusaurus/issues/7227
13 | export default function CustomDogfoodNavbarItem(props: {
14 |   content: string;
15 |   mobile?: boolean;
16 | }): JSX.Element | null {
17 |   const {pathname} = useLocation();
18 |   const shouldRender = pathname === '/tests' || pathname.startsWith('/tests/');
19 |   if (!shouldRender) {
20 |     return null;
21 |   }
22 |   return (
23 |     <button
24 |       onClick={() => {
25 |         // eslint-disable-next-line no-alert
26 |         alert("I'm a custom navbar item type example");
27 |       }}
28 |       type="button">
29 |       {props.content}
30 |       {props.mobile ? ' (mobile)' : ''}
31 |     </button>
32 |   );
33 | }
34 | 


--------------------------------------------------------------------------------
/website/src/components/Svg/styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .svgIcon {
 9 |   user-select: none;
10 |   width: 1em;
11 |   height: 1em;
12 |   display: inline-block;
13 |   fill: currentColor;
14 |   flex-shrink: 0;
15 |   color: inherit;
16 | }
17 | 
18 | /* font-size */
19 | .small {
20 |   font-size: 1.25rem;
21 | }
22 | 
23 | .medium {
24 |   font-size: 1.5rem;
25 | }
26 | 
27 | .large {
28 |   font-size: 2.185rem;
29 | }
30 | 
31 | /* colors */
32 | .primary {
33 |   color: var(--ifm-color-primary);
34 | }
35 | 
36 | .secondary {
37 |   color: var(--ifm-color-secondary);
38 | }
39 | 
40 | .success {
41 |   color: var(--ifm-color-success);
42 | }
43 | 
44 | .error {
45 |   color: var(--ifm-color-error);
46 | }
47 | 
48 | .warning {
49 |   color: var(--ifm-color-warning);
50 | }
51 | 
52 | .inherit {
53 |   color: inherit;
54 | }
55 | 


--------------------------------------------------------------------------------
/website/src/components/Tweet/styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .tweet {
 9 |   font-size: 15px;
10 | }
11 | 
12 | .tweetMeta {
13 |   color: var(--ifm-color-emphasis-700);
14 | }
15 | 
16 | .tweetMeta strong {
17 |   color: var(--ifm-font-color-base);
18 | }
19 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/quotes/christopher-chedeau.jpg


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/quotes/hector-ramos.jpg


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/quotes/ricky-vetter.jpg


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/30-days-swa.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/404lab-wiki.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/7wate-wiki.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/CIPP.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/SeaORM.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/SeaQL-blog.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/Seaography.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/StarfishQL.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/agilets.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/aide_jeune.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/aispeaker.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/akara-blog.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/algolia.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/apache-apisix.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/apexfp.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/astronomer.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/attobot.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/avana-wallet.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/aventus.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/awe-framework.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/axioms.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/bandwidth.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/benthos.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/blinkshell.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/blogasaurus.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/blogmatheusbrunelli.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/botonic.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/boxyhq.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/brainboard.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/bruce-wiki.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/build-tracker.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/chaos-mesh.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/charles-ancheta.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/chatkitty.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/claritychallenge.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/clutch.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/codesweetly.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/codeyourfuture.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/comp-labs.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/componentkit.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/configcat.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/console-table.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/countrystatecity.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/create-react-app.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/cryptodevhub.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/daily-digest-covid-19-in-france.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/darklang.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/dart-code-metrics.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/datagit.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/devspace.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/difranca-technotes.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/digitalsupportservices.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/dimeschedulersdk.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/discordresources.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/divine-wsf.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/djamaile.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/docs-taro-zone.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/draftjs.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/drayman.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/dyte.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/easy-dates.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/easyjwt.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/easypanel.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/edulinks.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/eightshift-docs.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/enarx.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/eric.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/erxes.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/eta.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/evantay.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/evershop.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/fast.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/fbt.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/files-gallery.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/firecms.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/firelordjs.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/flagsmith.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/flarum.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/flatifycss.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/flexit.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/flipper.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/flux.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/foal.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/formatjs.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/froggit.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/fullstackchronicles.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/geekyweb.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/getorca.org-dark.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/ghostly.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/gladys-assistant.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/gotenberg.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/graphql-codegen.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/gtfs-to-html.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/gulp.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/haochen.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/hashnode.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/hasura.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/hcaptcha.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/hermes.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/home-assistant.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/httpin.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/iammassoud.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/icodex.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/idb.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/indent.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/intelagent.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/ionic.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/iota-wiki.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/jest.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/joelpo.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/johnnyreilly.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/juffalow.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/junjie.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/k3ai.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/kaustubhk24.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/khyron_realm.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/kosko.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/kotest.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/kube-green.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/kubevela.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/kuizuo.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/kwatch.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/labviewbook.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/leedom.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/leon.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/lerna.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/liqvid.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/livekit.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/lux-algo.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/mailgo.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/mapillaryjs.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/mediamachine.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/meli.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/memgraph.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/meoo.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/metalyoung.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/metro.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/mia-platform.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/mikro-orm.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/mintmetrics.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/mixcore.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/mojaglobal.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/molecule-home.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/motion-layout.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/nanos-world.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/netbootxyz.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/netdata.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/neutronjs.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/nextauthjs.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/nhost.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/nocalhost.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/node-serialport.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/nodify.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/novu-docs.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/orbitjs.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/ory.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/ossinsight.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/outerbounds.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/oxidizer.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/patrikmasiar.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/paubox.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/pcapplusplus.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/pcc-archive.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/pdfme.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/pearl-ui.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/peradaban.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/pglet.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/piano-analytics.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/pincman.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/pipeline-ui.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/plausible.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/pnpm.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/postgres-ai.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/power.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/pptxgenjs.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/prefs.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/prismatic.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/profilo.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/pyre.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/qa-board.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/quantcdn.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/quickwit.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/rainbond.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/raspisuite.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/react-chat-elements.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/react-complex-tree.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/react-leaflet.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/react-native-elements.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/react-native-ios-kit.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/react-native-reanimated.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/react-native-testing-library.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/react-navigation.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/react-redux.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/reactive-button.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/reactnative-aria.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/reactnative.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/reactnativeboilerplate.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/realtime-apps-workshop.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/red-gradient.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/reddit-image-fetcher.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/redis-developer.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/redux-cool.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/redux.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/refine.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/registry.stackql.io.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/relay.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/rematch.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/remirror.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/remotion.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/repeaterjs.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/replicad.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/resoto.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/rivalis.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/rnrh.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/rooks.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/rsocket.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/runiac.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/runlet.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/sado0823.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/saleor.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/sapcloudsdk.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/sapphire.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/sass-fairy.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/sciwp.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/sequence.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/seven-innovation-base.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/shabados.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/shotstack.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/sicope-model.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/signoz.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/single-spa.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/smart-docs.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/smartcookieweb.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/smashgg.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/social-embed.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/sodaforsparc.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/someengineering.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/spicetify.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/spotifyapi-net.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/sqlframes_docusaurus.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/stackql.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/stryker-mutator.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/stylable.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/svix.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/sweetcode.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/synergies.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/t-regx.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/talentbrick.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/tamalwebsite.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/tasit.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/tauri.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/techharvesting.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/testing-library.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/the-diff.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/tidb-community-book.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/tinaeldevresse.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/tooljet.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/tourmaline.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/tremor.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/trpgengine.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/tuist.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/uniforms.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/unleash.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/unmand.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/verdaccio.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/verida-developers.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/virtual-photography-kit.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/vital.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/vue-nodegui.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/warrant.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/wasp.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/webdriverio.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/webiny.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/whirlcodes.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/wisdom.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/woodpecker.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/yeecord.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/zowe.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/src/data/showcase/zxuqian.png


--------------------------------------------------------------------------------
/website/src/pages/examples/_myComponent.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React, {useState} from 'react';
 9 | 
10 | export default function MyComponent() {
11 |   const [bool, setBool] = useState(false);
12 |   return (
13 |     <div>
14 |       <p>MyComponent rendered !</p>
15 |       <p>bool={bool ? 'true' : 'false'}</p>
16 |       <p>
17 |         <button onClick={() => setBool((b) => !b)}>toggle bool</button>
18 |       </p>
19 |     </div>
20 |   );
21 | }
22 | 


--------------------------------------------------------------------------------
/website/src/pages/examples/markdownPageExample.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: Markdown Page example
 3 | description: Markdown Page example
 4 | wrapperClassName: docusaurus-markdown-example
 5 | ---
 6 | 
 7 | # Markdown page
 8 | 
 9 | This is a page generated from markdown to illustrate the Markdown page feature.
10 | 
11 | :::tip
12 | 
13 | Use Markdown pages when you just want to focus on content and the default layout is good enough
14 | 
15 | :::
16 | 


--------------------------------------------------------------------------------
/website/src/pages/examples/noIndex.mdx:
--------------------------------------------------------------------------------
 1 | # No Index Page example
 2 | 
 3 | <head>
 4 |   <meta name="robots" content="nOiNdeX, NoFolLoW" />
 5 | </head>
 6 | 
 7 | This page will not be indexed by search engines because it contains the page following [page metadata](/docs/seo#single-page-metadata) markup:
 8 | 
 9 | ```html
10 | <head>
11 |   <meta name="robots" content="noindex, nofollow" />
12 | </head>
13 | ```
14 | 
15 | :::tip
16 | 
17 | The sitemap plugin filters pages containing a `noindex` content value. This page doesn't appear in Docusaurus [sitemap.xml](pathname:///sitemap.xml) file.
18 | 
19 | :::
20 | 
21 | :::note
22 | 
23 | Robots directives are [case-insensitive](https://developers.google.com/search/docs/advanced/robots/robots_meta_tag#directives).
24 | 
25 | :::
26 | 


--------------------------------------------------------------------------------
/website/src/pages/showcase/_components/ClearAllButton/index.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React, {type ReactNode} from 'react';
 9 | import {useClearQueryString} from '@docusaurus/theme-common';
10 | 
11 | export default function ClearAllButton(): ReactNode {
12 |   const clearQueryString = useClearQueryString();
13 |   // TODO translate
14 |   return (
15 |     <button
16 |       className="button button--outline button--primary"
17 |       type="button"
18 |       onClick={() => clearQueryString()}>
19 |       Clear All
20 |     </button>
21 |   );
22 | }
23 | 


--------------------------------------------------------------------------------
/website/src/pages/showcase/_components/FavoriteIcon/index.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React, {type ComponentProps} from 'react';
 9 | import clsx from 'clsx';
10 | 
11 | import styles from './styles.module.css';
12 | 
13 | interface Props {
14 |   className?: string;
15 |   style?: ComponentProps<'svg'>['style'];
16 |   size: 'small' | 'medium' | 'large';
17 | }
18 | 
19 | export default function FavoriteIcon({
20 |   size,
21 |   className,
22 |   style,
23 | }: Props): React.ReactNode {
24 |   return (
25 |     <svg
26 |       viewBox="0 0 24 24"
27 |       className={clsx(styles.svg, styles[size], className)}
28 |       style={style}>
29 |       <path d="M12,21.35L10.55,20.03C5.4,15.36 2,12.27 2,8.5C2,5.41 4.42,3 7.5,3C9.24,3 10.91,3.81 12,5.08C13.09,3.81 14.76,3 16.5,3C19.58,3 22,5.41 22,8.5C22,12.27 18.6,15.36 13.45,20.03L12,21.35Z" />
30 |     </svg>
31 |   );
32 | }
33 | 


--------------------------------------------------------------------------------
/website/src/pages/showcase/_components/FavoriteIcon/styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .svg {
 9 |   user-select: none;
10 |   color: #e9669e;
11 |   width: 1em;
12 |   height: 1em;
13 |   display: inline-block;
14 |   fill: currentColor;
15 | }
16 | 
17 | .small {
18 |   font-size: 1rem;
19 | }
20 | 
21 | .medium {
22 |   font-size: 1.25rem;
23 | }
24 | 
25 | .large {
26 |   font-size: 1.8rem;
27 | }
28 | 


--------------------------------------------------------------------------------
/website/src/pages/showcase/_components/ShowcaseCards/styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .cardList {
 9 |   display: grid;
10 |   grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
11 |   gap: 24px;
12 | }
13 | 
14 | .showcaseFavorite {
15 |   padding-top: 2rem;
16 |   padding-bottom: 2rem;
17 |   background-color: #f6fdfd;
18 | }
19 | 
20 | html[data-theme='dark'] .showcaseFavorite {
21 |   background-color: #232525;
22 | }
23 | 
24 | .headingFavorites {
25 |   display: flex;
26 |   align-items: center;
27 | }
28 | 


--------------------------------------------------------------------------------
/website/src/pages/showcase/_components/ShowcaseFilters/styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .headingRow {
 9 |   display: flex;
10 |   align-items: center;
11 |   justify-content: space-between;
12 | }
13 | 
14 | .headingText {
15 |   display: flex;
16 |   align-items: baseline;
17 | }
18 | 
19 | .headingText > h2 {
20 |   margin-bottom: 0;
21 | }
22 | 
23 | .headingText > span {
24 |   margin-left: 8px;
25 | }
26 | 
27 | .headingButtons {
28 |   display: flex;
29 |   align-items: center;
30 | }
31 | 
32 | .headingButtons > * {
33 |   margin-left: 8px;
34 | }
35 | 
36 | .tagList {
37 |   display: flex;
38 |   align-items: center;
39 |   flex-wrap: wrap;
40 | }
41 | 
42 | .tagListItem {
43 |   user-select: none;
44 |   white-space: nowrap;
45 |   height: 32px;
46 |   font-size: 0.8rem;
47 |   margin-top: 0.5rem;
48 |   margin-right: 0.5rem;
49 | }
50 | 
51 | .tagListItem:last-child {
52 |   margin-right: 0;
53 | }
54 | 


--------------------------------------------------------------------------------
/website/src/pages/showcase/_components/ShowcaseSearchBar/index.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import {type ReactNode} from 'react';
 9 | import {translate} from '@docusaurus/Translate';
10 | import {useSearchName} from '@site/src/pages/showcase/_utils';
11 | import styles from './styles.module.css';
12 | 
13 | export default function ShowcaseSearchBar(): ReactNode {
14 |   const [searchName, setSearchName] = useSearchName();
15 |   return (
16 |     <div className={styles.searchBar}>
17 |       <input
18 |         placeholder={translate({
19 |           message: 'Search for site name...',
20 |           id: 'showcase.searchBar.placeholder',
21 |         })}
22 |         value={searchName}
23 |         onInput={(e) => {
24 |           setSearchName(e.currentTarget.value);
25 |         }}
26 |       />
27 |     </div>
28 |   );
29 | }
30 | 


--------------------------------------------------------------------------------
/website/src/pages/showcase/_components/ShowcaseSearchBar/styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .searchBar {
 9 |   margin-left: auto;
10 | }
11 | 
12 | .searchBar input {
13 |   height: 30px;
14 |   border-radius: 15px;
15 |   padding: 10px;
16 |   border: 1px solid gray;
17 | }
18 | 


--------------------------------------------------------------------------------
/website/src/pages/tests.mdx:
--------------------------------------------------------------------------------
1 | # Tests
2 | 
3 | Docusaurus use some extra plugin instances for testing / dogfooding purpose:
4 | 
5 | - [/tests/docs](/tests/docs)
6 | - [/tests/blog](/tests/blog)
7 | - [/tests/pages](/tests/pages)
8 | 


--------------------------------------------------------------------------------
/website/src/plugins/changelog/theme/ChangelogItem/Header/Author/styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .image {
 9 |   width: 100%;
10 |   height: 100%;
11 |   object-fit: cover;
12 | }
13 | 


--------------------------------------------------------------------------------
/website/src/plugins/changelog/theme/ChangelogItem/Header/Authors/styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .authorCol {
 9 |   max-width: inherit !important;
10 |   flex-grow: 1 !important;
11 | }
12 | 
13 | .imageOnlyAuthorRow {
14 |   display: flex;
15 |   flex-flow: row wrap;
16 | }
17 | 
18 | .imageOnlyAuthorCol {
19 |   margin-left: 0.3rem;
20 |   margin-right: 0.3rem;
21 | }
22 | 
23 | .imageOnlyAuthorCol [class^='image'] {
24 |   background-color: var(--ifm-color-emphasis-100);
25 | }
26 | 
27 | .toggleButton {
28 |   margin-left: 0.3rem;
29 |   margin-right: 0.3rem;
30 |   border-radius: 50%;
31 |   width: var(--ifm-avatar-photo-size);
32 |   height: var(--ifm-avatar-photo-size);
33 |   background-color: var(--ifm-color-emphasis-100);
34 | }
35 | 
36 | .toggleButtonIconExpanded {
37 |   transform: rotate(180deg);
38 | }
39 | 


--------------------------------------------------------------------------------
/website/src/plugins/changelog/theme/ChangelogItem/Header/index.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React from 'react';
 9 | import {useBlogPost} from '@docusaurus/plugin-content-blog/client';
10 | 
11 | import BlogPostItemHeaderTitle from '@theme/BlogPostItem/Header/Title';
12 | import BlogPostItemHeaderInfo from '@theme/BlogPostItem/Header/Info';
13 | import ChangelogItemHeaderAuthors from '@theme/ChangelogItem/Header/Authors';
14 | 
15 | import styles from './styles.module.css';
16 | 
17 | // Reduce changelog title size, but only on list view
18 | function ChangelogTitle() {
19 |   const {isBlogPostPage} = useBlogPost();
20 |   return (
21 |     <BlogPostItemHeaderTitle
22 |       className={isBlogPostPage ? undefined : styles.changelogItemTitleList}
23 |     />
24 |   );
25 | }
26 | 
27 | export default function ChangelogItemHeader(): JSX.Element {
28 |   return (
29 |     <header>
30 |       <ChangelogTitle />
31 |       <BlogPostItemHeaderInfo />
32 |       <ChangelogItemHeaderAuthors />
33 |     </header>
34 |   );
35 | }
36 | 


--------------------------------------------------------------------------------
/website/src/plugins/changelog/theme/ChangelogItem/Header/styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .changelogItemTitleList {
 9 |   font-size: 2rem;
10 | }
11 | 


--------------------------------------------------------------------------------
/website/src/plugins/changelog/theme/ChangelogItem/index.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React from 'react';
 9 | import ChangelogItemHeader from '@theme/ChangelogItem/Header';
10 | import type {Props} from '@theme/BlogPostItem';
11 | import BlogPostItemContainer from '@theme/BlogPostItem/Container';
12 | import BlogPostItemContent from '@theme/BlogPostItem/Content';
13 | 
14 | import styles from './styles.module.css';
15 | 
16 | export default function ChangelogItem({children}: Props): JSX.Element {
17 |   return (
18 |     <BlogPostItemContainer className={styles.changelogItemContainer}>
19 |       <ChangelogItemHeader />
20 |       <BlogPostItemContent>{children}</BlogPostItemContent>
21 |     </BlogPostItemContainer>
22 |   );
23 | }
24 | 


--------------------------------------------------------------------------------
/website/src/plugins/changelog/theme/ChangelogItem/styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .changelogItemContainer {
 9 |   margin-bottom: 1rem;
10 | }
11 | 


--------------------------------------------------------------------------------
/website/src/plugins/changelog/theme/ChangelogList/Header/styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .rss,
 9 | .rss:hover {
10 |   color: #f26522;
11 | }
12 | 
13 | .x,
14 | .x:hover {
15 |   color: #1da1f2;
16 | }
17 | 


--------------------------------------------------------------------------------
/website/src/plugins/changelog/theme/types.d.ts:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | declare module '@theme/ChangelogPaginator';
 9 | 
10 | declare module '@theme/ChangelogItem';
11 | declare module '@theme/ChangelogItem/Header';
12 | declare module '@theme/ChangelogItem/Header/Author';
13 | declare module '@theme/ChangelogItem/Header/Authors';
14 | 
15 | declare module '@theme/ChangelogList';
16 | declare module '@theme/ChangelogList/Header';
17 | 
18 | declare module '@theme/Icon/Expand' {
19 |   import type {ComponentProps} from 'react';
20 | 
21 |   export interface Props extends ComponentProps<'svg'> {
22 |     expanded?: boolean;
23 |   }
24 | 
25 |   export default function IconExpand(props: Props): JSX.Element;
26 | }
27 | 


--------------------------------------------------------------------------------
/website/src/plugins/featureRequests/cannyScript.js:
--------------------------------------------------------------------------------
 1 | // Provided by Canny.
 2 | /* eslint-disable */
 3 | 
 4 | function cannyScript() {
 5 |   !(function (w, d, i, s) {
 6 |     function l() {
 7 |       if (!d.getElementById(i)) {
 8 |         let f = d.getElementsByTagName(s)[0],
 9 |           e = d.createElement(s);
10 |         (e.type = 'text/javascript'),
11 |           (e.async = !0),
12 |           (e.src = 'https://canny.io/sdk.js'),
13 |           f.parentNode.insertBefore(e, f);
14 |       }
15 |     }
16 |     if (typeof w.Canny !== 'function') {
17 |       var c = function () {
18 |         c.q.push(arguments);
19 |       };
20 |       (c.q = []),
21 |         (w.Canny = c),
22 |         d.readyState === 'complete'
23 |           ? l()
24 |           : w.attachEvent
25 |           ? w.attachEvent('onload', l)
26 |           : w.addEventListener('load', l, !1);
27 |     }
28 |   })(window, document, 'canny-jssdk', 'script');
29 | }
30 | 
31 | export default cannyScript;
32 | 


--------------------------------------------------------------------------------
/website/src/plugins/featureRequests/styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .main {
 9 |   padding: var(--ifm-spacing-horizontal);
10 |   border-radius: 4px;
11 |   background: var(--site-color-feedback-background);
12 |   min-height: 500px;
13 | }
14 | 


--------------------------------------------------------------------------------
/website/src/sw.js:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import {registerRoute} from 'workbox-routing';
 9 | import {StaleWhileRevalidate} from 'workbox-strategies';
10 | 
11 | export default function swCustom(params) {
12 |   if (params.debug) {
13 |     console.log('[Docusaurus-PWA][SW]: running swCustom code', params);
14 |   }
15 | 
16 |   // Cache responses from external resources
17 |   registerRoute(
18 |     (context) =>
19 |       [
20 |         /graph\.facebook\.com\/.*\/picture/,
21 |         /netlify\.com\/img/,
22 |         /avatars1\.githubusercontent/,
23 |       ].some((regex) => context.url.href.match(regex)),
24 |     new StaleWhileRevalidate(),
25 |   );
26 | }
27 | 


--------------------------------------------------------------------------------
/website/src/theme/Admonition/Types.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React from 'react';
 9 | import type {Props} from '@theme/Admonition';
10 | import DefaultAdmonitionTypes from '@theme-original/Admonition/Types';
11 | import Heading from '@theme/Heading';
12 | 
13 | function MyCustomAdmonition(props: Props): JSX.Element {
14 |   return (
15 |     <div style={{border: 'solid red', padding: 10}}>
16 |       <Heading as="h5" style={{color: 'blue', fontSize: 30}}>
17 |         {props.title}
18 |       </Heading>
19 |       <div>{props.children}</div>
20 |     </div>
21 |   );
22 | }
23 | 
24 | const AdmonitionTypes = {
25 |   ...DefaultAdmonitionTypes,
26 | 
27 |   // Add all your custom admonition types here...
28 |   // you can also override the default ones
29 |   'my-custom-admonition': MyCustomAdmonition,
30 | };
31 | 
32 | export default AdmonitionTypes;
33 | 


--------------------------------------------------------------------------------
/website/src/theme/CodeBlock/index.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React from 'react';
 9 | import CodeBlock from '@theme-original/CodeBlock';
10 | import type {Props} from '@theme/CodeBlock';
11 | 
12 | // This component does nothing on purpose
13 | // Dogfood: wrapping a theme component already enhanced by another theme
14 | // See https://github.com/facebook/docusaurus/pull/5983
15 | export default function CodeBlockWrapper(props: Props): JSX.Element {
16 |   return <CodeBlock {...props} />;
17 | }
18 | 


--------------------------------------------------------------------------------
/website/src/theme/DocCategoryGeneratedIndexPage/styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .footerTip {
 9 |   font-size: 0.8rem;
10 |   margin-top: var(--ifm-paragraph-margin-bottom);
11 | }
12 | 


--------------------------------------------------------------------------------
/website/src/theme/DocSidebar/Desktop/Content/index.js:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React from 'react';
 9 | import {useLocation} from '@docusaurus/router';
10 | import Content from '@theme-original/DocSidebar/Desktop/Content';
11 | 
12 | function SidebarAd() {
13 |   return (
14 |     // eslint-disable-next-line @docusaurus/no-untranslated-text
15 |     <div style={{border: 'solid thin red', padding: 10, textAlign: 'center'}}>
16 |       Sidebar Ad
17 |     </div>
18 |   );
19 | }
20 | 
21 | export default function ContentWrapper(props) {
22 |   const {pathname} = useLocation();
23 |   const shouldShowSidebarAd = pathname.includes('/tests/');
24 |   return (
25 |     <>
26 |       {shouldShowSidebarAd && <SidebarAd />}
27 |       <Content {...props} />
28 |       {shouldShowSidebarAd && <SidebarAd />}
29 |     </>
30 |   );
31 | }
32 | 


--------------------------------------------------------------------------------
/website/src/theme/Layout/index.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React from 'react';
 9 | import Layout from '@theme-original/Layout';
10 | import type {Props} from '@theme/Layout';
11 | 
12 | // This component is only used to test for CSS insertion order
13 | import './styles.module.css';
14 | 
15 | export default function LayoutWrapper(props: Props): JSX.Element {
16 |   return <Layout {...props} />;
17 | }
18 | 


--------------------------------------------------------------------------------
/website/src/theme/Layout/styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | /* Used to test CSS insertion order */
 9 | .test-marker-theme-layout {
10 |   content: 'theme-layout';
11 | }
12 | 


--------------------------------------------------------------------------------
/website/src/theme/MDXComponents.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import MDXComponents from '@theme-original/MDXComponents';
 9 | import Code from '@theme/MDXComponents/Code';
10 | import Highlight from '@site/src/components/Highlight';
11 | import TweetQuote from '@site/src/components/TweetQuote';
12 | 
13 | export default {
14 |   ...MDXComponents,
15 |   Code,
16 |   Highlight,
17 |   TweetQuote,
18 | };
19 | 


--------------------------------------------------------------------------------
/website/src/theme/NavbarItem/ComponentTypes.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import ComponentTypes from '@theme-original/NavbarItem/ComponentTypes';
 9 | import CustomDogfoodNavbarItem from '@site/src/components/NavbarItems/CustomDogfoodNavbarItem';
10 | 
11 | export default {
12 |   ...ComponentTypes,
13 |   'custom-dogfood-navbar-item': CustomDogfoodNavbarItem,
14 | };
15 | 


--------------------------------------------------------------------------------
/website/src/theme/ReactLiveScope/components.tsx:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React, {type ComponentProps} from 'react';
 9 | 
10 | export function ButtonExample(props: ComponentProps<'button'>): JSX.Element {
11 |   return (
12 |     <button
13 |       type="button"
14 |       {...props}
15 |       style={{
16 |         backgroundColor: 'white',
17 |         color: 'black',
18 |         border: 'solid red',
19 |         borderRadius: 20,
20 |         padding: 10,
21 |         cursor: 'pointer',
22 |         ...props.style,
23 |       }}
24 |     />
25 |   );
26 | }
27 | 


--------------------------------------------------------------------------------
/website/src/theme/ReactLiveScope/index.ts:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import React from 'react';
 9 | import * as components from './components';
10 | 
11 | // Add react-live imports you need here
12 | export default {
13 |   React,
14 |   ...React,
15 |   ...components,
16 | };
17 | 


--------------------------------------------------------------------------------
/website/src/theme/theme.d.ts:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | declare module '@theme-original/ColorModeToggle' {
 9 |   export {default} from '@theme/ColorModeToggle';
10 | }
11 | 


--------------------------------------------------------------------------------
/website/src/types.d.ts:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | /// <reference types="@docusaurus/plugin-ideal-image" />
 9 | /// <reference types="@types/gtag.js" />
10 | 


--------------------------------------------------------------------------------
/website/src/utils/__tests__/jsUtils.test.ts:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | import {toggleListItem} from '../jsUtils';
 9 | 
10 | describe('toggleListItem', () => {
11 |   it('removes item already in list', () => {
12 |     expect(toggleListItem([1, 2, 3], 2)).toEqual([1, 3]);
13 |   });
14 |   it('appends item not in list', () => {
15 |     expect(toggleListItem([1, 2], 3)).toEqual([1, 2, 3]);
16 |   });
17 | });
18 | 


--------------------------------------------------------------------------------
/website/src/utils/jsUtils.ts:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | // Inspired by https://github.com/you-dont-need/You-Dont-Need-Lodash-Underscore#_sortby-and-_orderby
 9 | export function sortBy<T>(
10 |   array: T[],
11 |   getter: (item: T) => string | number | boolean,
12 | ): T[] {
13 |   const sortedArray = [...array];
14 |   sortedArray.sort((a, b) =>
15 |     // eslint-disable-next-line no-nested-ternary
16 |     getter(a) > getter(b) ? 1 : getter(b) > getter(a) ? -1 : 0,
17 |   );
18 |   return sortedArray;
19 | }
20 | 
21 | export function toggleListItem<T>(list: T[], item: T): T[] {
22 |   const itemIndex = list.indexOf(item);
23 |   if (itemIndex === -1) {
24 |     return list.concat(item);
25 |   }
26 |   const newList = [...list];
27 |   newList.splice(itemIndex, 1);
28 |   return newList;
29 | }
30 | 


--------------------------------------------------------------------------------
/website/static/_headers:
--------------------------------------------------------------------------------
 1 | 
 2 | # /assets folder contain Webpack processed assets with a file hash
 3 | # They are safe for immutable caching, as filename change when content change
 4 | 
 5 | /assets/*
 6 |   Cache-Control: public
 7 |   Cache-Control: max-age=365000000
 8 |   Cache-Control: immutable
 9 | 
10 | /fr/assets/*
11 |   Cache-Control: public
12 |   Cache-Control: max-age=365000000
13 |   Cache-Control: immutable
14 | 
15 | /pt-BR/assets/*
16 |   Cache-Control: public
17 |   Cache-Control: max-age=365000000
18 |   Cache-Control: immutable
19 | 
20 | /ko/assets/*
21 |   Cache-Control: public
22 |   Cache-Control: max-age=365000000
23 |   Cache-Control: immutable
24 | 
25 | /zh-CN/assets/*
26 |   Cache-Control: public
27 |   Cache-Control: max-age=365000000
28 |   Cache-Control: immutable
29 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/architecture.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/baseUrlIssueBanner.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/blog/2020-recap/datagit-rtl-screenshot.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/blog/2020-recap/docusaurus-npm-trends.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/blog/2020-recap/docusaurus-plushie-banner.jpeg


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/blog/2020-recap/jest-screenshot.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/blog/2020-recap/react-native-screenshot.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/blog/2021-03-09-releasing-docusaurus-i18n/datagit.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/blog/2021-03-09-releasing-docusaurus-i18n/jest.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/blog/2021-03-09-releasing-docusaurus-i18n/redwood.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/blog/2021-03-09-releasing-docusaurus-i18n/social-card.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/crowdin/crowdin-create-project.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/crowdin/crowdin-download-translations-warning.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/crowdin/crowdin-files-rename.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/crowdin/crowdin-french-translations.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/crowdin/crowdin-hide-string.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/crowdin/crowdin-settings-duplicate-strings.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/crowdin/crowdin-source-files.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/crowdin/crowdin-translate-json.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/crowdin/crowdin-translate-markdown.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/crowdin/crowdin-upload-sources-cli.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/docsearch-troubleshoot-index-facets.jpg


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/docusaurus-2020-recap.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/docusaurus-social-card.jpg


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/docusaurus-social-card.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/docusaurus.ico


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/docusaurus.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/endi.jpg


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/favicon/favicon.ico


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/icons/icon-128x128.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/icons/icon-144x144.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/icons/icon-152x152.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/icons/icon-192x192.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/icons/icon-384x384.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/icons/icon-512x512.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/icons/icon-72x72.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/icons/icon-96x96.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/playgrounds/codesandbox.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/playgrounds/stackblitz.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/profilo_blog_post_android_ios.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/profilo_blog_post_palette_website_color_picker.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/profilo_blog_post_photoshop_color_picker.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/profilo_blog_post_website_final.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/profilo_blog_post_website_final_docs.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/profilo_blog_post_website_initial.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/pwa_install.gif


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/pwa_reload.gif


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/slash-birth.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/slash-introducing.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/img/slash-up-and-running.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_AMS-Regular.ttf


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_AMS-Regular.woff


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_AMS-Regular.woff2


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Caligraphic-Bold.ttf


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Caligraphic-Bold.woff


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Caligraphic-Bold.woff2


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Caligraphic-Regular.ttf


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Caligraphic-Regular.woff


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Caligraphic-Regular.woff2


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Fraktur-Bold.ttf


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Fraktur-Bold.woff


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Fraktur-Bold.woff2


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Fraktur-Regular.ttf


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Fraktur-Regular.woff


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Fraktur-Regular.woff2


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Main-Bold.ttf


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Main-Bold.woff


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Main-Bold.woff2


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Main-BoldItalic.ttf


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Main-BoldItalic.woff


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Main-BoldItalic.woff2


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Main-Italic.ttf


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Main-Italic.woff


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Main-Italic.woff2


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Main-Regular.ttf


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Main-Regular.woff


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Main-Regular.woff2


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Math-BoldItalic.ttf


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Math-BoldItalic.woff


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Math-BoldItalic.woff2


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Math-Italic.ttf


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Math-Italic.woff


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Math-Italic.woff2


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_SansSerif-Bold.ttf


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_SansSerif-Bold.woff


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_SansSerif-Bold.woff2


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_SansSerif-Italic.ttf


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_SansSerif-Italic.woff


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_SansSerif-Italic.woff2


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_SansSerif-Regular.ttf


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_SansSerif-Regular.woff


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_SansSerif-Regular.woff2


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Script-Regular.ttf


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Script-Regular.woff


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Script-Regular.woff2


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Size1-Regular.ttf


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Size1-Regular.woff


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Size1-Regular.woff2


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Size2-Regular.ttf


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Size2-Regular.woff


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Size2-Regular.woff2


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Size3-Regular.ttf


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Size3-Regular.woff


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Size3-Regular.woff2


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Size4-Regular.ttf


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Size4-Regular.woff


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Size4-Regular.woff2


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Typewriter-Regular.ttf


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Typewriter-Regular.woff


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/static/katex/fonts/KaTeX_Typewriter-Regular.woff2


--------------------------------------------------------------------------------
/website/static/pure-html.html:
--------------------------------------------------------------------------------
 1 | <!DOCTYPE html>
 2 | <html>
 3 |   <head>
 4 |     <title>Purely HTML page | Docusaurus</title>
 5 |     <meta charset="utf-8" />
 6 |     <meta name="robots" content="noindex, nofollow" />
 7 |   </head>
 8 |   <body>
 9 |     <h1>Not part of the Docusaurus app</h1>
10 |     <div>
11 |       This page is purely HTML, placed in the <code>static</code> folder
12 |     </div>
13 |   </body>
14 | </html>
15 | 


--------------------------------------------------------------------------------
/website/svgo.config.js:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | const path = require('path');
 9 | 
10 | module.exports = {
11 |   plugins: [
12 |     {
13 |       name: 'preset-default',
14 |       params: {
15 |         overrides: {
16 |           removeTitle: false,
17 |           removeViewBox: false,
18 |         },
19 |       },
20 |     },
21 |     {
22 |       name: 'prefixIds',
23 |       params: {
24 |         delim: '',
25 |         prefix: (_, info) => path.parse(info.path).name,
26 |       },
27 |     },
28 |   ],
29 | };
30 | 


--------------------------------------------------------------------------------
/website/tsconfig.skipLibCheck.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "extends": "./tsconfig.json",
 3 |   "compilerOptions": {
 4 |     // There is no --skipLibCheck CLI option, so we have to create a config file
 5 |     // Some CI workflows will run the following command:
 6 |     // yarn workspace website typecheck --project tsconfig.skipLibCheck.json
 7 |     // See https://github.com/facebook/docusaurus/pull/10486
 8 |     "skipLibCheck": true
 9 |   }
10 | }
11 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-2.x/advanced/index.mdx:
--------------------------------------------------------------------------------
 1 | # Advanced Tutorials
 2 | 
 3 | This section is not going to be very structured, but we will cover the following topics:
 4 | 
 5 | ```mdx-code-block
 6 | import DocCardList from '@theme/DocCardList';
 7 | 
 8 | <DocCardList />
 9 | ```
10 | 
11 | We will assume that you have finished the guides, and know the basics like how to configure plugins, how to write React components, etc. These sections will have plugin authors and code contributors in mind, so we may occasionally refer to [plugin APIs](../api/plugin-methods/README.mdx) or other architecture details. Don't panic if you don't understand everything😉
12 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-2.x/api/misc/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Miscellaneous
2 | position: 4
3 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-2.x/api/misc/logger/demo.png


--------------------------------------------------------------------------------
/website/versioned_docs/version-2.x/api/plugin-methods/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Plugin method references
2 | position: 1
3 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-2.x/api/plugins/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Plugins
2 | position: 2
3 | link:
4 |   type: doc
5 |   id: api/plugins/plugins-overview # Dogfood using a "qualified id"
6 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-2.x/api/themes/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Themes
2 | position: 3
3 | link:
4 |   type: doc
5 |   id: themes-overview # Dogfood using a "local id"
6 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-2.x/api/themes/theme-live-codeblock.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 3
 3 | slug: /api/themes/@docusaurus/theme-live-codeblock
 4 | ---
 5 | 
 6 | # 📦 theme-live-codeblock
 7 | 
 8 | This theme provides a `@theme/CodeBlock` component that is powered by react-live. You can read more on [interactive code editor](../../guides/markdown-features/markdown-features-code-blocks.mdx#interactive-code-editor) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-live-codeblock
12 | ```
13 | 
14 | ### Configuration {#configuration}
15 | 
16 | ```js title="docusaurus.config.js"
17 | module.exports = {
18 |   plugins: ['@docusaurus/theme-live-codeblock'],
19 |   themeConfig: {
20 |     liveCodeBlock: {
21 |       /**
22 |        * The position of the live playground, above or under the editor
23 |        * Possible values: "top" | "bottom"
24 |        */
25 |       playgroundPosition: 'bottom',
26 |     },
27 |   },
28 | };
29 | ```
30 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-2.x/api/themes/theme-search-algolia.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 4
 3 | slug: /api/themes/@docusaurus/theme-search-algolia
 4 | ---
 5 | 
 6 | # 📦 theme-search-algolia
 7 | 
 8 | This theme provides a `@theme/SearchBar` component that integrates with Algolia DocSearch easily. Combined with `@docusaurus/theme-classic`, it provides a very easy search integration. You can read more on [search](../../search.mdx) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-search-algolia
12 | ```
13 | 
14 | This theme also adds search page available at `/search` (as swizzlable `SearchPage` component) path with OpenSearch support. You can change this default path via `themeConfig.algolia.searchPagePath`. Use `false` to disable search page.
15 | 
16 | :::tip
17 | 
18 | If you have installed `@docusaurus/preset-classic`, you don't need to install it as a dependency.
19 | 
20 | :::
21 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-2.x/assets/docusaurus-asset-example-banner.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-2.x/assets/docusaurus-asset-example.docx


--------------------------------------------------------------------------------
/website/versioned_docs/version-2.x/assets/docusaurus-asset-example.xyz:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-2.x/assets/docusaurus-asset-example.xyz


--------------------------------------------------------------------------------
/website/versioned_docs/version-2.x/guides/markdown-features/_markdown-partial-example.mdx:
--------------------------------------------------------------------------------
1 | <span>Hello {props.name}</span>
2 | 
3 | This is text some content from `_markdown-partial-example.md`.
4 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-2.x/guides/markdown-features/markdown-features-react.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .wrappingBlock {
 9 |   width: 50%;
10 |   display: inline-block;
11 |   padding: 5px;
12 |   vertical-align: top;
13 | }
14 | 
15 | .wrappingBlock code[class^='codeBlockLines'] {
16 |   white-space: pre-wrap;
17 | }
18 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-2.x/guides/markdown-features/markdown-features-tabs-styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .red {
 9 |   color: red;
10 | }
11 | 
12 | .red[aria-selected='true'] {
13 |   border-bottom-color: red;
14 | }
15 | 
16 | .orange {
17 |   color: orange;
18 | }
19 | 
20 | .orange[aria-selected='true'] {
21 |   border-bottom-color: orange;
22 | }
23 | 
24 | .yellow {
25 |   color: yellow;
26 | }
27 | 
28 | .yellow[aria-selected='true'] {
29 |   border-bottom-color: yellow;
30 | }
31 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-2.x/playground.mdx:
--------------------------------------------------------------------------------
 1 | # Playground
 2 | 
 3 | Playgrounds allow you to run Docusaurus **in your browser, without installing anything**!
 4 | 
 5 | They are mostly useful for:
 6 | 
 7 | - Testing Docusaurus
 8 | - Reporting bugs
 9 | 
10 | Use [docusaurus.new](https://docusaurus.new) as an easy-to-remember shortcut.
11 | 
12 | Choose one of the available options below.
13 | 
14 | ```mdx-code-block
15 | import {PlaygroundCardsRow} from '@site/src/components/Playground';
16 | 
17 | <PlaygroundCardsRow />
18 | ```
19 | 
20 | :::tip
21 | 
22 | For convenience, we'll remember your choice next time you visit [docusaurus.new](https://docusaurus.new).
23 | 
24 | :::
25 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.0.1/advanced/index.mdx:
--------------------------------------------------------------------------------
 1 | # Advanced Tutorials
 2 | 
 3 | This section is not going to be very structured, but we will cover the following topics:
 4 | 
 5 | ```mdx-code-block
 6 | import DocCardList from '@theme/DocCardList';
 7 | 
 8 | <DocCardList />
 9 | ```
10 | 
11 | We will assume that you have finished the guides, and know the basics like how to configure plugins, how to write React components, etc. These sections will have plugin authors and code contributors in mind, so we may occasionally refer to [plugin APIs](../api/plugin-methods/README.mdx) or other architecture details. Don't panic if you don't understand everything😉
12 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.0.1/api/misc/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Miscellaneous
2 | position: 4
3 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.0.1/api/misc/eslint-plugin/prefer-docusaurus-heading.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | slug: /api/misc/@docusaurus/eslint-plugin/prefer-docusaurus-heading
 3 | ---
 4 | 
 5 | # prefer-docusaurus-heading
 6 | 
 7 | Ensures that the `@theme/Heading` theme component provided by Docusaurus [`theme-classic`](../../themes/theme-classic.mdx) is used instead of `<hn>` tags for headings.
 8 | 
 9 | ## Rule Details {#details}
10 | 
11 | Examples of **incorrect** code for this rule:
12 | 
13 | ```html
14 | <h1>This is heading 1</h1>
15 | 
16 | <h2>This is heading 2</h2>
17 | 
18 | <h3>This is heading 3</h3>
19 | ```
20 | 
21 | Examples of **correct** code for this rule:
22 | 
23 | ```javascript
24 | import Heading from '@theme/Heading'
25 | 
26 | <Heading as='h1'>This is heading 1</Heading>
27 | 
28 | <Heading as='h2'>This is heading 2</Heading>
29 | 
30 | <Heading as='h3'>This is heading 3</Heading>
31 | ```
32 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.0.1/api/misc/logger/demo.png


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.0.1/api/plugin-methods/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Plugin method references
2 | position: 1
3 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.0.1/api/plugins/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Plugins
2 | position: 2
3 | link:
4 |   type: doc
5 |   id: api/plugins/plugins-overview # Dogfood using a "qualified id"
6 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.0.1/api/themes/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Themes
2 | position: 3
3 | link:
4 |   type: doc
5 |   id: themes-overview # Dogfood using a "local id"
6 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.0.1/api/themes/theme-live-codeblock.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 3
 3 | slug: /api/themes/@docusaurus/theme-live-codeblock
 4 | ---
 5 | 
 6 | # 📦 theme-live-codeblock
 7 | 
 8 | This theme provides a `@theme/CodeBlock` component that is powered by react-live. You can read more on [interactive code editor](../../guides/markdown-features/markdown-features-code-blocks.mdx#interactive-code-editor) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-live-codeblock
12 | ```
13 | 
14 | ### Configuration {#configuration}
15 | 
16 | ```js title="docusaurus.config.js"
17 | export default {
18 |   plugins: ['@docusaurus/theme-live-codeblock'],
19 |   themeConfig: {
20 |     liveCodeBlock: {
21 |       /**
22 |        * The position of the live playground, above or under the editor
23 |        * Possible values: "top" | "bottom"
24 |        */
25 |       playgroundPosition: 'bottom',
26 |     },
27 |   },
28 | };
29 | ```
30 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.0.1/api/themes/theme-mermaid.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 5
 3 | slug: /api/themes/@docusaurus/theme-mermaid
 4 | ---
 5 | 
 6 | # 📦 theme-mermaid
 7 | 
 8 | This theme provides a `@theme/Mermaid` component that is powered by [mermaid](https://mermaid-js.github.io/). You can read more on [diagrams](../../guides/markdown-features/markdown-features-diagrams.mdx) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-mermaid
12 | ```
13 | 
14 | ## Configuration {#configuration}
15 | 
16 | ```js title="docusaurus.config.js"
17 | export default {
18 |   themes: ['@docusaurus/theme-mermaid'],
19 |   // In order for Mermaid code blocks in Markdown to work,
20 |   // you also need to enable the Remark plugin with this option
21 |   markdown: {
22 |     mermaid: true,
23 |   },
24 | };
25 | ```
26 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.0.1/api/themes/theme-search-algolia.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 4
 3 | slug: /api/themes/@docusaurus/theme-search-algolia
 4 | ---
 5 | 
 6 | # 📦 theme-search-algolia
 7 | 
 8 | This theme provides a `@theme/SearchBar` component that integrates with Algolia DocSearch easily. Combined with `@docusaurus/theme-classic`, it provides a very easy search integration. You can read more on [search](../../search.mdx) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-search-algolia
12 | ```
13 | 
14 | This theme also adds search page available at `/search` (as swizzlable `SearchPage` component) path with OpenSearch support. You can change this default path via `themeConfig.algolia.searchPagePath`. Use `false` to disable search page.
15 | 
16 | :::tip
17 | 
18 | If you have installed `@docusaurus/preset-classic`, you don't need to install it as a dependency.
19 | 
20 | :::
21 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.0.1/assets/docusaurus-asset-example-banner.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.0.1/assets/docusaurus-asset-example.docx


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.0.1/assets/docusaurus-asset-example.xyz:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.0.1/assets/docusaurus-asset-example.xyz


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.0.1/guides/markdown-features/_markdown-partial-example.mdx:
--------------------------------------------------------------------------------
1 | <span>Hello {props.name}</span>
2 | 
3 | This is text some content from `_markdown-partial-example.md`.
4 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.0.1/guides/markdown-features/markdown-features-react.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .wrappingBlock {
 9 |   width: 50%;
10 |   display: inline-block;
11 |   padding: 5px;
12 |   vertical-align: top;
13 | }
14 | 
15 | .wrappingBlock code[class^='codeBlockLines'] {
16 |   white-space: pre-wrap;
17 | }
18 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.0.1/guides/markdown-features/markdown-features-tabs-styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .red {
 9 |   color: red;
10 | }
11 | 
12 | .red[aria-selected='true'] {
13 |   border-bottom-color: red;
14 | }
15 | 
16 | .orange {
17 |   color: orange;
18 | }
19 | 
20 | .orange[aria-selected='true'] {
21 |   border-bottom-color: orange;
22 | }
23 | 
24 | .yellow {
25 |   color: yellow;
26 | }
27 | 
28 | .yellow[aria-selected='true'] {
29 |   border-bottom-color: yellow;
30 | }
31 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.0.1/migration/index.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | slug: /migration
 3 | ---
 4 | 
 5 | # Upgrading Docusaurus
 6 | 
 7 | Docusaurus versioning is based on the `major.minor.patch` scheme and respects [**Semantic Versioning**](https://semver.org/).
 8 | 
 9 | **Breaking changes** are only released on major version upgrades, and thoroughly documented in the following upgrade guides.
10 | 
11 | import DocCardList from '@theme/DocCardList';
12 | 
13 | <DocCardList />
14 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.0.1/playground.mdx:
--------------------------------------------------------------------------------
 1 | # Playground
 2 | 
 3 | Playgrounds allow you to run Docusaurus **in your browser, without installing anything**!
 4 | 
 5 | They are mostly useful for:
 6 | 
 7 | - Testing Docusaurus
 8 | - Reporting bugs
 9 | 
10 | Use [docusaurus.new](https://docusaurus.new) as an easy-to-remember shortcut.
11 | 
12 | Choose one of the available options below.
13 | 
14 | ```mdx-code-block
15 | import {PlaygroundCardsRow} from '@site/src/components/Playground';
16 | 
17 | <PlaygroundCardsRow />
18 | ```
19 | 
20 | :::tip
21 | 
22 | For convenience, we'll remember your choice next time you visit [docusaurus.new](https://docusaurus.new).
23 | 
24 | :::
25 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.1.1/advanced/index.mdx:
--------------------------------------------------------------------------------
 1 | # Advanced Tutorials
 2 | 
 3 | This section is not going to be very structured, but we will cover the following topics:
 4 | 
 5 | ```mdx-code-block
 6 | import DocCardList from '@theme/DocCardList';
 7 | 
 8 | <DocCardList />
 9 | ```
10 | 
11 | We will assume that you have finished the guides, and know the basics like how to configure plugins, how to write React components, etc. These sections will have plugin authors and code contributors in mind, so we may occasionally refer to [plugin APIs](../api/plugin-methods/README.mdx) or other architecture details. Don't panic if you don't understand everything😉
12 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.1.1/api/misc/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Miscellaneous
2 | position: 4
3 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.1.1/api/misc/eslint-plugin/prefer-docusaurus-heading.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | slug: /api/misc/@docusaurus/eslint-plugin/prefer-docusaurus-heading
 3 | ---
 4 | 
 5 | # prefer-docusaurus-heading
 6 | 
 7 | Ensures that the `@theme/Heading` theme component provided by Docusaurus [`theme-classic`](../../themes/theme-classic.mdx) is used instead of `<hn>` tags for headings.
 8 | 
 9 | ## Rule Details {#details}
10 | 
11 | Examples of **incorrect** code for this rule:
12 | 
13 | ```html
14 | <h1>This is heading 1</h1>
15 | 
16 | <h2>This is heading 2</h2>
17 | 
18 | <h3>This is heading 3</h3>
19 | ```
20 | 
21 | Examples of **correct** code for this rule:
22 | 
23 | ```javascript
24 | import Heading from '@theme/Heading'
25 | 
26 | <Heading as='h1'>This is heading 1</Heading>
27 | 
28 | <Heading as='h2'>This is heading 2</Heading>
29 | 
30 | <Heading as='h3'>This is heading 3</Heading>
31 | ```
32 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.1.1/api/misc/logger/demo.png


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.1.1/api/plugin-methods/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Plugin method references
2 | position: 1
3 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.1.1/api/plugins/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Plugins
2 | position: 2
3 | link:
4 |   type: doc
5 |   id: api/plugins/plugins-overview # Dogfood using a "qualified id"
6 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.1.1/api/themes/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Themes
2 | position: 3
3 | link:
4 |   type: doc
5 |   id: themes-overview # Dogfood using a "local id"
6 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.1.1/api/themes/theme-live-codeblock.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 3
 3 | slug: /api/themes/@docusaurus/theme-live-codeblock
 4 | ---
 5 | 
 6 | # 📦 theme-live-codeblock
 7 | 
 8 | This theme provides a `@theme/CodeBlock` component that is powered by react-live. You can read more on [interactive code editor](../../guides/markdown-features/markdown-features-code-blocks.mdx#interactive-code-editor) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-live-codeblock
12 | ```
13 | 
14 | ### Configuration {#configuration}
15 | 
16 | ```js title="docusaurus.config.js"
17 | export default {
18 |   plugins: ['@docusaurus/theme-live-codeblock'],
19 |   themeConfig: {
20 |     liveCodeBlock: {
21 |       /**
22 |        * The position of the live playground, above or under the editor
23 |        * Possible values: "top" | "bottom"
24 |        */
25 |       playgroundPosition: 'bottom',
26 |     },
27 |   },
28 | };
29 | ```
30 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.1.1/api/themes/theme-mermaid.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 5
 3 | slug: /api/themes/@docusaurus/theme-mermaid
 4 | ---
 5 | 
 6 | # 📦 theme-mermaid
 7 | 
 8 | This theme provides a `@theme/Mermaid` component that is powered by [mermaid](https://mermaid-js.github.io/). You can read more on [diagrams](../../guides/markdown-features/markdown-features-diagrams.mdx) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-mermaid
12 | ```
13 | 
14 | ## Configuration {#configuration}
15 | 
16 | ```js title="docusaurus.config.js"
17 | export default {
18 |   themes: ['@docusaurus/theme-mermaid'],
19 |   // In order for Mermaid code blocks in Markdown to work,
20 |   // you also need to enable the Remark plugin with this option
21 |   markdown: {
22 |     mermaid: true,
23 |   },
24 | };
25 | ```
26 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.1.1/api/themes/theme-search-algolia.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 4
 3 | slug: /api/themes/@docusaurus/theme-search-algolia
 4 | ---
 5 | 
 6 | # 📦 theme-search-algolia
 7 | 
 8 | This theme provides a `@theme/SearchBar` component that integrates with Algolia DocSearch easily. Combined with `@docusaurus/theme-classic`, it provides a very easy search integration. You can read more on [search](../../search.mdx) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-search-algolia
12 | ```
13 | 
14 | This theme also adds search page available at `/search` (as swizzlable `SearchPage` component) path with OpenSearch support. You can change this default path via `themeConfig.algolia.searchPagePath`. Use `false` to disable search page.
15 | 
16 | :::tip
17 | 
18 | If you have installed `@docusaurus/preset-classic`, you don't need to install it as a dependency.
19 | 
20 | :::
21 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.1.1/assets/docusaurus-asset-example-banner.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.1.1/assets/docusaurus-asset-example.docx


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.1.1/assets/docusaurus-asset-example.xyz:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.1.1/assets/docusaurus-asset-example.xyz


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.1.1/guides/markdown-features/_markdown-partial-example.mdx:
--------------------------------------------------------------------------------
1 | <span>Hello {props.name}</span>
2 | 
3 | This is text some content from `_markdown-partial-example.md`.
4 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.1.1/guides/markdown-features/markdown-features-react.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .wrappingBlock {
 9 |   width: 50%;
10 |   display: inline-block;
11 |   padding: 5px;
12 |   vertical-align: top;
13 | }
14 | 
15 | .wrappingBlock code[class^='codeBlockLines'] {
16 |   white-space: pre-wrap;
17 | }
18 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.1.1/guides/markdown-features/markdown-features-tabs-styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .red {
 9 |   color: red;
10 | }
11 | 
12 | .red[aria-selected='true'] {
13 |   border-bottom-color: red;
14 | }
15 | 
16 | .orange {
17 |   color: orange;
18 | }
19 | 
20 | .orange[aria-selected='true'] {
21 |   border-bottom-color: orange;
22 | }
23 | 
24 | .yellow {
25 |   color: yellow;
26 | }
27 | 
28 | .yellow[aria-selected='true'] {
29 |   border-bottom-color: yellow;
30 | }
31 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.1.1/migration/index.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | slug: /migration
 3 | ---
 4 | 
 5 | # Upgrading Docusaurus
 6 | 
 7 | Docusaurus versioning is based on the `major.minor.patch` scheme and respects [**Semantic Versioning**](https://semver.org/).
 8 | 
 9 | **Breaking changes** are only released on major version upgrades, and thoroughly documented in the following upgrade guides.
10 | 
11 | import DocCardList from '@theme/DocCardList';
12 | 
13 | <DocCardList />
14 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.1.1/playground.mdx:
--------------------------------------------------------------------------------
 1 | # Playground
 2 | 
 3 | Playgrounds allow you to run Docusaurus **in your browser, without installing anything**!
 4 | 
 5 | They are mostly useful for:
 6 | 
 7 | - Testing Docusaurus
 8 | - Reporting bugs
 9 | 
10 | Use [docusaurus.new](https://docusaurus.new) as an easy-to-remember shortcut.
11 | 
12 | Choose one of the available options below.
13 | 
14 | ```mdx-code-block
15 | import {PlaygroundCardsRow} from '@site/src/components/Playground';
16 | 
17 | <PlaygroundCardsRow />
18 | ```
19 | 
20 | :::tip
21 | 
22 | For convenience, we'll remember your choice next time you visit [docusaurus.new](https://docusaurus.new).
23 | 
24 | :::
25 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.2.1/advanced/index.mdx:
--------------------------------------------------------------------------------
 1 | # Advanced Tutorials
 2 | 
 3 | This section is not going to be very structured, but we will cover the following topics:
 4 | 
 5 | ```mdx-code-block
 6 | import DocCardList from '@theme/DocCardList';
 7 | 
 8 | <DocCardList />
 9 | ```
10 | 
11 | We will assume that you have finished the guides, and know the basics like how to configure plugins, how to write React components, etc. These sections will have plugin authors and code contributors in mind, so we may occasionally refer to [plugin APIs](../api/plugin-methods/README.mdx) or other architecture details. Don't panic if you don't understand everything😉
12 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.2.1/api/misc/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Miscellaneous
2 | position: 4
3 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.2.1/api/misc/eslint-plugin/prefer-docusaurus-heading.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | slug: /api/misc/@docusaurus/eslint-plugin/prefer-docusaurus-heading
 3 | ---
 4 | 
 5 | # prefer-docusaurus-heading
 6 | 
 7 | Ensures that the `@theme/Heading` theme component provided by Docusaurus [`theme-classic`](../../themes/theme-classic.mdx) is used instead of `<hn>` tags for headings.
 8 | 
 9 | ## Rule Details {#details}
10 | 
11 | Examples of **incorrect** code for this rule:
12 | 
13 | ```html
14 | <h1>This is heading 1</h1>
15 | 
16 | <h2>This is heading 2</h2>
17 | 
18 | <h3>This is heading 3</h3>
19 | ```
20 | 
21 | Examples of **correct** code for this rule:
22 | 
23 | ```javascript
24 | import Heading from '@theme/Heading'
25 | 
26 | <Heading as='h1'>This is heading 1</Heading>
27 | 
28 | <Heading as='h2'>This is heading 2</Heading>
29 | 
30 | <Heading as='h3'>This is heading 3</Heading>
31 | ```
32 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.2.1/api/misc/logger/demo.png


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.2.1/api/plugin-methods/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Plugin method references
2 | position: 1
3 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.2.1/api/plugins/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Plugins
2 | position: 2
3 | link:
4 |   type: doc
5 |   id: api/plugins/plugins-overview # Dogfood using a "qualified id"
6 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.2.1/api/themes/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Themes
2 | position: 3
3 | link:
4 |   type: doc
5 |   id: themes-overview # Dogfood using a "local id"
6 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.2.1/api/themes/theme-live-codeblock.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 3
 3 | slug: /api/themes/@docusaurus/theme-live-codeblock
 4 | ---
 5 | 
 6 | # 📦 theme-live-codeblock
 7 | 
 8 | This theme provides a `@theme/CodeBlock` component that is powered by react-live. You can read more on [interactive code editor](../../guides/markdown-features/markdown-features-code-blocks.mdx#interactive-code-editor) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-live-codeblock
12 | ```
13 | 
14 | ### Configuration {#configuration}
15 | 
16 | ```js title="docusaurus.config.js"
17 | export default {
18 |   plugins: ['@docusaurus/theme-live-codeblock'],
19 |   themeConfig: {
20 |     liveCodeBlock: {
21 |       /**
22 |        * The position of the live playground, above or under the editor
23 |        * Possible values: "top" | "bottom"
24 |        */
25 |       playgroundPosition: 'bottom',
26 |     },
27 |   },
28 | };
29 | ```
30 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.2.1/api/themes/theme-mermaid.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 5
 3 | slug: /api/themes/@docusaurus/theme-mermaid
 4 | ---
 5 | 
 6 | # 📦 theme-mermaid
 7 | 
 8 | This theme provides a `@theme/Mermaid` component that is powered by [mermaid](https://mermaid-js.github.io/). You can read more on [diagrams](../../guides/markdown-features/markdown-features-diagrams.mdx) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-mermaid
12 | ```
13 | 
14 | ## Configuration {#configuration}
15 | 
16 | ```js title="docusaurus.config.js"
17 | export default {
18 |   themes: ['@docusaurus/theme-mermaid'],
19 |   // In order for Mermaid code blocks in Markdown to work,
20 |   // you also need to enable the Remark plugin with this option
21 |   markdown: {
22 |     mermaid: true,
23 |   },
24 | };
25 | ```
26 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.2.1/api/themes/theme-search-algolia.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 4
 3 | slug: /api/themes/@docusaurus/theme-search-algolia
 4 | ---
 5 | 
 6 | # 📦 theme-search-algolia
 7 | 
 8 | This theme provides a `@theme/SearchBar` component that integrates with Algolia DocSearch easily. Combined with `@docusaurus/theme-classic`, it provides a very easy search integration. You can read more on [search](../../search.mdx) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-search-algolia
12 | ```
13 | 
14 | This theme also adds search page available at `/search` (as swizzlable `SearchPage` component) path with OpenSearch support. You can change this default path via `themeConfig.algolia.searchPagePath`. Use `false` to disable search page.
15 | 
16 | :::tip
17 | 
18 | If you have installed `@docusaurus/preset-classic`, you don't need to install it as a dependency.
19 | 
20 | :::
21 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.2.1/assets/docusaurus-asset-example-banner.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.2.1/assets/docusaurus-asset-example.docx


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.2.1/assets/docusaurus-asset-example.xyz:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.2.1/assets/docusaurus-asset-example.xyz


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.2.1/guides/markdown-features/_markdown-partial-example.mdx:
--------------------------------------------------------------------------------
1 | <span>Hello {props.name}</span>
2 | 
3 | This is text some content from `_markdown-partial-example.md`.
4 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.2.1/guides/markdown-features/markdown-features-react.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .wrappingBlock {
 9 |   width: 50%;
10 |   display: inline-block;
11 |   padding: 5px;
12 |   vertical-align: top;
13 | }
14 | 
15 | .wrappingBlock code[class^='codeBlockLines'] {
16 |   white-space: pre-wrap;
17 | }
18 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.2.1/guides/markdown-features/markdown-features-tabs-styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .red {
 9 |   color: red;
10 | }
11 | 
12 | .red[aria-selected='true'] {
13 |   border-bottom-color: red;
14 | }
15 | 
16 | .orange {
17 |   color: orange;
18 | }
19 | 
20 | .orange[aria-selected='true'] {
21 |   border-bottom-color: orange;
22 | }
23 | 
24 | .yellow {
25 |   color: yellow;
26 | }
27 | 
28 | .yellow[aria-selected='true'] {
29 |   border-bottom-color: yellow;
30 | }
31 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.2.1/migration/index.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | slug: /migration
 3 | ---
 4 | 
 5 | # Upgrading Docusaurus
 6 | 
 7 | Docusaurus versioning is based on the `major.minor.patch` scheme and respects [**Semantic Versioning**](https://semver.org/).
 8 | 
 9 | **Breaking changes** are only released on major version upgrades, and thoroughly documented in the following upgrade guides.
10 | 
11 | import DocCardList from '@theme/DocCardList';
12 | 
13 | <DocCardList />
14 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.2.1/playground.mdx:
--------------------------------------------------------------------------------
 1 | # Playground
 2 | 
 3 | Playgrounds allow you to run Docusaurus **in your browser, without installing anything**!
 4 | 
 5 | They are mostly useful for:
 6 | 
 7 | - Testing Docusaurus
 8 | - Reporting bugs
 9 | 
10 | Use [docusaurus.new](https://docusaurus.new) as an easy-to-remember shortcut.
11 | 
12 | Choose one of the available options below.
13 | 
14 | ```mdx-code-block
15 | import {PlaygroundCardsRow} from '@site/src/components/Playground';
16 | 
17 | <PlaygroundCardsRow />
18 | ```
19 | 
20 | :::tip
21 | 
22 | For convenience, we'll remember your choice next time you visit [docusaurus.new](https://docusaurus.new).
23 | 
24 | :::
25 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.3.2/advanced/index.mdx:
--------------------------------------------------------------------------------
 1 | # Advanced Tutorials
 2 | 
 3 | This section is not going to be very structured, but we will cover the following topics:
 4 | 
 5 | ```mdx-code-block
 6 | import DocCardList from '@theme/DocCardList';
 7 | 
 8 | <DocCardList />
 9 | ```
10 | 
11 | We will assume that you have finished the guides, and know the basics like how to configure plugins, how to write React components, etc. These sections will have plugin authors and code contributors in mind, so we may occasionally refer to [plugin APIs](../api/plugin-methods/README.mdx) or other architecture details. Don't panic if you don't understand everything😉
12 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.3.2/api/misc/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Miscellaneous
2 | position: 4
3 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.3.2/api/misc/eslint-plugin/prefer-docusaurus-heading.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | slug: /api/misc/@docusaurus/eslint-plugin/prefer-docusaurus-heading
 3 | ---
 4 | 
 5 | # prefer-docusaurus-heading
 6 | 
 7 | Ensures that the `@theme/Heading` theme component provided by Docusaurus [`theme-classic`](../../themes/theme-classic.mdx) is used instead of `<hn>` tags for headings.
 8 | 
 9 | ## Rule Details {#details}
10 | 
11 | Examples of **incorrect** code for this rule:
12 | 
13 | ```html
14 | <h1>This is heading 1</h1>
15 | 
16 | <h2>This is heading 2</h2>
17 | 
18 | <h3>This is heading 3</h3>
19 | ```
20 | 
21 | Examples of **correct** code for this rule:
22 | 
23 | ```javascript
24 | import Heading from '@theme/Heading'
25 | 
26 | <Heading as='h1'>This is heading 1</Heading>
27 | 
28 | <Heading as='h2'>This is heading 2</Heading>
29 | 
30 | <Heading as='h3'>This is heading 3</Heading>
31 | ```
32 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.3.2/api/misc/logger/demo.png


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.3.2/api/plugin-methods/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Plugin method references
2 | position: 1
3 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.3.2/api/plugins/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Plugins
2 | position: 2
3 | link:
4 |   type: doc
5 |   id: api/plugins/plugins-overview # Dogfood using a "qualified id"
6 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.3.2/api/themes/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Themes
2 | position: 3
3 | link:
4 |   type: doc
5 |   id: themes-overview # Dogfood using a "local id"
6 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.3.2/api/themes/theme-live-codeblock.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 3
 3 | slug: /api/themes/@docusaurus/theme-live-codeblock
 4 | ---
 5 | 
 6 | # 📦 theme-live-codeblock
 7 | 
 8 | This theme provides a `@theme/CodeBlock` component that is powered by react-live. You can read more on [interactive code editor](../../guides/markdown-features/markdown-features-code-blocks.mdx#interactive-code-editor) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-live-codeblock
12 | ```
13 | 
14 | ### Configuration {#configuration}
15 | 
16 | ```js title="docusaurus.config.js"
17 | export default {
18 |   plugins: ['@docusaurus/theme-live-codeblock'],
19 |   themeConfig: {
20 |     liveCodeBlock: {
21 |       /**
22 |        * The position of the live playground, above or under the editor
23 |        * Possible values: "top" | "bottom"
24 |        */
25 |       playgroundPosition: 'bottom',
26 |     },
27 |   },
28 | };
29 | ```
30 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.3.2/api/themes/theme-mermaid.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 5
 3 | slug: /api/themes/@docusaurus/theme-mermaid
 4 | ---
 5 | 
 6 | # 📦 theme-mermaid
 7 | 
 8 | This theme provides a `@theme/Mermaid` component that is powered by [mermaid](https://mermaid-js.github.io/). You can read more on [diagrams](../../guides/markdown-features/markdown-features-diagrams.mdx) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-mermaid
12 | ```
13 | 
14 | ## Configuration {#configuration}
15 | 
16 | ```js title="docusaurus.config.js"
17 | export default {
18 |   themes: ['@docusaurus/theme-mermaid'],
19 |   // In order for Mermaid code blocks in Markdown to work,
20 |   // you also need to enable the Remark plugin with this option
21 |   markdown: {
22 |     mermaid: true,
23 |   },
24 | };
25 | ```
26 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.3.2/api/themes/theme-search-algolia.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 4
 3 | slug: /api/themes/@docusaurus/theme-search-algolia
 4 | ---
 5 | 
 6 | # 📦 theme-search-algolia
 7 | 
 8 | This theme provides a `@theme/SearchBar` component that integrates with Algolia DocSearch easily. Combined with `@docusaurus/theme-classic`, it provides a very easy search integration. You can read more on [search](../../search.mdx) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-search-algolia
12 | ```
13 | 
14 | This theme also adds search page available at `/search` (as swizzlable `SearchPage` component) path with OpenSearch support. You can change this default path via `themeConfig.algolia.searchPagePath`. Use `false` to disable search page.
15 | 
16 | :::tip
17 | 
18 | If you have installed `@docusaurus/preset-classic`, you don't need to install it as a dependency.
19 | 
20 | :::
21 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.3.2/assets/docusaurus-asset-example-banner.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.3.2/assets/docusaurus-asset-example.docx


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.3.2/assets/docusaurus-asset-example.xyz:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.3.2/assets/docusaurus-asset-example.xyz


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.3.2/guides/markdown-features/_markdown-partial-example.mdx:
--------------------------------------------------------------------------------
1 | <span>Hello {props.name}</span>
2 | 
3 | This is text some content from `_markdown-partial-example.md`.
4 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.3.2/guides/markdown-features/markdown-features-react.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .wrappingBlock {
 9 |   width: 50%;
10 |   display: inline-block;
11 |   padding: 5px;
12 |   vertical-align: top;
13 | }
14 | 
15 | .wrappingBlock code[class^='codeBlockLines'] {
16 |   white-space: pre-wrap;
17 | }
18 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.3.2/guides/markdown-features/markdown-features-tabs-styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .red {
 9 |   color: red;
10 | }
11 | 
12 | .red[aria-selected='true'] {
13 |   border-bottom-color: red;
14 | }
15 | 
16 | .orange {
17 |   color: orange;
18 | }
19 | 
20 | .orange[aria-selected='true'] {
21 |   border-bottom-color: orange;
22 | }
23 | 
24 | .yellow {
25 |   color: yellow;
26 | }
27 | 
28 | .yellow[aria-selected='true'] {
29 |   border-bottom-color: yellow;
30 | }
31 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.3.2/playground.mdx:
--------------------------------------------------------------------------------
 1 | # Playground
 2 | 
 3 | Playgrounds allow you to run Docusaurus **in your browser, without installing anything**!
 4 | 
 5 | They are mostly useful for:
 6 | 
 7 | - Testing Docusaurus
 8 | - Reporting bugs
 9 | 
10 | Use [docusaurus.new](https://docusaurus.new) as an easy-to-remember shortcut.
11 | 
12 | Choose one of the available options below.
13 | 
14 | ```mdx-code-block
15 | import {PlaygroundCardsRow} from '@site/src/components/Playground';
16 | 
17 | <PlaygroundCardsRow />
18 | ```
19 | 
20 | :::tip
21 | 
22 | For convenience, we'll remember your choice next time you visit [docusaurus.new](https://docusaurus.new).
23 | 
24 | :::
25 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.4.0/advanced/index.mdx:
--------------------------------------------------------------------------------
 1 | # Advanced Tutorials
 2 | 
 3 | This section is not going to be very structured, but we will cover the following topics:
 4 | 
 5 | ```mdx-code-block
 6 | import DocCardList from '@theme/DocCardList';
 7 | 
 8 | <DocCardList />
 9 | ```
10 | 
11 | We will assume that you have finished the guides, and know the basics like how to configure plugins, how to write React components, etc. These sections will have plugin authors and code contributors in mind, so we may occasionally refer to [plugin APIs](../api/plugin-methods/README.mdx) or other architecture details. Don't panic if you don't understand everything😉
12 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.4.0/api/misc/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Miscellaneous
2 | position: 4
3 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.4.0/api/misc/eslint-plugin/prefer-docusaurus-heading.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | slug: /api/misc/@docusaurus/eslint-plugin/prefer-docusaurus-heading
 3 | ---
 4 | 
 5 | # prefer-docusaurus-heading
 6 | 
 7 | Ensures that the `@theme/Heading` theme component provided by Docusaurus [`theme-classic`](../../themes/theme-classic.mdx) is used instead of `<hn>` tags for headings.
 8 | 
 9 | ## Rule Details {#details}
10 | 
11 | Examples of **incorrect** code for this rule:
12 | 
13 | ```html
14 | <h1>This is heading 1</h1>
15 | 
16 | <h2>This is heading 2</h2>
17 | 
18 | <h3>This is heading 3</h3>
19 | ```
20 | 
21 | Examples of **correct** code for this rule:
22 | 
23 | ```javascript
24 | import Heading from '@theme/Heading'
25 | 
26 | <Heading as='h1'>This is heading 1</Heading>
27 | 
28 | <Heading as='h2'>This is heading 2</Heading>
29 | 
30 | <Heading as='h3'>This is heading 3</Heading>
31 | ```
32 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.4.0/api/misc/logger/demo.png


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.4.0/api/plugin-methods/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Plugin method references
2 | position: 1
3 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.4.0/api/plugins/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Plugins
2 | position: 2
3 | link:
4 |   type: doc
5 |   id: api/plugins/plugins-overview # Dogfood using a "qualified id"
6 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.4.0/api/themes/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Themes
2 | position: 3
3 | link:
4 |   type: doc
5 |   id: themes-overview # Dogfood using a "local id"
6 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.4.0/api/themes/theme-live-codeblock.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 3
 3 | slug: /api/themes/@docusaurus/theme-live-codeblock
 4 | ---
 5 | 
 6 | # 📦 theme-live-codeblock
 7 | 
 8 | This theme provides a `@theme/CodeBlock` component that is powered by react-live. You can read more on [interactive code editor](../../guides/markdown-features/markdown-features-code-blocks.mdx#interactive-code-editor) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-live-codeblock
12 | ```
13 | 
14 | ### Configuration {#configuration}
15 | 
16 | ```js title="docusaurus.config.js"
17 | export default {
18 |   plugins: ['@docusaurus/theme-live-codeblock'],
19 |   themeConfig: {
20 |     liveCodeBlock: {
21 |       /**
22 |        * The position of the live playground, above or under the editor
23 |        * Possible values: "top" | "bottom"
24 |        */
25 |       playgroundPosition: 'bottom',
26 |     },
27 |   },
28 | };
29 | ```
30 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.4.0/api/themes/theme-mermaid.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 5
 3 | slug: /api/themes/@docusaurus/theme-mermaid
 4 | ---
 5 | 
 6 | # 📦 theme-mermaid
 7 | 
 8 | This theme provides a `@theme/Mermaid` component that is powered by [mermaid](https://mermaid-js.github.io/). You can read more on [diagrams](../../guides/markdown-features/markdown-features-diagrams.mdx) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-mermaid
12 | ```
13 | 
14 | ## Configuration {#configuration}
15 | 
16 | ```js title="docusaurus.config.js"
17 | export default {
18 |   themes: ['@docusaurus/theme-mermaid'],
19 |   // In order for Mermaid code blocks in Markdown to work,
20 |   // you also need to enable the Remark plugin with this option
21 |   markdown: {
22 |     mermaid: true,
23 |   },
24 | };
25 | ```
26 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.4.0/api/themes/theme-search-algolia.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 4
 3 | slug: /api/themes/@docusaurus/theme-search-algolia
 4 | ---
 5 | 
 6 | # 📦 theme-search-algolia
 7 | 
 8 | This theme provides a `@theme/SearchBar` component that integrates with Algolia DocSearch easily. Combined with `@docusaurus/theme-classic`, it provides a very easy search integration. You can read more on [search](../../search.mdx) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-search-algolia
12 | ```
13 | 
14 | This theme also adds search page available at `/search` (as swizzlable `SearchPage` component) path with OpenSearch support. You can change this default path via `themeConfig.algolia.searchPagePath`. Use `false` to disable search page.
15 | 
16 | :::tip
17 | 
18 | If you have installed `@docusaurus/preset-classic`, you don't need to install it as a dependency.
19 | 
20 | :::
21 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.4.0/assets/docusaurus-asset-example-banner.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.4.0/assets/docusaurus-asset-example.docx


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.4.0/assets/docusaurus-asset-example.xyz:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.4.0/assets/docusaurus-asset-example.xyz


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.4.0/guides/markdown-features/_markdown-partial-example.mdx:
--------------------------------------------------------------------------------
1 | <span>Hello {props.name}</span>
2 | 
3 | This is text some content from `_markdown-partial-example.md`.
4 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.4.0/guides/markdown-features/markdown-features-react.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .wrappingBlock {
 9 |   width: 50%;
10 |   display: inline-block;
11 |   padding: 5px;
12 |   vertical-align: top;
13 | }
14 | 
15 | .wrappingBlock code[class^='codeBlockLines'] {
16 |   white-space: pre-wrap;
17 | }
18 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.4.0/guides/markdown-features/markdown-features-tabs-styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .red {
 9 |   color: red;
10 | }
11 | 
12 | .red[aria-selected='true'] {
13 |   border-bottom-color: red;
14 | }
15 | 
16 | .orange {
17 |   color: orange;
18 | }
19 | 
20 | .orange[aria-selected='true'] {
21 |   border-bottom-color: orange;
22 | }
23 | 
24 | .yellow {
25 |   color: yellow;
26 | }
27 | 
28 | .yellow[aria-selected='true'] {
29 |   border-bottom-color: yellow;
30 | }
31 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.4.0/playground.mdx:
--------------------------------------------------------------------------------
 1 | # Playground
 2 | 
 3 | Playgrounds allow you to run Docusaurus **in your browser, without installing anything**!
 4 | 
 5 | They are mostly useful for:
 6 | 
 7 | - Testing Docusaurus
 8 | - Reporting bugs
 9 | 
10 | Use [docusaurus.new](https://docusaurus.new) as an easy-to-remember shortcut.
11 | 
12 | Choose one of the available options below.
13 | 
14 | ```mdx-code-block
15 | import {PlaygroundCardsRow} from '@site/src/components/Playground';
16 | 
17 | <PlaygroundCardsRow />
18 | ```
19 | 
20 | :::tip
21 | 
22 | For convenience, we'll remember your choice next time you visit [docusaurus.new](https://docusaurus.new).
23 | 
24 | :::
25 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.5.2/advanced/index.mdx:
--------------------------------------------------------------------------------
 1 | # Advanced Tutorials
 2 | 
 3 | This section is not going to be very structured, but we will cover the following topics:
 4 | 
 5 | ```mdx-code-block
 6 | import DocCardList from '@theme/DocCardList';
 7 | 
 8 | <DocCardList />
 9 | ```
10 | 
11 | We will assume that you have finished the guides, and know the basics like how to configure plugins, how to write React components, etc. These sections will have plugin authors and code contributors in mind, so we may occasionally refer to [plugin APIs](../api/plugin-methods/README.mdx) or other architecture details. Don't panic if you don't understand everything😉
12 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.5.2/api/misc/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Miscellaneous
2 | position: 4
3 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.5.2/api/misc/eslint-plugin/prefer-docusaurus-heading.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | slug: /api/misc/@docusaurus/eslint-plugin/prefer-docusaurus-heading
 3 | ---
 4 | 
 5 | # prefer-docusaurus-heading
 6 | 
 7 | Ensures that the `@theme/Heading` theme component provided by Docusaurus [`theme-classic`](../../themes/theme-classic.mdx) is used instead of `<hn>` tags for headings.
 8 | 
 9 | ## Rule Details {#details}
10 | 
11 | Examples of **incorrect** code for this rule:
12 | 
13 | ```html
14 | <h1>This is heading 1</h1>
15 | 
16 | <h2>This is heading 2</h2>
17 | 
18 | <h3>This is heading 3</h3>
19 | ```
20 | 
21 | Examples of **correct** code for this rule:
22 | 
23 | ```javascript
24 | import Heading from '@theme/Heading'
25 | 
26 | <Heading as='h1'>This is heading 1</Heading>
27 | 
28 | <Heading as='h2'>This is heading 2</Heading>
29 | 
30 | <Heading as='h3'>This is heading 3</Heading>
31 | ```
32 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.5.2/api/misc/logger/demo.png


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.5.2/api/plugin-methods/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Plugin method references
2 | position: 1
3 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.5.2/api/plugins/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Plugins
2 | position: 2
3 | link:
4 |   type: doc
5 |   id: api/plugins/plugins-overview # Dogfood using a "qualified id"
6 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.5.2/api/themes/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Themes
2 | position: 3
3 | link:
4 |   type: doc
5 |   id: themes-overview # Dogfood using a "local id"
6 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.5.2/api/themes/theme-live-codeblock.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 3
 3 | slug: /api/themes/@docusaurus/theme-live-codeblock
 4 | ---
 5 | 
 6 | # 📦 theme-live-codeblock
 7 | 
 8 | This theme provides a `@theme/CodeBlock` component that is powered by react-live. You can read more on [interactive code editor](../../guides/markdown-features/markdown-features-code-blocks.mdx#interactive-code-editor) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-live-codeblock
12 | ```
13 | 
14 | ### Configuration {#configuration}
15 | 
16 | ```js title="docusaurus.config.js"
17 | export default {
18 |   plugins: ['@docusaurus/theme-live-codeblock'],
19 |   themeConfig: {
20 |     liveCodeBlock: {
21 |       /**
22 |        * The position of the live playground, above or under the editor
23 |        * Possible values: "top" | "bottom"
24 |        */
25 |       playgroundPosition: 'bottom',
26 |     },
27 |   },
28 | };
29 | ```
30 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.5.2/api/themes/theme-mermaid.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 5
 3 | slug: /api/themes/@docusaurus/theme-mermaid
 4 | ---
 5 | 
 6 | # 📦 theme-mermaid
 7 | 
 8 | This theme provides a `@theme/Mermaid` component that is powered by [mermaid](https://mermaid-js.github.io/). You can read more on [diagrams](../../guides/markdown-features/markdown-features-diagrams.mdx) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-mermaid
12 | ```
13 | 
14 | ## Configuration {#configuration}
15 | 
16 | ```js title="docusaurus.config.js"
17 | export default {
18 |   themes: ['@docusaurus/theme-mermaid'],
19 |   // In order for Mermaid code blocks in Markdown to work,
20 |   // you also need to enable the Remark plugin with this option
21 |   markdown: {
22 |     mermaid: true,
23 |   },
24 | };
25 | ```
26 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.5.2/api/themes/theme-search-algolia.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 4
 3 | slug: /api/themes/@docusaurus/theme-search-algolia
 4 | ---
 5 | 
 6 | # 📦 theme-search-algolia
 7 | 
 8 | This theme provides a `@theme/SearchBar` component that integrates with Algolia DocSearch easily. Combined with `@docusaurus/theme-classic`, it provides a very easy search integration. You can read more on [search](../../search.mdx) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-search-algolia
12 | ```
13 | 
14 | This theme also adds search page available at `/search` (as swizzlable `SearchPage` component) path with OpenSearch support. You can change this default path via `themeConfig.algolia.searchPagePath`. Use `false` to disable search page.
15 | 
16 | :::tip
17 | 
18 | If you have installed `@docusaurus/preset-classic`, you don't need to install it as a dependency.
19 | 
20 | :::
21 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.5.2/assets/docusaurus-asset-example-banner.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.5.2/assets/docusaurus-asset-example.docx


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.5.2/assets/docusaurus-asset-example.xyz:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.5.2/assets/docusaurus-asset-example.xyz


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.5.2/guides/markdown-features/_markdown-partial-example.mdx:
--------------------------------------------------------------------------------
1 | <span>Hello {props.name}</span>
2 | 
3 | This is text some content from `_markdown-partial-example.md`.
4 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.5.2/guides/markdown-features/markdown-features-react.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .wrappingBlock {
 9 |   width: 50%;
10 |   display: inline-block;
11 |   padding: 5px;
12 |   vertical-align: top;
13 | }
14 | 
15 | .wrappingBlock code[class^='codeBlockLines'] {
16 |   white-space: pre-wrap;
17 | }
18 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.5.2/guides/markdown-features/markdown-features-tabs-styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .red {
 9 |   color: red;
10 | }
11 | 
12 | .red[aria-selected='true'] {
13 |   border-bottom-color: red;
14 | }
15 | 
16 | .orange {
17 |   color: orange;
18 | }
19 | 
20 | .orange[aria-selected='true'] {
21 |   border-bottom-color: orange;
22 | }
23 | 
24 | .yellow {
25 |   color: yellow;
26 | }
27 | 
28 | .yellow[aria-selected='true'] {
29 |   border-bottom-color: yellow;
30 | }
31 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.5.2/playground.mdx:
--------------------------------------------------------------------------------
 1 | # Playground
 2 | 
 3 | Playgrounds allow you to run Docusaurus **in your browser, without installing anything**!
 4 | 
 5 | They are mostly useful for:
 6 | 
 7 | - Testing Docusaurus
 8 | - Reporting bugs
 9 | 
10 | Use [docusaurus.new](https://docusaurus.new) as an easy-to-remember shortcut.
11 | 
12 | Choose one of the available options below.
13 | 
14 | ```mdx-code-block
15 | import {PlaygroundCardsRow} from '@site/src/components/Playground';
16 | 
17 | <PlaygroundCardsRow />
18 | ```
19 | 
20 | :::tip
21 | 
22 | For convenience, we'll remember your choice next time you visit [docusaurus.new](https://docusaurus.new).
23 | 
24 | :::
25 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.6.3/advanced/index.mdx:
--------------------------------------------------------------------------------
 1 | # Advanced Tutorials
 2 | 
 3 | This section is not going to be very structured, but we will cover the following topics:
 4 | 
 5 | ```mdx-code-block
 6 | import DocCardList from '@theme/DocCardList';
 7 | 
 8 | <DocCardList />
 9 | ```
10 | 
11 | We will assume that you have finished the guides, and know the basics like how to configure plugins, how to write React components, etc. These sections will have plugin authors and code contributors in mind, so we may occasionally refer to [plugin APIs](../api/plugin-methods/README.mdx) or other architecture details. Don't panic if you don't understand everything😉
12 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.6.3/api/misc/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Miscellaneous
2 | position: 4
3 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.6.3/api/misc/eslint-plugin/prefer-docusaurus-heading.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | slug: /api/misc/@docusaurus/eslint-plugin/prefer-docusaurus-heading
 3 | ---
 4 | 
 5 | # prefer-docusaurus-heading
 6 | 
 7 | Ensures that the `@theme/Heading` theme component provided by Docusaurus [`theme-classic`](../../themes/theme-classic.mdx) is used instead of `<hn>` tags for headings.
 8 | 
 9 | ## Rule Details {#details}
10 | 
11 | Examples of **incorrect** code for this rule:
12 | 
13 | ```html
14 | <h1>This is heading 1</h1>
15 | 
16 | <h2>This is heading 2</h2>
17 | 
18 | <h3>This is heading 3</h3>
19 | ```
20 | 
21 | Examples of **correct** code for this rule:
22 | 
23 | ```javascript
24 | import Heading from '@theme/Heading'
25 | 
26 | <Heading as='h1'>This is heading 1</Heading>
27 | 
28 | <Heading as='h2'>This is heading 2</Heading>
29 | 
30 | <Heading as='h3'>This is heading 3</Heading>
31 | ```
32 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.6.3/api/misc/logger/demo.png


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.6.3/api/plugin-methods/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Plugin method references
2 | position: 1
3 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.6.3/api/plugins/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Plugins
2 | position: 2
3 | link:
4 |   type: doc
5 |   id: api/plugins/plugins-overview # Dogfood using a "qualified id"
6 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.6.3/api/themes/_category_.yml:
--------------------------------------------------------------------------------
1 | label: Themes
2 | position: 3
3 | link:
4 |   type: doc
5 |   id: themes-overview # Dogfood using a "local id"
6 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.6.3/api/themes/theme-live-codeblock.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 3
 3 | slug: /api/themes/@docusaurus/theme-live-codeblock
 4 | ---
 5 | 
 6 | # 📦 theme-live-codeblock
 7 | 
 8 | This theme provides a `@theme/CodeBlock` component that is powered by react-live. You can read more on [interactive code editor](../../guides/markdown-features/markdown-features-code-blocks.mdx#interactive-code-editor) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-live-codeblock
12 | ```
13 | 
14 | ### Configuration {#configuration}
15 | 
16 | ```js title="docusaurus.config.js"
17 | export default {
18 |   plugins: ['@docusaurus/theme-live-codeblock'],
19 |   themeConfig: {
20 |     liveCodeBlock: {
21 |       /**
22 |        * The position of the live playground, above or under the editor
23 |        * Possible values: "top" | "bottom"
24 |        */
25 |       playgroundPosition: 'bottom',
26 |     },
27 |   },
28 | };
29 | ```
30 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.6.3/api/themes/theme-mermaid.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 5
 3 | slug: /api/themes/@docusaurus/theme-mermaid
 4 | ---
 5 | 
 6 | # 📦 theme-mermaid
 7 | 
 8 | This theme provides a `@theme/Mermaid` component that is powered by [mermaid](https://mermaid-js.github.io/). You can read more on [diagrams](../../guides/markdown-features/markdown-features-diagrams.mdx) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-mermaid
12 | ```
13 | 
14 | ## Configuration {#configuration}
15 | 
16 | ```js title="docusaurus.config.js"
17 | export default {
18 |   themes: ['@docusaurus/theme-mermaid'],
19 |   // In order for Mermaid code blocks in Markdown to work,
20 |   // you also need to enable the Remark plugin with this option
21 |   markdown: {
22 |     mermaid: true,
23 |   },
24 | };
25 | ```
26 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.6.3/api/themes/theme-search-algolia.mdx:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_position: 4
 3 | slug: /api/themes/@docusaurus/theme-search-algolia
 4 | ---
 5 | 
 6 | # 📦 theme-search-algolia
 7 | 
 8 | This theme provides a `@theme/SearchBar` component that integrates with Algolia DocSearch easily. Combined with `@docusaurus/theme-classic`, it provides a very easy search integration. You can read more on [search](../../search.mdx) documentation.
 9 | 
10 | ```bash npm2yarn
11 | npm install --save @docusaurus/theme-search-algolia
12 | ```
13 | 
14 | This theme also adds search page available at `/search` (as swizzlable `SearchPage` component) path with OpenSearch support. You can change this default path via `themeConfig.algolia.searchPagePath`. Use `false` to disable search page.
15 | 
16 | :::tip
17 | 
18 | If you have installed `@docusaurus/preset-classic`, you don't need to install it as a dependency.
19 | 
20 | :::
21 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.6.3/assets/docusaurus-asset-example-banner.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.6.3/assets/docusaurus-asset-example.docx


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.6.3/assets/docusaurus-asset-example.xyz:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/facebook/docusaurus/main/website/versioned_docs/version-3.6.3/assets/docusaurus-asset-example.xyz


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.6.3/guides/markdown-features/_markdown-partial-example.mdx:
--------------------------------------------------------------------------------
1 | <span>Hello {props.name}</span>
2 | 
3 | This is text some content from `_markdown-partial-example.md`.
4 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.6.3/guides/markdown-features/markdown-features-react.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .wrappingBlock {
 9 |   width: 50%;
10 |   display: inline-block;
11 |   padding: 5px;
12 |   vertical-align: top;
13 | }
14 | 
15 | .wrappingBlock code[class^='codeBlockLines'] {
16 |   white-space: pre-wrap;
17 | }
18 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.6.3/guides/markdown-features/markdown-features-tabs-styles.module.css:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | .red {
 9 |   color: red;
10 | }
11 | 
12 | .red[aria-selected='true'] {
13 |   border-bottom-color: red;
14 | }
15 | 
16 | .orange {
17 |   color: orange;
18 | }
19 | 
20 | .orange[aria-selected='true'] {
21 |   border-bottom-color: orange;
22 | }
23 | 
24 | .yellow {
25 |   color: yellow;
26 | }
27 | 
28 | .yellow[aria-selected='true'] {
29 |   border-bottom-color: yellow;
30 | }
31 | 


--------------------------------------------------------------------------------
/website/versioned_docs/version-3.6.3/playground.mdx:
--------------------------------------------------------------------------------
 1 | # Playground
 2 | 
 3 | Playgrounds allow you to run Docusaurus **in your browser, without installing anything**!
 4 | 
 5 | They are mostly useful for:
 6 | 
 7 | - Testing Docusaurus
 8 | - Reporting bugs
 9 | 
10 | Use [docusaurus.new](https://docusaurus.new) as an easy-to-remember shortcut.
11 | 
12 | Choose one of the available options below.
13 | 
14 | ```mdx-code-block
15 | import {PlaygroundCardsRow} from '@site/src/components/Playground';
16 | 
17 | <PlaygroundCardsRow />
18 | ```
19 | 
20 | :::tip
21 | 
22 | For convenience, we'll remember your choice next time you visit [docusaurus.new](https://docusaurus.new).
23 | 
24 | :::
25 | 


--------------------------------------------------------------------------------
/website/versions.d.json.ts:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | declare const versions: string[];
 9 | 
10 | export default versions;
11 | 


--------------------------------------------------------------------------------
/website/versions.json:
--------------------------------------------------------------------------------
 1 | [
 2 |   "3.6.3",
 3 |   "3.5.2",
 4 |   "3.4.0",
 5 |   "3.3.2",
 6 |   "3.2.1",
 7 |   "3.1.1",
 8 |   "3.0.1",
 9 |   "2.x"
10 | ]
11 | 


--------------------------------------------------------------------------------
/website/versionsArchived.d.json.ts:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Copyright (c) Facebook, Inc. and its affiliates.
 3 |  *
 4 |  * This source code is licensed under the MIT license found in the
 5 |  * LICENSE file in the root directory of this source tree.
 6 |  */
 7 | 
 8 | declare const versionsArchived: {[key: string]: string};
 9 | 
10 | export default versionsArchived;
11 | 


--------------------------------------------------------------------------------
/website/versionsArchived.json:
--------------------------------------------------------------------------------
1 | {
2 |   "2.3.1": "https://docusaurus-archive-october-2023.netlify.app/docs/2.3.1",
3 |   "2.2.0": "https://docusaurus-archive-october-2023.netlify.app/docs/2.2.0",
4 |   "2.1.0": "https://docusaurus-archive-october-2023.netlify.app/docs/2.1.0",
5 |   "2.0.1": "https://docusaurus-archive-october-2023.netlify.app/docs/2.0.1"
6 | }
7 |