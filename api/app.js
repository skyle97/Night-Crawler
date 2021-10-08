const { json } = require('body-parser');
const express = require('express');
const mongoose = require('mongoose');
const Device = require('./models/devices');
const  device_router = require('./routes/devices');

const app = express();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

var url = 'mongodb://localhost:27017/IOT'

mongoose.connect(url, {useUnifiedTopology: true, useNewUrlParser: true }).then(() => console.log('Connection to database IOT OK')).catch(error => console.log(error));

app.listen(3000, function() {
    console.log("Server running on port 3000")
})

app.use('/',device_router)
