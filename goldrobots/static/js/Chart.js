var xValues = ["Sat","Sun","Mon","Tue","Wed","Thu","Fri"];


new Chart("myChart", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{
      label: 'Last Week',
      data: [2,5,20,16,22,18,30,40],
      borderColor: "#BA6D18",
      fill: false
    },{
      label: 'This Week',
      data: [3,10,7,15,13,20,23,35],
      borderColor: "#F2D884",
      fill: false
    }]
  },
  options: {
    legend: {display: true}
  }
});


