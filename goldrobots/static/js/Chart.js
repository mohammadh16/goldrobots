var xValues = ["Sat","Sun","Mon","Tue","Wed","Thu","Fri"];

new Chart("myChart", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{
      data: [2,14,20,16,22,18,30,40],
      borderColor: "#BA6D18",
      fill: false
    },{
      data: [3,10,7,15,13,20,23,35],
      borderColor: "#F2D884",
      fill: false
    }]
  },
  options: {
    legend: {display: false}
  }
});

