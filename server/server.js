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



//esempoi---------------------------------------------------


//pagina di invio della form
app.get('/formRegistrazione', (req, res) => {
console.log("Mi hai chiesto la form di registrazione");
res.sendFile("formsemplice.html", { root: './htdoc' });
});


app.post('/gestiscidatiform', (req, res) => {
    console.log(req.body.fname);
    response="<html>  Buonaserata " + req.body.fname + " " + req.body.fcognome + "<br>"+ "</html" ;
    if (req.body.fsesso == "1")
        response += "<br>sei un maschio"
    else
        response += "<br>sei una femmina"

    response += "<br>sei di questa citta " + req.body.fcomune 
    res.send(response);
    });





//esercizio1  sendfile--------------------------------------------

app.get('/sendfile', (req, res) => {
    console.log("Mi hai chiesto la form di registrazione");
    res.sendFile("sendfile.html", { root: './htdoc' });
    });



// gestione urlmansend-----------------------------------------
app.post('/mansendfile', (req, res) => {

    console.log(req.body.password)
    password_ricevuta = req.body.password;

    if(password_ricevuta =="paperino")
        response = "<html>Bravo " + req.body.email + "<br> sono ponto a ricevere il file!, la spassword inserita è"+ req.body.fpassword+ "</html>"
        res.send(response)



    });




//esercizio 2------------------------------------------