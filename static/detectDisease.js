window.onload =()=>{
  
  var divs=document.querySelectorAll(".symptom");
  var list=[];
  var symptomList=[
    'shivering', 'joint_pain', 'ulcers_on_tongue', 'spotting_ urination', 'weight_loss', 'patches_in_throat', 'nausea', 'back_pain', 'constipation', 'diarrhoea', 'mild_fever', 'yellowing_of_eyes', 'sinus_pressure', 'neck_pain', 'swollen_extremeties', 'slurred_speech', 'hip_joint_pain', 'movement_stiffness', 'unsteadiness', 'continuous_feel_of_urine', 'internal_itching', 'depression', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'polyuria', 'family_history', 'rusty_sputum', 'lack_of_concentration', 'receiving_unsterile_injections', 'coma', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'pus_filled_pimples', 'silver_like_dusting', 'yellow_crust_ooze'
  ]
  addDivs(symptomList);
  toggle=()=>{
  
    $(".symptom").click(function () {
      $(this).toggleClass("selected");
      const symptom=$(this).html()
      if($(this).attr("class").split(/\s+/).includes("selected")===true && list.includes(symptom)===false){
        list.push(symptom);
      }
      else{
        const index = list.indexOf(symptom);
        if (index > -1) {
          list.splice(index, 1); // 2nd parameter means remove one item only
        }
      }
      return list;
      
    });
  }
  toggle();
  $("button").click(()=>{
    onClickButton(list)
  })
  
  

}


addDivs=(symptomList)=>{
  var mainDiv=document.getElementById("symptomList");
  for(var i=0;i<symptomList.length;++i){
    var div = document.createElement('div');
    div.innerHTML=symptomList[i];
    div.className = 'symptom';
    div.name=symptomList[i];
    
    mainDiv.appendChild(div);
  }
  
}
onClickButton=(arr)=> {
  
  

  fetch($SCRIPT_ROOT+'/detect-disease', {
      method: 'POST',
      body: JSON.stringify({ message: arr }),
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json'
      },
    })
    .then(r => r.json())
    .then(r => {
      
      document.querySelector("h2").innerHTML="Your are suffering from: "+r.answer;

  }).catch((error) => {
      console.error('Error:', error);
      
    });
}