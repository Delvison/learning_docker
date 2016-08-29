// app/models/entry.js

var mongoose     = require('mongoose');
var Schema        = mongoose.Schema;

var OrderSchema   = new Schema({
    customer: String,
    // phone_number: String,
    order: String
    // time_placed: String,
    // was_delivered: Boolean
});

module.exports = mongoose.model('Order', OrderSchema);
