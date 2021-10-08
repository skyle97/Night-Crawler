const mongoose = require('mongoose');

device_schema = new mongoose.Schema({
      ip: {type: String},
      ports: {type: Array},
      services: {type: Array},
      banners: {type: Array},
      date: {type: String},
      screenshot: {type: String},
      geo: {type: Object}
    })

module.exports = mongoose.model('Device',device_schema)

