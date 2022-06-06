
import * as Chartist from 'chartist';
import { Component, OnInit, ViewChild } from '@angular/core';

import * as Highcharts from 'highcharts';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
highcharts=Highcharts;
chartOptions={
title:{

},
xAxis:{

},
yAxis:{

},
series:[{
  name:"US",
  data:[11,23,43]
},
{
  name:"Maroc",
  data:[11,22,41]
}]

}
  constructor() { }

  // public pivotReport = {
  //   dataSource: {
  //     filename: "../../assets/data/produit.csv"
  //   },
  //   slice: {
  //     rows: [{
  //       uniqueName: "Date",
  //       filter: {
  //         query: {
  //           last: "month",
  //         },
  //       },
  //     }, ],
  //     columns: [{
  //         uniqueName: "Country/Region",
  //         filter: {
  //           members: ["country/region.[us]"],
  //         },
  //       },
  //       {
  //         uniqueName: "[Measures]",
  //       },
  //     ],
  //     measures: [{
  //         uniqueName: "Active",
  //         aggregation: "sum",
  //       },
  //       {
  //         uniqueName: "Recovered",
  //         aggregation: "sum",
  //       }
  //     ],
  //   },
  // };
  

ngOnInit(): void {}
}
