import { Component, OnInit, Input } from '@angular/core';
import { propertyStructure } from '../structures/property'

@Component({
  selector: 'app-property-card',
  templateUrl: './property-card.component.html',
  styleUrls: ['./property-card.component.css']
})
export class PropertyCardComponent {


  constructor() {




  }

  @Input() property: any = {
    _id: "jdkvmeowjgmpwegmp",
    greenscore: 2.5,
    address: "Amsterdam",
    propertyvalues: []
  };


}
