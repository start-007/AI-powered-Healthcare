
window.onload = () => {
  const button = document.getElementById('button');
  var value="";
  var flag=0;
  button.addEventListener('click', () => {
    if (button.style['animation-name'] === 'flash') {
      recognition.stop();
      console.log(value);
      onStopButton(value);
      value="";
      button.style['animation-name'] = 'none';
      button.innerText = 'Press to Start';
      content.innerText = '';
    } else {
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