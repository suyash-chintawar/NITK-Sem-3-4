var express = require('express');
var app = express();

var controller = require('./controller/controller');

app.set('view engine','ejs');
app.use(express.static(__dirname+'/public'));

app.set('views',(__dirname+ '/views'));

app.use('/',controller);
app.use('/home',controller);
app.use('/login',controller);
app.use('/signup',controller);
app.use('/demo',controller);
app.use('/search',controller);

app.listen(3000);
console.log('connected..go to 127.0.0.1:3000/ in your browser');