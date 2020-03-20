var path = require("path");
var webpack = require("webpack");
var base = require("./webpack.base.js");
var BundleTracker = require("webpack-bundle-tracker");

base[0].mode = "development";
base[1].mode = "development";

base[0].output = {
  path: path.resolve("./assets/js/min/"),
  filename: "[name].js"
};
base[1].output = {
  path: path.resolve("./assets/css/min/"),
  filename: "[name].js",
};

base[1].plugins = [
  new BundleTracker({
    filename: "./webpack-stats.json"
  })
];

module.exports = base;
