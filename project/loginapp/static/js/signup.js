function passwordcheck() {
  let password1 = document.getElementById("password1");
  let password2 = document.getElementById("password2");
  let passwordcheck = document.getElementsByClassName("passwordchecktxt")[0];
  if (password1.value != password2.value) {
    passwordcheck.style.display = "block";
    password2.style.marginBottom = "0px";
    return false;
  } else {
    passwordcheck.style.display = "none";
    password2.style.marginBottom = "20px";
    return true;
  }
}
function signupcheck() {
  if (password1.value != password2.value) {
    alert("비밀번호를 확인해주세요");
    return;
  }
}
