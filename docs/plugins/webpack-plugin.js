const path = require('path');

module.exports = function (context, options) {
  return {
    name: 'webpack-plugin',
    configureWebpack(config, isServer, utils) {
      return {
        resolve: {
          alias: {
            '@': path.resolve(__dirname, '../src'),
            '@/lib': path.resolve(__dirname, '../src/lib'),
            '@/components': path.resolve(__dirname, '../src/components'),
          },
        },
      };
    },
  };
};
