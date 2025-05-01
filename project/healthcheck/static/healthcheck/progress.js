
const trendLabels = JSON.parse(document.getElementById('user-trend-labels').textContent);
const trendData = JSON.parse(document.getElementById('user-trend-data').textContent);
const stateLabels = JSON.parse(document.getElementById('user-state-labels').textContent);
const stateData = JSON.parse(document.getElementById('user-state-data').textContent);

new Chart(document.getElementById('userTrendChart').getContext('2d'), {
  type: 'bar',
  data: {
    labels: trendLabels,
    datasets: [{
      label: 'Your Trend Votes',
      data: trendData,
      backgroundColor: ['red', 'gold', 'green']
    }]
  },
  options: {
    responsive: true,
    scales: { y: { beginAtZero: true } }
  }
});

new Chart(document.getElementById('userStateChart').getContext('2d'), {
  type: 'bar',
  data: {
    labels: stateLabels,
    datasets: [{
      label: 'Your State Votes',
      data: stateData,
      backgroundColor: ['red', 'gold', 'green']
    }]
  },
  options: {
    responsive: true,
    scales: { y: { beginAtZero: true } }
  }
});


