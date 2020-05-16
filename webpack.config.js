var path = require("path");

module.exports = {
	entry: [],
	output: {
		filename: "index.js",
		path: path.resolve(__dirname, "s4slide/app/static/js")
	},
	module: {
		rules: [
			{
				test: /\.ts$/,
				exclude: /node_modules/,
				loader: "babel-loader",
				options: {
					presets: ["@babel/preset-typescript"]
				}
			}
		]
	}
};
