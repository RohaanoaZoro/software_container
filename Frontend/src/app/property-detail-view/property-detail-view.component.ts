import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-property-detail-view',
  templateUrl: './property-detail-view.component.html',
  styleUrls: ['./property-detail-view.component.css']
})
export class PropertyDetailViewComponent implements OnInit {

  constructor(public activatedRoute: ActivatedRoute) { }

  ngOnInit(): void {


    this.activatedRoute.params.subscribe(params => {
      console.log(params);
      this.property = JSON.parse(atob(params['id'])); 
      debugger
      });
      
    
    
  }

  @Input() property: any = {
    _id: "jdkvmeowjgmpwegmp",
    greenscore: 2.5,
    address: "Amsterdam",
    propertyvalues: []
  };

}
