
window.onload = () => {
  const button = document.getElementById('button');
  var value="";
  var flag=0;
  
 
  button.addEventListener('click', () => {
    if (button.style['animation-name'] === 'flash') {
      recognition.stop();
      console.log(value);
      onStopButton(value);
      testCanvas(0);
      
      value="";
      button.style['animation-name'] = 'none';
      button.innerText = 'Press to Start';
      content.innerText = '';
    } else {
      testCanvas(1);
      button.style['animation-name'] = 'flash';
      button.innerText = 'Press to Stop';
      console.log("started");
      recognition.start();
    }
  });


  const content = document.getElementById('content');

  const recognition = new webkitSpeechRecognition();
  recognition.continuous = true;
  recognition.interimResults = true;
  
  recognition.onresult = function (event) {
    let result=""
    for (let i = event.resultIndex; i < event.results.length; i++) {
      result += event.results[i][0].transcript;
    }
    content.innerText = result;
    value=result;
  };
  
};

function onStopButton(text1) {
  

  if(text1=="") return;
  var msg=fetch($SCRIPT_ROOT+'/predict', {
      method: 'POST',
      body: JSON.stringify({ message: text1 }),
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json'
      },
    })
    .then(r => r.json())
    .then(r => {
      
      window.speechSynthesis.speak(new SpeechSynthesisUtterance(r.answer));

    })
    .catch((error) => {
      console.error('Error:', error);
      
    });

}


const testCanvas=(test)=>{
  var canvas=document.querySelector("canvas");
  //var drawVisual = requestAnimationFrame(testCanvas);
  var canvasCtx = canvas.getContext("2d");
  if(test===0){
    canvasCtx.clearRect(0, 0,canvas.width, canvas.height);
    canvasCtx.beginPath();
    
    canvasCtx.fillStyle = "rgba(0, 0, 0, 255)";
    canvasCtx.fillRect(0, 0, canvas.width, canvas.height);    
    canvasCtx.stroke();
    return;
  }
  
  var drawVisual = requestAnimationFrame(testCanvas);
  var WIDTH=1000;
  var HEIGHT=1000;
  var bufferLength=10;
  canvasCtx.clearRect(0, 0,canvas.width, canvas.height);
  canvasCtx.fillStyle = 'rgb(200, 200, 200)';
  canvasCtx.fillRect(0, 0, WIDTH, HEIGHT);
  canvasCtx.lineWidth = 2;
  canvasCtx.strokeStyle = 'rgb(0, 0, 0)'; 
  canvasCtx.beginPath();
  var sliceWidth = WIDTH * 1.0 / bufferLength;
  var x = 0;
  for(var i = 0; i < bufferLength; i++) {

    var v = (Math.floor(Math.random() * 50)+10)/ 128.0;
    var y = v * HEIGHT/2;

    if(i === 0) {
      canvasCtx.moveTo(x, y);
    } else {
      canvasCtx.lineTo(x, y);
    }
   
    x += sliceWidth;
  }
  canvasCtx.lineTo(canvas.width, canvas.height/2);
  canvasCtx.stroke();
  //console.log("ok");
}

