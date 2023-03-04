var xValues = ["Your Share","Bulima Share"];
var yValues = [60, 40];
var barColors = [
    "#FAE25B",
  "#E2912D"
];

new Chart("myChart", {
  type: "pie",
  options: {
    legend: {
       display: false
    }
},
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  
});
