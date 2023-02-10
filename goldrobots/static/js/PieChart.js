var xValues = ["Italy", "France"];
var yValues = [60, 40];
var barColors = [
    "#FAE25B",
  "#E2912D"
];

new Chart("myChart", {
  type: "pie",
  data: {
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  
});