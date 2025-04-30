

const trendCounts = { 'Red': 0, 'Yellow': 0, 'Green': 0 };
const stateCounts = { 'Getting worse': 0, 'Stable': 0, 'Improving': 0 };

voteData.forEach(item => {
  const color = item.status__statusColor.toLowerCase();
  if (['red', 'yellow', 'green'].includes(color)) {
    trendCounts[item.status__statusColor] += item.count;
  } else if (['worse', 'stable', 'improving'].includes(color)) {
    const map = {
      'worse': 'Getting worse',
      'stable': 'Stable',
      'improving': 'Improving'
    };
    stateCounts[map[color]] += item.count;
  }
});

new Chart(document.getElementById('trendChart'), {
  type: 'bar',
  data: {
    labels: Object.keys(trendCounts),
    datasets: [{
      label: 'Trend',
      data: Object.values(trendCounts),
      backgroundColor: ['red', 'yellow', 'green']
    }]
  }
});

new Chart(document.getElementById('stateChart'), {
  type: 'bar',
  data: {
    labels: Object.keys(stateCounts),
    datasets: [{
      label: 'State',
      data: Object.values(stateCounts),
      backgroundColor: ['red', 'yellow', 'green']
    }]
  }
})















// const raw = localStorage.getItem('userSelections');
// if (raw) {
//   const data = JSON.parse(raw);
//   const group = 'group1'; 

//   if (data[group]) {
//     const labels = Object.keys(data[group]);       
//     const values = Object.values(data[group]);     

//     const ctx = document.getElementById('myChart').getContext('2d');
//     new Chart(ctx, {
//       type: 'bar',
//       data: {
//         labels: labels,
//         datasets: [{
//           label: 'Your Submission',
//           data: values,
//           backgroundColor: ['#FF6384', '#FFCE56', '#4BC0C0'],
//           borderWidth: 1
//         }]
//       },
//       options: {
//         scales: {
//           y: { beginAtZero: true }
//         }
//       }
//     });
//   }
// }



// const item = localStorage.setItem('Test-Item', JSON.stringify);
// if(item){
//   const rest = (new Date()).getTime()>= JSON.parse(item).expDate;
// if (res){
  
//     localStorage.removeItem('Test-Item');
//   }else{
//     console.log(JSON.parse(item).value);

// }
// } else {
// console.log("no item found");


// }





