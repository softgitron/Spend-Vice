const mongoose = require("mongoose");
const Schema = mongoose.Schema;

var UserSchema = new Schema({
    username: {
        type: String,
        required: true
    },
    password: {
        type: String,
        required: true
    },
    purchases: {
        type: [Number],
        required: true
    }
});

const UserModel = mongoose.model("UserModel", UserSchema);
module.exports = UserModel;