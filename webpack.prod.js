var path = require("path");
var webpack = require("webpack");
var base = require("./webpack.base.js");
var BundleTracker = require("webpack-bundle-tracker");
var MiniCssExtractPlugin = require("mini-css-extract-plugin");


base[0].mode = "production";
base[1].mode = "production";

base[0].output = {
  path: path.resolve("./assets/js/min/"),
  filename: "[name].[contentHash].js"
};
base[1].output = {
  path: path.resolve("./assets/css/min/"),
  filename: "[name].[contentHash].js"
};

base[1].optimization = { minimize: true };

base[1].plugins = [
  new MiniCssExtractPlugin({ filename: "[name]-[hash].css", disable: false, allChunks: true }),
  new BundleTracker({
    filename: "./webpack-stats.json"
  }),

];

module.exports = base;
