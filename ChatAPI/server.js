
var express = require('express');


var app = express();
var http = require('http').Server(app);



var io = require('socket.io')(http);
var XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest;

// creating an instance of XMLHttpRequest
var xhttp = new XMLHttpRequest();
var users = {};
// host of the server
var host = 'localhost';
var port = '8000';

io.sockets.on('connection', function (socket) {
    
    console.log("created a socket with id",String(socket.id));
    
    socket.on('disconnect', function() { 
        delete users[String(socket.id)];
        console.log("disconnected...id ",String(socket.id));
        socket.broadcast.emit('display_active',users);
    });
    });



// when a connection happens (client enters on the website)
io.on('connection', function(socket) {

    
    socket.on('active',function(user_info){
        console.log("current users dictionary...");
        users[String(socket.id)] = { 'name':user_info['name'],'img':user_info['img'] };
        for (var key in users){
            console.log(String(key)," : ",users[key]);
        }
        io.emit('display_active',users);
    });


    // socket for getting a message

    socket.on('message', function(msgObject) {
        console.log("got a post");
        // emits the msgObject to the client
        socket.broadcast.emit('getMessage', msgObject);

        // url of the view that will process
        var url = 'http://' + host +':' + port + '/chat/save_message/';

        // when the request finishes
        xhttp.onreadystatechange = function() {
            // it checks if the request was succeeded
            if(this.readyState === 4 && this.status === 200) {
                // if the value returned from the view is error
                if(xhttp.responseText === "error")
                    console.log("error saving message");
                // if the value returned from the view is success
                else if(xhttp.responseText === "success")
                    console.log("the message was posted successfully");
            }
        };

        // prepares to send
        xhttp.open('POST', url, true);
        xhttp.send(JSON.stringify(msgObject));
    });

    socket.on('wikisearch',function(queryObject){
        var url = 'http://' + host +':' + port + '/user_panel/chatbot/';    
        xhttp.onreadystatechange = function() {
            // it checks if the request was succeeded
            if(this.readyState === 4 && this.status === 200) {
                // if the value returned from the view is error
                var result = JSON.parse(xhttp.responseText);
                console.log(result['url']);
                
                   socket.emit('results',result);
                
                   
            }
        };

        xhttp.open('POST', url, true);
        // sends the data to the view
        xhttp.send(JSON.stringify(queryObject));

    });

});

http.listen(8000, function () {
  console.log('listening on *:3000');
});
