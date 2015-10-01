var express = require('express');
var bodyParser = require('body-parser');
var request = require('request');
var async = require('async');

var app = express(); // initialize app
app.use(bodyParser.urlencoded({ extended: false })); // need to add the ability to encode post urls

// keep track of the current vm process
// [{ "name": name, "ip": ip}]
var VMS = [
	{
		"name": "VM1",
		"ip": "http://localhost:8080/"
	}
]

// to change based on load
var currentVM = VMS[0].ip;

// check if alive
app.get('/', function(req, res){
	res.send(200);
});

// the url to redirect to
app.post('/checkForPrimes', function(req, res){
	var n = req.body.number;
	async.series([
		function(cb){
			// request that the current set VM run the check for primes
			request( currentVM + "checkForPrimes/" + n, function (error, response, body) {
			  if (!error && response.statusCode == 200) {
			    	console.log("IS PRIEM");
			    	var data = JSON.parse(body);
			    	cb(null, data.isPrime);
			  }else{
			  		console.log(error);
			  		cb(error, null);
			  }
			});
		}],
		function(err, results){
			if(err) res.sendStatus(400);
			console.log(results[0]);
			res.json({"isPrime": results[0]});
	});
	

});

app.listen(8888);
