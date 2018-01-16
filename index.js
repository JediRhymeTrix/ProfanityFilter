const express = require('express');
const app = express();
const PythonShell = require('python-shell');
const bodyParser= require('body-parser')

app.use(bodyParser.urlencoded({extended: true}))
app.use(bodyParser.json())

app.listen(4000, function () {
    console.log('server running');
});

app.post('/filter', function(req, res) {
    console.log('filter: POST');

    var pyshell = new PythonShell('ProfanityFilter.py');
    pyshell.send(req.body.text);

    pyshell.on('message', function (words) {
        res.send(words);
    });
});