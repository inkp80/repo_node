var express = require('express');
var router = express.Router();
var models = require('../models');

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('insert data to user_core');
  models.usercore.create({
    id : 'asd11'
    , gems : '123'
    , coins : '123'
    , hearts : '123'
    , highScore : '123'
  });
  models.book.create({
    name : 'Operating System'
  });
});

/* POST 사용자 아이디를 등록할 때 사용한다. */
router.get('/add/:userID', function (req, res) {
    res.send('nonono');
    models.book.create({
      id : 'Operating System'
    });
});

module.exports = router;
