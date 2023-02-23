const path = require('path');

module.exports = {
    mode: "development",
    entry: {
        app: './src/index.js'
    },
    watch: true,
    devtool: 'source-map',
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, '../../static/react/moviesite')
    },

    resolve: {
      alias: {
        components: path.resolve(__dirname, 'src/components')
      },
      extensions: ['.js', '.jsx']
    },

    module: {
        rules: [
          {
            test: /\.(js|jsx)$/,
            exclude: /(node_modules|bower_components)/,
            use: {
                loader: 'babel-loader',
                options: {
                  presets: ['@babel/preset-env']
                }
            }
          }, {
            test: /\.css$/,
            use: ["style-loader", "css-loader"]
          }
        ]
    },
    externals : {
        'react': 'React',
        'react-dom' : 'ReactDOM'
    },
    optimization: {
        minimize: true,
    }
    
}