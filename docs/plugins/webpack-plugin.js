module.exports = function (context, options) {
  return {
    name: 'webpack-plugin',
    configureWebpack(config, isServer, utils) {
      return {
        resolve: {
          alias: {
            '@': require('path').resolve(__dirname, '../src'),
          },
        },
      };
    },
  };
};
