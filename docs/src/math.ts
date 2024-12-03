export const katexConfig = {
  stylesheets: [
    {
      href: 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css',
      integrity: 'sha384-nB0miv6/jRmo5UMMR1wu3Gz6NLsoTkbqJghGIsx//Rlm+ZU03BU6SQNC66uf4l5+',
      crossorigin: 'anonymous',
    },
  ],
  scripts: [
    {
      src: 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js',
      integrity: 'sha384-7zkQWkzuo3B5mTepMUcHkMB5jZaolc2xDwL6VFqjFALcbeS9Ggm/Yr2r3Dy4lfFg',
      crossorigin: 'anonymous',
      defer: true,
    },
    {
      src: 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js',
      integrity: 'sha384-43gviWU0YVjaDtb/GhzOouOXtZMP/7XUzwPTstBeZFe/+rCMvRwr4yROQP43s0Xk',
      crossorigin: 'anonymous',
      defer: true,
      onload: 'renderMathInElement(document.body);',
    },
    {
      src: 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/mathtex-script-type.min.js',
      integrity: 'sha384-OGHJvxKrLNowXjZcg7A8ziPZctl4h7FncefPoKSuxgVXFxeM87GCKFJvOaTeBB9q',
      crossorigin: 'anonymous',
      defer: true,
    },
    {
      src: 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/copy-tex.min.js',
      integrity: 'sha384-HORx6nWi8j5/mYA+y57/9/CZc5z8HnEw4WUZWy5yOn9ToKBv1l58vJaufFAn9Zzi',
      crossorigin: 'anonymous',
    },
  ],
};
