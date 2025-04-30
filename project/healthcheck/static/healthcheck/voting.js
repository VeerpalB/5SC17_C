let currentTab = 0;
let selections = {};

showTab(currentTab);

function showTab(n) {
  const tabs = document.getElementsByClassName("tab");
  for (let i = 0; i < tabs.length; i++) {
    tabs[i].style.display = "none";
  }
  if (tabs[n]) {
    tabs[n].style.display = "block";
  }

  const prevBtn = document.querySelector('button[onclick="nextPrev(-1)"]');
  const nextBtn = document.querySelector('button[onclick="nextPrev(1)"]');

  if (prevBtn) prevBtn.style.display = n === 0 ? "none" : "inline";
  if (nextBtn) nextBtn.innerHTML = (n === tabs.length - 1) ? "Submit" : "Next";
}

function nextPrev(n) {
  const tabs = document.getElementsByClassName("tab");

  if ((currentTab + n) >= tabs.length) {
    localStorage.setItem("surveySelections", JSON.stringify(selections));
    alert("We are now saving your selections. View your progress in the next page.");
    window.location.href = "/progress";  
    return false;
  }

  tabs[currentTab].style.display = "none";
  currentTab += n;
  showTab(currentTab);
}

document.querySelectorAll('.select-box').forEach(box => {
  box.addEventListener('click', function () {
    const group = this.getAttribute('data-group');
    const value = this.getAttribute('data-value');

    document.querySelectorAll(`.select-box[data-group="${group}"]`).forEach(el => {
      el.classList.remove('selected');
    });

    this.classList.add('selected');

    selections[group] = value;
  });
});
