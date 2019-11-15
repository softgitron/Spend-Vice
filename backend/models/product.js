const mongoose = require("mongoose");
const Schema = mongoose.Schema;

var DataSchema = new Schema({
    name: {
        type: String,
        required: true
    },
    ean: {
        type: Number,
        required: true
    },
    price: {
        type: Number,
        required: true
    },
    usage: {
        type: Number,
        required: false
    },
    co2: {
        type: Number,
        required: false
    },
    photo: {
        type: String,
        required: false
    }
});

const DataModel = mongoose.model("DataModel", DataSchema);
module.exports = DataModel;