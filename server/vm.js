var express = require('express');
var bodyParser = require('body-parser');
var os  = require('os-utils');
var async = require('async');

var app = express(); // initialize app
app.use(bodyParser.urlencoded({ extended: false }));

// check if alive
app.get('/getLoad', function(req, res){
	// get the cpu in series so that to return thre correct value
	async.series([
			function(cb){
				os.cpuUsage(function(v){
					cb(null, v);
				})
			}
		],
		function(err, results){
			if(err) res.send(400);

			// return the cpuUsage - cpu load
			res.json({"load": results[0]});
		});
});

// the url to redirect to
app.get('/checkForPrimes/:number', function(req, res){
	var n = req.params.number;
	console.log(n);
	var isPrime = checkForPrimes(n);
	res.json({"isPrime": isPrime});
});

// check if n is a prime number
var checkForPrimes = function(n){
	if(n < 0) return false;
	if(n <= 3) return true;
	if(n % 2 == 0) return false;
	if(n % 3 == 0) return false;

	var i = 5;
	var w = 2;

	while(i * i <= n){
		
		if(n % i == 0)
			return false;

		i += w;
		w = 6 - w;
	}

	return true;
}

app.listen(8080);
