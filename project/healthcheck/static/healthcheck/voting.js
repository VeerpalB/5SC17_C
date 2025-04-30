let currentTab = 0;
showTab(currentTab);

function showTab(n) {
  const tabs = document.getElementsByClassName("tab");
  for (let i = 0; i < tabs.length; i++) {
    tabs[i].style.display = "none";
  }
  if (tabs[n]) {
    tabs[n].style.display = "block";
  }

  const prevBtn = document.querySelector('#prevBtn');
  const nextBtn = document.querySelector('#nextBtn');

  if (prevBtn) prevBtn.style.display = n === 0 ? "none" : "inline";
  if (nextBtn) nextBtn.innerHTML = (n === tabs.length - 1) ? "Submit" : "Next";
}

function nextPrev(n) {
  const tabs = document.getElementsByClassName("tab");

  if ((currentTab + n) >= tabs.length) {
    // Final submission
    document.querySelector('form').submit();
    return false;
  }

  tabs[currentTab].style.display = "none";
  currentTab += n;
  showTab(currentTab);
}

// Track selections for trend/state
document.querySelectorAll('.select-box').forEach(box => {
  box.addEventListener('click', function () {
    const group = this.getAttribute('data-group');
    const value = this.getAttribute('data-value');
    const parentTab = this.closest('.tab');

    // Deselect siblings
    parentTab.querySelectorAll(`.select-box[data-group="${group}"]`).forEach(el => {
      el.classList.remove('selected');
    });

    this.classList.add('selected');

    // Set hidden input
    if (group === 'group1') {
      const trendInput = parentTab.querySelector('.trend-input');
      if (trendInput) trendInput.value = value;
    } else if (group === 'group2') {
      const stateInput = parentTab.querySelector('.state-input');
      if (stateInput) stateInput.value = value;
    }
  });
});
