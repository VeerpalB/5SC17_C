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
    document.querySelector('form').submit();
    return false;
  }

  tabs[currentTab].style.display = "none";
  currentTab += n;
  showTab(currentTab);
}

document.querySelectorAll('.select-box').forEach(box => {
  box.addEventListener('click', () => {
    const group = box.getAttribute('data-group');
    const value = box.getAttribute('data-value');
    const parentTab = box.closest('.tab');
    parentTab.querySelectorAll(`.select-box[data-group="${group}"]`).forEach(b => b.classList.remove('selected'));
    box.classList.add('selected');
    if (group === 'group1') {
      parentTab.querySelector('.trend-input').value = value;
    } else if (group === 'group2') {
      parentTab.querySelector('.state-input').value = value;
    }
  });
});
