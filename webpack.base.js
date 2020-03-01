var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = [{
  entry: './assets/js/script',
  output: {},
  module: {
    rules: [
      { test: /\.jsx?$/, exclude: /node_modules/, loader: 'babel-loader'},
    ],
  },

  resolve: {
    modules: ['node_modules', 'bower_components', path.resolve(__dirname, 'assets/js/'),],
    extensions: ['.js', '.jsx']
  },
  plugins: [
    new webpack.ProvidePlugin({
        $: "jquery",
    }),
]
},{
  context: __dirname,
  entry: './assets/css/style.scss',
  output: {},
  module: {
    rules: [
      {
        test: /\.css$/,
        loaders: [
          'style-loader',
          'css-loader',
        ],
      },
      {
        test: /\.scss$/,
        loaders: [
          'style-loader',
          'css-loader',
          'sass-loader',
        ],
      },
      {
        test: /\.(svg)(\?v=\d+\.\d+\.\d+)?$/,
        loader: 'url-loader?limit=100000',
      },
      {
        test: /\.(jpg|png)?$/,
        loaders: [
          'file-loader?name=i-[hash].[ext]',
        ],
      },
    ]
  }
}]
