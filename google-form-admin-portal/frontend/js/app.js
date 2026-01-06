async function login() {
  const res = await fetch("http://127.0.0.1:8000/auth/login", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      username: username.value,
      password: password.value
    })
  });

  if (res.ok) {
    window.location.href = "dashboard.html";
  } else {
    msg.innerText = "Invalid login";
  }
}
