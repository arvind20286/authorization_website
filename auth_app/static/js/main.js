window.onload = function () {
  google.accounts.id.initialize({
    client_id:
      "775820619887-949m71g9o41l44qu8evrg83ivbi4tbhq.apps.googleusercontent.com",
    login_uri:
      "https://1098-2401-4900-1c21-8ffa-f8b5-8e0-8429-f8be.ngrok-free.app/auth_app/google-signin/",
    ux_mode: "redirect",
  });
  const parent = document.getElementById("google_btn");
  google.accounts.id.renderButton(parent, {
    theme: "filled_black",
    size: "large",
  });
  google.accounts.id.prompt();
};

const togglePassword = document.querySelector("#togglePassword");
const passwordField = document.querySelector("#floatingPassword");

togglePassword.addEventListener("click", function () {
  const type =
    passwordField.getAttribute("type") === "password" ? "text" : "password";
  passwordField.setAttribute("type", type);

  // Toggle the icon class between eye and eye-slash
  this.classList.toggle("bi-eye");
  this.classList.toggle("bi-eye-slash");
});
async function isValid() {
  let is_valid = false;
  let form = document.getElementById("login_form");
  let formData = {};
  for (let i = 0; i < form.elements.length; i++) {
    let element = form.elements[i];
    if (element.type !== "submit") {
      formData[element.name] = element.value;
    }
  }
  let jsonData = JSON.stringify(formData);
  console.log(jsonData);
  await fetch(verify_url, {
    method: "POST",
    body: jsonData,
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      if (data.user_exists) {
        is_valid = true;
        console.log(is_valid);
      }
    });
  console.log(is_valid);
  if (!is_valid) {
    // document.getElementById("error_message").style.display = "block";
    document.getElementById("error_message").classList.remove("d-none");
    document.getElementById("error_message").innerText =
      "Invalid email or password!";
  } else {
    window.location.href = welcome_page_url;
  }
}
document.getElementById("login_form").addEventListener("submit", function (e) {
  e.preventDefault();
  isValid();
});

