const express = require('express');
const cors = require('cors')
const app = express();
app.use(cors());
var iPortaTcp = 4201;
var sIpAddress = "127.0.0.1"
app.listen(iPortaTcp,sIpAddress, () => console.log('API is running on http://' + sIpAddress +
':' + iPortaTcp));
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));


//pagina di invio della form
app.get('/formRegistrazione', (req, res) => {
console.log("Mi hai chiesto la form di registrazione");
res.sendFile("formsemplice.html", { root: './htdoc' });
});


app.get('/gestiscidatiform', (req, res) => {
    console.log(req.query.fname);
    res.send("<html>  Buonaserata " + req.query.fname + "</html" );
    });