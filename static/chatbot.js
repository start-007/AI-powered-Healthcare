class Chatbox {
  constructor() {
      this.args = {
          openButton: document.querySelector('.chatbox__button'),
          chatBox: document.querySelector('.chatbox__support'),
          sendButton: document.querySelector('.send__button'),
          arrow:document.querySelector(".arrow1")
         
      }
      
    this.state = false;
    this.messages = [];
    this.flag=0;
    
  }

  display() {
        
      const {openButton, chatBox, sendButton} = this.args;

      openButton.addEventListener('click', () => this.toggleState(chatBox))
      
     
      sendButton.addEventListener('click', () => this.onSendButton(chatBox))

      const node = chatBox.querySelector('input');
      node.addEventListener("keyup", ({key}) => {
          if (key === "Enter") {
              this.onSendButton(chatBox)
          }
      })
  }

  toggleState(chatbox) {
      this.state = !this.state;

      // show or hides the box
      if(this.state) {
        chatbox.classList.add('chatbox--active');
          if(this.flag==0){
            
            const msg={ name: "ME", message: "Hey there who please fill the below form before we even start our conversation." }
            this.messages.push(msg);
            this.updateChatText(chatbox);
            this.flag=1;

          }
            
     
      } else {
          chatbox.classList.remove('chatbox--active')
       
      }
  }
    

  onSendButton(chatbox) {
      var textField = chatbox.querySelector('input');
      let text1 = textField.value
      if (text1 === "") {
          return;
      }

      let msg1 = { name: "User", message: text1 }
      this.messages.push(msg1);

      fetch($SCRIPT_ROOT+'/predict', {
          method: 'POST',
          body: JSON.stringify({ message: text1 }),
          mode: 'cors',
          headers: {
            'Content-Type': 'application/json'
          },
        })
        .then(r => r.json())
        .then(r => {
          let msg2 = { name: "ME", message: r.answer };
          this.messages.push(msg2);
          this.updateChatText(chatbox)
          textField.value = ''

      }).catch((error) => {
          console.error('Error:', error);
          this.updateChatText(chatbox)
          textField.value = ''
        });
  }

  updateChatText(chatbox) {
      var html = '';
      this.messages.slice().reverse().forEach(function(item, index) {
          if (item.name === "ME")
          {
              html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
          }
          else
          {
              html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
          }
        });

      const chatmessage = chatbox.querySelector('.chatbox__messages');
      chatmessage.innerHTML = html;
  }
}


const chatbox = new Chatbox();
chatbox.display();

const $icon = document.querySelector('.icon');
const $arrow = document.querySelector('.arrow');
$arrow.animate([
    {left: '0'},
    {left: '10px'},
    {left: '0'}
],{
    duration: 700,
    iterations: Infinity
});

