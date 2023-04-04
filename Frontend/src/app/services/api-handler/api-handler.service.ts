import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { propertyStructure } from '../../structures/property'
import { Observable } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})

export class ApiHandlerService {

  constructor(private http: HttpClient, private router: Router) { }

  //private _url: string = 'https://uvadevops.azurewebsites.net/';
  // private _url: string = 'http://localhost:7071/';
  private _url: string = this.router.url+"api/";

  getProperty(): Observable<propertyStructure[]>{
    var res = this.http.get<propertyStructure[]>(this._url+"getProperty");
    return res;

    
  }

  addProperty(data: any){
    var res = this.http.post(this._url+"addProperty", data);
    return res;
  }
}
