// Pobierz wagę ciała z Django i przekształć ją w liczbę zmiennoprzecinkową
var weightData = parseFloat('{{ weight }}');

// Utwórz tablicę etykiet na podstawie dostępnych danych (miesiące)
var labels = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"];

// Utwórz tablicę z danymi wagi (zaczynając od wartości wagi z bazy danych)
var weightDataset = [weightData];

var ctx = document.getElementById("myAreaChart");
var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: labels,
    datasets: [{
      label: "Waga ciała", // Zaktualizuj etykietę
      lineTension: 0.3,
      backgroundColor: "rgba(78, 115, 223, 0.05)",
      borderColor: "rgba(78, 115, 223, 1)",
      pointRadius: 3,
      pointBackgroundColor: "rgba(78, 115, 223, 1)",
      pointBorderColor: "rgba(78, 115, 223, 1)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
      pointHoverBorderColor: "rgba(78, 115, 223, 1)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: weightDataset, // Zaktualizuj dane
    }],
  },
  options: {
    // ... (inne opcje wykresu pozostają bez zmian)
  }
});
