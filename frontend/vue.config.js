module.exports = {
  devServer: {
    host: "127.0.0.1",
    port: 8081,
  },
  chainWebpack: (config) => {
    config.plugin("copy").tap((args) => {
      const patterns = args[0].patterns || args[0];

      patterns.forEach((pattern) => {
        const currentIgnore = pattern.globOptions?.ignore || [];
        pattern.globOptions = {
          ...(pattern.globOptions || {}),
          ignore: [...currentIgnore, "**/index.html"],
        };
      });

      return args;
    });
  },
};
