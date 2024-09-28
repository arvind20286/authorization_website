function handleRegistration(event) {
  event.preventDefault(); // Prevent form submission

  const fullName = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const confirmPassword = document.getElementById('confirmPassword').value;

  if(fullName == '' || email == '' || password == '' || confirmPassword == ''){
    document.getElementById("rejct_reason_messg").innerText = "Please fill all fields!";
    document.getElementById("rejct_reason_messg").classList.remove("d-none");

    return;
  }
  // Validate form fields
  if (password !== confirmPassword) {
      alert("Passwords do not match!");
      return;
  }
  let user_data = {
    name: fullName,
    email: email,
    password: password
  }
  
  // Simulate successful registration (replace with actual backend logic)
  const init = {
    method: "post",
    body: JSON.stringify(user_data),
    headers:{
      "Content-type": "application/json",
    }
    
  }
  fetch(check_registration_url, init).then((response)=>{
    return response.json();
  }).then((data)=>{
    if(data.registration_successful){
      alert(`Registration successful! Welcome, ${fullName}.`);
      window.location.href = welcome_page_url;
    }
    else{
      document.getElementById("rejct_reason_messg").classList.remove("d-none");
      document.getElementById("rejct_reason_messg").innerText = data.rejct_reason_messg;
    }
  });
  
}

document.getElementById("registrationForm").addEventListener("submit", (event) => {
handleRegistration(event);
});