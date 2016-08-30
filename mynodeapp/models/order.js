// app/models/entry.js

var mongoose     = require('mongoose');
var Schema        = mongoose.Schema;

var OrderSchema   = new Schema({
    customer: String,
    order: String,
    phone: String,
    total: String,
    address: String,
    isFulfilled: Boolean
});

module.exports = mongoose.model('Order', OrderSchema);
