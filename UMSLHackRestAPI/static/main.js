
const Http = new XMLHttpRequest();
const url='http://127.0.0.1:8000/api/v1/predict';
var parameters = JSON.stringify({
    "start_year": 2017,
    "end_year": 2021,
    "state": "Missouri",
    "factor": "average_AQI"
});
Http.open("POST", url, true);
Http.setRequestHeader('Content-type', 'application/json');
//Http.send(parameters);


Http.onreadystatechange = (e) => {
  console.log(Http.responseText)
}