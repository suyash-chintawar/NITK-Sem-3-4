var express = require('express');
var router = express.Router();
module.exports = router;
var bodyParser = require('body-parser');

var urlencodedParser = bodyParser.urlencoded({extended:false});

router.get('/',function (req,res) {
	res.render('web-app');
});

router.get('/home',function (req,res) {
	res.render('web-app');
});

router.get('/login',function (req,res) {
	res.render('login_page');
});

router.get('/signup',function (req,res) {
	res.render('signup_page');
});

router.get('/demo',function (req,res) {
	res.render('demo');
});

router.get('/search',function (req,res) {
	res.render('product_search');
});

router.post('/login',function (req,res) {
	res.render('demo');
});

router.post('/signup',function (req,res) {
	res.render('demo');
});

router.post('/demo', urlencodedParser, function (req,res) {
	res.render('demo_success',{data: req.body});
});
