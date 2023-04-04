import { Component } from '@angular/core';
import { propertyStructure } from '../structures/property';
import { ApiHandlerService } from '../services/api-handler/api-handler.service';


@Component({
  selector: 'app-add-property',
  templateUrl: './add-property.component.html',
  styleUrls: ['./add-property.component.css']
})
export class AddPropertyComponent {

  

  public property: propertyStructure = {
    _id: { "$oid": ""},
    greenscore: 0,
    address: '',
    name:'',
    description:'',
    propertyvalues: {
      energy: '',
      co2: 0,
      waste: 0,
      cleanenergy: 0,
      area: 0,
      propertytype: ''
    }
  }

  public res: any;


  constructor(private myApiHandler: ApiHandlerService) { }

  onSubmit() {
    console.log("property", this.property)

    this.res = this.property;
    delete this.res["_id"];
    this.myApiHandler.addProperty(this.res).subscribe((response)=> {console.log("response", response)})
    console.log("submit res", this.res)
  }
  
}
