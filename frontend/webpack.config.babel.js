import HtmlPlugin from 'html-webpack-plugin'
import VueLoaderPlugin from 'vue-loader/lib/plugin'

export default {
  entry: './main.js',
  output: { filename: 'bundle.js' },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: { compilerOptions: { whitespace: 'condense' } }
      },
      { test: /\.css$/, use: ['vue-style-loader', 'css-loader'] }
    ]
  },
  plugins: [
    new VueLoaderPlugin(),
    new HtmlPlugin({
      templateContent: `
        <!doctype html>
        <html>
          <head>
            <meta name="viewport" content="width=device-width, initial-scale=1"/>
            <title>Moti</title>
          </head>
          <body><div id="vue-main"></div></body>
        </html>`
    })
  ],
  devServer: {
    inline: true,
    port: 80,
    host: '0.0.0.0',
    proxy: { '/api/': 'http://backend:8000' }
  }
}
