const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const spawn = require("child_process").spawn;

const port = process.env.PORT || 5000;
app.use(express.json());

const Data = require("./models/product");
const User = require("./models/userinfo");

const mongoUI = "mongodb+srv://spend:wise@spendwisedata-gaqmj.mongodb.net/Datas";
mongoose.connect(mongoUI, {useNewUrlParser: true, useUnifiedTopology: true},(err) => {
    if (err) console.log(err);
    else {
        console.log("mongo connected!");
    }
const db = mongoose.connection;
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

app.post("/newuserproduct", (req, res) => {
    console.log(req.body);
    User.findOneAndUpdate({username: req.body.username}, {
        username: req.body.username,
        password: req.body.password,
        $push: {purchases: req.body.product}
    }, {upsert: true, useFindAndModify: false}, (err) => {
        if (err) {
            return res.status(500).send(err);
        }
        res.status(200).send("upload worked");
    });
})

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
    const pythonProcess = spawn("python", ["./dummy.py", url]);
    pythonProcess.stdout.on("data", (data) => {
        console.log("Python is being executed!");
        console.log(data.toString());
        //Finds the correct file
        Data.findOne({ean: data}, (err, document) => {
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