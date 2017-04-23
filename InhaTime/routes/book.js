var express = require('express');
var router = express.Router();

var models = require('../models');

router.get('/', function(req, res, next) {
  //res.render('book', { title: 'book' });
  var data;
  models.book.findAll({
        //where: {id: 1}
        //attributes: ['name']
  }).then(function(results){
    res.send(results[0]);
    //console.log('Book: ', result.name);
  }).catch(function(err){
    next(1005);
  });
});


// *****update******
//
// models.Publisher.update({name: newName},
//  {where: {pub_id: pub_id}, returning: true}).then(function(result) {
//       res.json(result[1][0]);
//  }).catch(function(err) {
//       //TODO: error handling
//  });

// ***delete***
// models.Publisher.destroy({where: {pub_id: pub_id}}).then(function(result) {
//     res.json({});
// }).catch(function(err) {
//     //TODO: error handling
// });


module.exports = router;
