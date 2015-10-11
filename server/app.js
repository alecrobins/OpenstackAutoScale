/**
 *  Cloud Computing
 *  Assignment 1
 *  Alec Robins
 *
 * This is the second teir of the auto scaler
 * This server's role is to relay calls from the client
 *   to the correct VM and return info about the VMs
 *
 */

var express = require('express');
var bodyParser = require('body-parser');
var request = require('request');
var async = require('async');

var app = express(); // initialize app
app.use(bodyParser.urlencoded({ extended: false })); // need to add the ability to encode post urls

// keep track of the current vm process
// [{ "name": name, "ip": ip}]
var VMS = [];

// TODO: change to correct VM IP's

VMS["VM1"] = 
	{
		"name": "VM1",
		"ip": "http://localhost:8080/"
	};

VMS["VM2"] = 
	{
		"name": "VM1",
		"ip": "http://localhost:8080/"
	};

// return all the virtual machines
app.get('/getVMS', function(req, res){
	res.json(VMS);
});

// return all the virtual machines
app.get('/getLoad/:vmID', function(req, res){
	var vmID = req.params.vmID;

	async.series([
		function(cb){
			// request that the current set VM run the check for primes
			request( VMS[vmID].ip + "getLoad", function (error, response, body) {
			  if (!error && response.statusCode == 200) {
			    	var data = JSON.parse(body);
			    	cb(null, data.load);
			  }else{
			  		console.log(error);
			  		cb(error, null);
			  }
			});
		}],
		function(err, results){
			if(err) res.sendStatus(400);
			res.json({"load": results[0]});
	});
});

// ask a vm to compute the check for primes
app.post('/n', function(req, res){
	var n = req.body.number;
	var currentVM = VMS[req.body.vm];

	async.series([
		function(cb){
			// request that the current set VM run the check for primes
			request( currentVM.ip + "checkForPrimes/" + n, function (error, response, body) {
			  if (!error && response.statusCode == 200) {
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
			res.json({"isPrime": results[0]});
	});
	
});

app.listen(8888);
