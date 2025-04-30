const raw = localStorage.getItem('userSelections');
if (raw) {
  const data = JSON.parse(raw);
  const group = 'group1'; 

  if (data[group]) {
    const labels = Object.keys(data[group]);       
    const values = Object.values(data[group]);     

    const ctx = document.getElementById('myChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Your Submission',
          data: values,
          backgroundColor: ['#FF6384', '#FFCE56', '#4BC0C0'],
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: { beginAtZero: true }
        }
      }
    });
  }
}



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





