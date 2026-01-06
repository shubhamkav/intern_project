let formsOpen = true; // frontend-tracked state

const statusEl = document.getElementById("status");
const citySelect = document.getElementById("city");
const rows = document.getElementById("rows");

// ---------------- UI UPDATE ----------------
function updateUI() {
  const label = document.getElementById("formStatusLabel");
  const closeBtn = document.getElementById("closeBtn");
  const openBtn = document.getElementById("openBtn");

  if (formsOpen) {
    label.innerText = "OPEN";
    label.className = "status-open";
    closeBtn.disabled = false;
    openBtn.disabled = true;
  } else {
    label.innerText = "CLOSED";
    label.className = "status-closed";
    closeBtn.disabled = true;
    openBtn.disabled = false;
  }
}

// ---------------- CITY SYNC ----------------
async function syncCity() {
  const city = citySelect.value;
  statusEl.innerText = `Syncing ${city}...`;

  await fetch(`http://127.0.0.1:8000/sync/${city}`, {
    method: "POST"
  });

  statusEl.innerText = `Sync completed for ${city}`;
}

// ---------------- LOAD DATA ----------------
async function loadData() {
  const city = citySelect.value;
  statusEl.innerText = "Loading data...";

  const res = await fetch(
    `http://127.0.0.1:8000/admin/responses/${city}`
  );
  const data = await res.json();

  rows.innerHTML = "";
  data.forEach(r => {
    rows.innerHTML += `
      <tr>
        <td>${r.full_name}</td>
        <td>${r.email}</td>
        <td>${r.mobile || ""}</td>
        <td>${r.gender || ""}</td>
        <td>${r.nationality || ""}</td>
      </tr>
    `;
  });

  statusEl.innerText = `Loaded ${data.length} records`;
}

// ---------------- CONFIRMATION (ONLY HERE) ----------------
function confirmClose() {
  const ok = confirm("Are you sure you want to CLOSE all Google Forms?");
  if (!ok) return;
  closeAllForms();
}

function confirmOpen() {
  const ok = confirm("Are you sure you want to OPEN all Google Forms?");
  if (!ok) return;
  openAllForms();
}

// ---------------- FORM CONTROL ----------------
async function closeAllForms() {
  statusEl.innerText = "Closing all forms...";

  await fetch("http://127.0.0.1:8000/forms/close-all", {
    method: "POST"
  });

  formsOpen = false;
  updateUI();
  statusEl.innerText = "All forms are CLOSED";
}

async function openAllForms() {
  statusEl.innerText = "Opening all forms...";

  await fetch("http://127.0.0.1:8000/forms/open-all", {
    method: "POST"
  });

  formsOpen = true;
  updateUI();
  statusEl.innerText = "All forms are OPEN";
}

// ---------------- INIT ----------------
updateUI();
