var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,
  entry: './apfelschuss/static-src/js/index',
  output: {
      path: path.resolve('./apfelschuss/static/'),
      filename: "[name]-[hash].js"
  },

  plugins: [
    new BundleTracker({filename: './apfelschuss/static-src/webpack-stats.json'})
  ]
}
