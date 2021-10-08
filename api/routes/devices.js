var express = require('express');
var device_controller = require('../controllers/controller');
var router = express.Router();

router.get('/search',device_controller.search);
module.exports = router;


