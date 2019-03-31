const path = require('path');
const webpack = require("webpack");

module.exports = {
    entry: {
        app: './apfelschuss/static-src/js/index.js'
    },
    plugins: [
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            Util: 'exports-loader?Util!bootstrap/js/dist/util'
        })
    ],
    output: {
        filename: '[name]-[hash].js',
        path: path.resolve(__dirname, './apfelschuss/static/')
    }
};
