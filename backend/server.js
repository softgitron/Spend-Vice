const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const spawn = require("child_process").spawn;

const port = process.env.PORT || 5000;
app.use(express.json());

const Data = require("./models/product");
const Buy = require("./models/userinfo");

//-----------------------------DATABASE INITIALIZATION--------------
const mongoUsername = process.env["DB_USERNAME"];
const mongoPassword = process.env["DB_PASSWORD"];

if (!mongoUsername  || !mongoPassword) {
    console.log("You must define Mongo databse username and password.\n \
                 Define variables using \
                 'export DB_USERNAME=(user name)' and\n \
                 'export DB_PASSWORD=(user password)'.");
    process.exit(1);
}

const mongoUI = `mongodb+srv://${mongoUsername}:${mongoPassword}@spendwisedata-gaqmj.mongodb.net/Datas`;

mongoose.connect(mongoUI, {useNewUrlParser: true, useUnifiedTopology: true},(err) => {
    if (err) console.log(err);
    else {
        console.log("mongo connected!");
    }
});

//-----------------------------REQUESTS-----------------------------
app.post("/finduserinfo", (req, res) => {
    console.log(req.body);
    User.findOne({username: req.body.username}, (err, document) => {
        if (err) res.status(404).send("Error with search");
        if (document) {
            console.log("user info was found");
            res.status(200).json(document);
        } else {
            console.log("user info was not found");
            res.status(404).send("this username did not provide any information.");
        }
    });
});

app.post("/newpurchase", (req, res) => {
    console.log(req.body);
    let newPurchase = new Buy({
        username: req.body.username,
        ean: req.body.ean,
        buydate: Date.now()
    });
    newPurchase.save((err) => {
        if (err) res.status(500).send(err);
        res.status(200).send("purchase added");
    });
});

app.post("/newdata", (req, res) => {
    console.log(req.body);
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
    const url = req.body.url;
    //Runs the python script that generates the EAN based on the url posted
    console.log("Python3 is being executed!");
    const pythonProcess = spawn("python3", ["../crawler/node_wrapper.py", url]);
    pythonProcess.stdout.on("data", (data) => {
        output = data.toString()
        if (output === "ERROR") {
            res.status(401).send("Error in data extraction");
        }
        responseJson = JSON.parse(output);
        console.log(responseJson);
        productName = responseJson.Name;
        console.log(productName);
        //Finds the correct file
        Data.findOne({name: productName}, (err, document) => {
            if (err) {
                console.log("ean can't be found!");
                res.status(500).send(err);
            }
            if (document) {
                console.log("document was found");
                res.status(200).json(document);
            } else {
                console.log("document was not found");
                res.status(404).send("The product could not be found in the database");
            }
        });
    });
});

app.get("/", (req, res) => {
    console.log("homepage");
    res.send("This is our homepage. Get out!");
});

app.listen(port, () => console.log(`Listening to port number ${port}`));
module.exports = app;