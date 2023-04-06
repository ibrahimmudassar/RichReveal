$(document).ready(function () {
  // DataTable
  var table = $("#mainTable").DataTable({
    autoFill: true,
    stateSave: true,
    order: [[3, "desc"]],

    scrollY: "98vh",
    scrollCollapse: true,

    lengthMenu: [
      [15, 50, 100, -1],
      [15, 50, 100, "All"],
    ],

    deferRender: true,
    ajax: {
      url: "https://raw.githubusercontent.com/ibrahimmudassar/RichReveal/main/billionaires.csv",
      dataType: "text",
      dataSrc: function (csvdata) {
        return $.csv.toObjects(csvdata);
      },
    },
    responsive: true,
    columnDefs: [
      { responsivePriority: 1, targets: 0 },
      { responsivePriority: 2, targets: 1 },
    ],

    columns: [
      { data: "personName" },
      { data: "rank" },
      { data: "source" },
      { data: "birthDate" },
      { data: "countryOfCitizenship" },
      { data: "finalWorth" },
      { data: "Percentile" },
    ],
  });
});
