// server.js
var express    = require('express');
var app        = express();
var bodyParser = require('body-parser');

// setup bodyparser
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// set up connection to mongodb
// var mongoose   = require('mongoose');
// mongoose.connect('mongodb://node:node@novus.modulusmongo.net:27017/Iganiq8o'); // connect to our database

// set up port
var port = process.env.PORT || 3000;

// import Order model
var Order       = require('./models/order');

// get an instance of the express Router
var router = express.Router();

// middleware to use for all requests
router.use(function(req, res, next) {
    // do logging
    console.log("+ "+req.ip+" - "+req.headers['user-agent']);
    next(); // make sure we go to the next routes and don't stop here
});

// test route to make sure everything is working (accessed at GET http://localhost:8080/api)
router.get('/', function(req, res) {
    res.json({ message: 'hooray! welcome to our api!' });
});

// more routes for our API will happen here

router.route('/orders')

    // create an order
    .post(function(req, res) {
      var order = new Order();
      order.customer = req.body.customer;
      order.order = req.body.order;
      console.log("   RECEIVING ORDER > "+order.customer+" : "+order.order);
      // order.save(function(err) {
      //   if (err)
      //     console.log(err);
      //   res.json({ message: 'Order placed!' });
      // });
      res.json({ message: 'Order placed!' });

    })

    // GET all orders
    .get(function(req,res) {
      console.log("   REQUESTED ALL ORDERS");
      // Order.find(function(err, orders) {
      //   if (err)
      //     res.send(err);
      //   res.json(orders);
      // });
      res.json({ orders: 'some orders' });
    });



router.route('/orders/:order_id')

    .get(function(req, res){
      console.log("   REQUESTED ORDER > "+req.params.order_id);
      // Order.findById(req.params.order_id, function(err, order) {
      //   if (err)
      //     res.send(err);
      //   res.json(order);
      // });
      res.json({ order: 'some order' });
    })

    .put(function(req, res){
      console.log("   UPDATING ORDER > "+req.params.order_id+" : "+req.body.customer+" : "+req.body.order);
      // Order.findById(req.params.order_id, function(err, order) {
      //   if (err)
      //     res.send(err);
      //   order.customer = req.body.customer;
      //   order.order = req.body.order;
      // })
      // // save the order
      // order.save(function(err) {
      //   if (err)
      //     res.send(err);
      //   res.json({ message: 'Order updated!' });
      // });
      res.json({ message: 'Order updated!' });
    })

    .delete(function(req, res){
      console.log("   DELETING ORDER > "+req.params.order_id);
      // Order.remove({
      //   _id: req.params.order_id
      // }, function(err, order) {
      //   if (err)
      //     res.send(err);
      //   res.json({ message: 'Successfully deleted' });
      // });
      res.json({ message: 'Successfully deleted' });
    });

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api
app.use('/api', router);

// START THE SERVER
// =============================================================================
app.listen(port);
console.log('Running on port ' + port);
