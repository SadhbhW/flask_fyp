function draw_body() {
      // [1] GET ALL THE HTML ELEMENTS
      var video = document.getElementById("vid-show"),
              canvas = document.getElementById("vid-canvas"),
              take = document.getElementById("vid-take");

      // [2] ASK FOR USER PERMISSION TO ACCESS CAMERA
      navigator.mediaDevices.getUserMedia({video: true})
              .then(function (stream) {
                // [3] SHOW VIDEO STREAM ON VIDEO TAG
                video.srcObject = stream;
                video.play();

                // [4] WHEN WE CLICK ON "TAKE PHOTO" BUTTON
                take.addEventListener("click", capture_xmit_frame);
    })
              .catch(function (err) {
                document.getElementById("vid-controls").innerHTML = "Please enable access and attach a camera";
              });
    }

function capture_xmit_frame() {

    var video = document.getElementById("vid-show"),
    canvas = document.getElementById("vid-canvas");

    console.log("capture triggered!");
    // Create snapshot from video
    var draw = document.createElement("canvas");
    draw.width = video.videoWidth;
    draw.height = video.videoHeight;
    var context2D = draw.getContext("2d");
    context2D.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);
    // Upload to server
    var data = draw.toDataURL('image/png');
    xmit_frame(data)
    }

    // ajax POST
function xmit_frame(image_data){
      $.ajax({
        url: '/image',
        processData: false,
        type: 'POST',
        data: '{ "imageData" : "' + image_data + '" }',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response){
                console.log(response);
        },
        error: function(error){
        console.log("error");
      }
    });
}
