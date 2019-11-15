const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const port = process.env.PORT || 5000;
app.use(express.json());

const mongoUI = "mongodb+srv://spend:wise@spendwisedata-gaqmj.mongodb.net/Datas";
mongoose.connect(mongoUI, {useNewUrlParser: true, useUnifiedTopology: true},(err) => {
    if (err) console.log(err);
    else {
        console.log("mongo connected!");
    }
});

app.post("/getinfo", (req, res) => {
    const data = res.json(req.body);
    console.log(data.body.name);
    res.status(200).send(res);
});

app.get("/", (req, res) => {
    console.log("homepage");
    res.send("hello there");
});

app.listen(port, () => console.log(`Listening to port number ${port}`));