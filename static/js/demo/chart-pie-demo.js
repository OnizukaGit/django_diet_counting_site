
    var chartData = document.getElementById("chart-data");
    var BMI = parseFloat(chartData.getAttribute("data-bmi"));

    var ctx = document.getElementById("myPieChart");
    var bmiValue = parseFloat(chartData.getAttribute("data-bmi"));

    var myPieChart = new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: ["BMI", "Norma"],
        datasets: [{
          data: [bmiValue, 100 - bmiValue],
          backgroundColor: ['#4e73df', '#d3d3d3'],
          hoverBackgroundColor: ['#2e59d9', '#a9a9a9'],
          hoverBorderColor: "rgba(234, 236, 244, 1)",
        }],
      },
      options: {
        maintainAspectRatio: false,
        tooltips: {
          backgroundColor: "rgb(255,255,255)",
          bodyFontColor: "#858796",
          borderColor: '#dddfeb',
          borderWidth: 1,
          xPadding: 15,
          yPadding: 15,
          displayColors: false,
          caretPadding: 10,
        },
        legend: {
          display: false
        },
        cutoutPercentage: 80,
      },
    });

