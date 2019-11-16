const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const port = process.env.PORT || 5000;
app.use(express.json());

const Data = require("./models/product");

const mongoUI = "mongodb+srv://spend:wise@spendwisedata-gaqmj.mongodb.net/Datas";
mongoose.connect(mongoUI, {useNewUrlParser: true, useUnifiedTopology: true},(err) => {
    if (err) console.log(err);
    else {
        console.log("mongo connected!");
    }
const db = mongoose.connection;
});

app.post("/newdata", (req, res) => {
    const data = req.body;
    console.log(data);
    //console.log(req.body);
    Data.findOneAndUpdate({ean: req.body.ean}, {
        name: req.body.name,
        ean: req.body.ean,
        price: req.body.price,
        usage: req.body.usage,
        co2: req.body.co2,
        photo: req.body.photo
    }, {upsert: true, useFindAndModify: false}, (err) => {
        if (err) {
            return res.status(500).send(err);
        }
        res.status(200).send("upload worked");
    });
});

app.post("/getinfo", (req, res) => {
    console.log(req.body);
    Data.findOne({ean: req.body.ean}, (err, document) => {
        if (err) {
            console.log("ean can't be found!");
            res.status(500).send(err);
        }
        console.log("document was found");
        res.status(200).send(document);
    });
});

app.get("/", (req, res) => {
    console.log("homepage");
    res.send("hello ttttthere");
});

app.listen(port, () => console.log(`Listening to port number ${port}`));
module.exports = app;