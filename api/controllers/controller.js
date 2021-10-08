const Device = require('../models/devices');

var controller = {
    search: function (req, res) {
        Device.find({ ports: 21 }).exec(function (error, device){
            if (error) {
                res.send('Failed to send data')
            } else {
                return res.status(200).send(device)
            }
        })
    }
}
module.exports = controller;
