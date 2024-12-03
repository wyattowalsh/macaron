import type { LoadContext, Plugin } from '@docusaurus/types';
import * as path from 'node:path';

export default function webpackPlugin(context: LoadContext): Plugin<void> {
  return {
    name: 'docusaurus-plugin-webpack',
    configureWebpack(config, isServer, utils) {
      return {
        resolve: {
          alias: {
            '@': path.resolve(context.siteDir, './src'),
            '@/lib': path.resolve(context.siteDir, './src/lib'),
            '@/components': path.resolve(context.siteDir, './src/components'),
            '@/ui': path.resolve(context.siteDir, './src/components/ui'),
          },
        },
      };
    },
  };
}
