import type { LoadContext, Plugin } from '@docusaurus/types';
import * as path from 'node:path';

export default function webpackPlugin(context: LoadContext): Plugin<void> {
  return {
    name: 'docusaurus-plugin-webpack',
    configureWebpack(config, isServer, utils) {
      return {
        resolve: {
          modules: [
            path.resolve(context.siteDir, 'src'),
            'node_modules'
          ],
          extensions: ['.js', '.jsx', '.ts', '.tsx', '.json'],
        },
      };
    },
  };
}
