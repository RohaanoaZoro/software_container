import { Component } from '@angular/core';

import { ApiHandlerService } from '../services/api-handler/api-handler.service'
import { propertyStructure } from '../structures/property'

@Component({
  selector: 'app-view-property',
  templateUrl: './view-property.component.html',
  styleUrls: ['./view-property.component.css']
})
export class ViewPropertyComponent {

  constructor( private myApiHandler: ApiHandlerService) { }

  public properties:propertyStructure[] = [];


  ngOnInit(): void {
    //This is the code to get the property details
     this.myApiHandler.getProperty().subscribe(data => {
      this.properties = data; 
      
      console.log("home data", this.properties)
    });
  }

  showFilter: boolean = false;
  toggleFilter(){
      this.showFilter = !this.showFilter;       
  }

  propertyBtoa(property: any): string {
    return btoa(JSON.stringify(property)); 

  }

}
