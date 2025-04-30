const date = new Date().setDate(new Date().getDate());


localStorage.setItem('Test-Item', JSON.stringify({
value:"string",
expDate:date,


}))