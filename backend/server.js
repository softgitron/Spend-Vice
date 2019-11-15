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
});

app.post("/newdata", (req, res) => {
    console.log("yolo");
});

app.post("/getinfo", (req, res) => {
    const data = req.body;
    console.log(data);
    console.log(req.body.this);
    res.status(200).json();
});

app.get("/", (req, res) => {
    console.log("homepage");
    res.send("hello ttttthere");
});

app.listen(port, () => console.log(`Listening to port number ${port}`));