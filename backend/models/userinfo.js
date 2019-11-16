const mongoose = require("mongoose");
const Schema = mongoose.Schema;

var UserSchema = new Schema({
    username: {
        type: String,
        required: true
    },
    ean: {
        type: Number,
        required: true
    },
    buydate: {
        type: Date,
        required: true
    }
});

const BuyModel = mongoose.model("BuyModel", UserSchema);
module.exports = UserModel;